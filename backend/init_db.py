from app import app, db
from models import user, seat, reservation

with app.app_context():
    db.create_all()
    print("✅ DB 초기화 완료")
