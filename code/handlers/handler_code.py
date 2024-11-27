from util.calculate_points import calculate_points
from util.utils import get_unique_id
import json
import logging

logging.basicConfig(level=logging.DEBUG)

receipts = {}
points = {}

def search_id(id: str):
    if id in receipts:
        return receipts[id]
    else:
         return None

def get_receipt_points_by_id(id):
    res = search_id(id)
    if not res:
        return json.dumps({"Error": "No receipt found for that id"}), 404
    points = calculate_points(res)
    return {"points": points}, 200

def post_receipt(body):
    """
    Input: Submits a receipt for processing
    Output: Returns the ID assigned to the receipt
    """

    receipt_id = get_unique_id()
    receipts[receipt_id] = body
    response = json.dumps({"id": receipt_id})
    return response, 200
