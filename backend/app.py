from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Flask 앱 생성
app = Flask(__name__)
CORS(app)

# SQLite 데이터베이스 경로 설정
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, '../database/app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy 객체 생성
db = SQLAlchemy(app)

# 간단한 테스트 라우트
@app.route('/')
def home():
    return jsonify({"message": "Hello from Seat Reservation System!"})

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)

# 모델 임포트 (app.py 맨 아래쪽에 추가)
from models import user, seat, reservation
