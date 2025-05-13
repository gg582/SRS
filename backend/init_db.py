from app import app
from extensions import db
from models import user, seat, reservation

with app.app_context():
    print("⚠️ 좌석 및 예약 테이블 초기화 중 (사용자 유지)")
    # 예약 및 좌석 테이블만 삭제 후 생성
    reservation.Reservation.__table__.drop(db.engine)
    seat.Seat.__table__.drop(db.engine)
    db.create_all()

    print("🪑 좌석 더미 데이터 삽입 중...")
    for i in range(1, 6):
        db.session.add(seat.Seat(id=i, status='available'))
    db.session.commit()
    print("✅ 좌석 데이터 삽입 완료 (사용자 정보는 유지됨)")
