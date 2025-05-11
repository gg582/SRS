from flask import Blueprint, request, jsonify
from models.reservation import Reservation
from models.seat import Seat
from extensions import db
from datetime import datetime

bp = Blueprint('reserve', __name__)

@bp.route('/api/reserve', methods=['POST'])
def reserve_seat():
    data = request.get_json()
    user_id = data.get('user_id')
    seat_id = data.get('seat_id')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    try:
        # 문자열 → datetime 변환
        start_dt = datetime.fromisoformat(start_time)
        end_dt = datetime.fromisoformat(end_time)
    except Exception:
        return jsonify({"error": "날짜 형식이 잘못되었습니다."}), 400

    # 중복 예약 검사
    conflict = Reservation.query.filter(
        Reservation.seat_id == seat_id,
        Reservation.end_time > start_dt.isoformat(),
        Reservation.start_time < end_dt.isoformat(),
        Reservation.status == 'reserved'
    ).first()

    if conflict:
        return jsonify({"error": "해당 시간에 이미 예약된 좌석입니다."}), 409

    # 좌석 존재 확인 및 상태 변경
    seat = Seat.query.get(seat_id)
    if not seat:
        return jsonify({"error": "해당 좌석이 존재하지 않습니다."}), 404

    seat.status = 'reserved'  # ✅ 좌석 상태 변경

    # 예약 생성
    reservation = Reservation(
        user_id=user_id,
        seat_id=seat_id,
        start_time=start_time,
        end_time=end_time,
        status='reserved'
    )

    db.session.add_all([reservation, seat])  # 두 객체 모두 커밋
    db.session.commit()

    return jsonify({"message": "예약이 완료되었습니다."}), 201
