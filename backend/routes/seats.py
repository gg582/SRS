from flask import Blueprint, jsonify
from models.seat import Seat

bp = Blueprint('seats', __name__)

@bp.route('/api/seats', methods=['GET'])
def get_seats():
    seats = Seat.query.all()
    result = [{"id": seat.id, "status": seat.status} for seat in seats]
    return jsonify(result)
