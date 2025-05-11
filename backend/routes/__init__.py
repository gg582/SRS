from .seats import bp as seats_bp

def register_routes(app):
    print("🔗 register_routes() 함수 진입")
    app.register_blueprint(seats_bp)
    print("✅ seats_bp 등록 완료")