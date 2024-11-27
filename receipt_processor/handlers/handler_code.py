from receipt_processor.util.calculate_points import calculate_points
from receipt_processor.util.utils import get_unique_id
import logging

logging.basicConfig(level=logging.DEBUG)

receipts = {}
points = {}

def search_id(id: str):
    """
    Search
    """
    if id in receipts:
        return receipts[id]
    else:
         return None

def get_receipt_points_by_id(id):

    res = search_id(id)
    if not res:
        return {"Error": "No receipt found for that id"}, 404

    if id in points:
        return points[id]

    curr_points = calculate_points(res)

    points[id] = curr_points
    return {"points": curr_points}, 200

def post_receipt(body):
    """
    Input: Submits a receipt for processing
    Output: Returns the ID assigned to the receipt
    """

    receipt_id = get_unique_id()
    receipts[receipt_id] = body
    response = {"id": receipt_id}
    return response, 200
