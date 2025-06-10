from flask import Flask, jsonify
from flask_cors import CORS
from extensions import db
import os
from flask import Flask, redirect

# Flask 앱 생성
app = Flask(__name__)
CORS(app)

# DB 설정
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, '../database/app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # ← 여기서 db와 app을 연결

# 테스트 라우트
@app.route('/')
def root():
    return redirect("/frontend")

# 모델 및 라우트 등록
from models import user, seat, reservation
from routes import register_routes
register_routes(app)

from flask import send_from_directory

@app.route('/frontend')
def frontend_page():
    return send_from_directory('static', 'index.html')

# 실행
if __name__ == '__main__':
    print("🚀 서버 실행 중...")
    app.run(debug=True)


