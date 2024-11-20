#!/usr/bin/env python

import uuid

from flask import Flask, request, jsonify
from werkzeug.exceptions import UnsupportedMediaType

from points_service import PointsService

app = Flask(__name__)
data = {}


@app.route('/receipts/process', methods=['POST'])
def post_receipt():
    try:
        payload = request.get_json()
    except UnsupportedMediaType:
        return jsonify({'Error': 'Bad Request'}), 400

    receipt_id = str(uuid.uuid4())
    data[receipt_id] = payload
    return {'id': receipt_id}


@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_receipt(receipt_id: str):
    if not receipt_id:
        return jsonify({"Error": "Missing ID parameter in request"}), 400
    receipt = data.get(receipt_id)
    if receipt:
        return {"points": PointsService.calculate_points(receipt)}
    return jsonify({'Error': 'Not Found'}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
