from app import app, db
from sqlalchemy import inspect

with app.app_context():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print("📋 현재 데이터베이스에 존재하는 테이블 목록:")
    for table in tables:
        print(f" - {table}")
