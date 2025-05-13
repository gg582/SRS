from flask import Blueprint, request, jsonify
from models.user import User
from extensions import db

bp = Blueprint('auth', __name__)

@bp.route('/api/login', methods=['POST'])
def login_or_register():
    print("✅ /api/login 요청 도착")

    # 1. 헤더 로그 확인
    headers = dict(request.headers)
    print("🔎 요청 헤더:", headers)

    # 2. ID 토큰이 있는가?
    auth_header = headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        print("❌ Authorization 헤더 누락 또는 잘못됨")
        return jsonify({"error": "Authorization token required"}), 401

    token = auth_header.split(" ")[1]
    print("🧾 받은 토큰:", token[:30], "...")  # 토큰 일부만 출력

    # 3. 요청 본문(JSON)
    data = request.get_json()
    print("📦 요청 본문:", data)

    # 임시로 이메일만 사용
    email = data.get('email')
    name = data.get('name', '이름없음')

    # 4. 사용자 등록 또는 찾기
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email, name=name)
        db.session.add(user)
        db.session.commit()
        print(f"🆕 사용자 생성: {email}")

    print(f"✅ 로그인 완료: user_id={user.id}")
    return jsonify({
        "id": user.id,
        "email": user.email,
        "name": user.name
    })
