from app import app
from extensions import db
from models import user, seat, reservation

with app.app_context():
    print("⚠️ 모든 테이블 삭제 중...")
    db.drop_all()  # 기존 테이블 전체 삭제
    db.create_all()  # 테이블 재생성
    print("✅ 테이블 재생성 완료")

    # 좌석 더미 데이터 삽입
    print("🪑 좌석 더미 데이터 삽입 중...")
    for i in range(1, 6):
        db.session.add(seat.Seat(id=i, status='available'))
    db.session.commit()
    print("✅ 좌석 데이터 삽입 완료")

