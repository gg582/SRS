from app import app
from extensions import db
from models import seat

with app.app_context():
    db.create_all()

    if seat.Seat.query.count() == 0:
        print("🪑 좌석 더미 데이터 삽입 중...")
        for i in range(1, 6):
            db.session.add(seat.Seat(id=i, status='available'))
        db.session.commit()
        print("✅ 좌석 데이터 삽입 완료")
    else:
        print("ℹ️ 좌석 데이터 이미 존재함")
