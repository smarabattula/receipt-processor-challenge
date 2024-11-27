import json
import uuid
import logging
import math
from typing import List, Dict, Any

logging.basicConfig(level=logging.DEBUG)

receipts = {}
points = {}
def search_id(id: str):
    if id in receipts:
        return receipts[id]
    else:
         return None

def get_unique_id() -> str:
    unique_id = uuid.uuid4()
    return str(unique_id)

def get_items(items: List[Dict[str, str]]) -> Dict[str, List[Any]]:
    """
    Groups items by description and calculates occurrences and total price.
    """
    hash_items = {}
    for item in items:
        item_desc = item["shortDescription"].strip()
        item_price = float(item["price"])
        if item_desc not in hash_items:
            hash_items[item_desc] = [0, item_price]  # [count, price]
        hash_items[item_desc][0] += 1
    return hash_items

def get_retailer_points(retailer_name: str) -> int:
    """
    Calculates points based on alphanumeric characters in the retailer name.
    """
    return sum(1 for s in retailer_name if s.isalnum())


def get_total_price_points(total: float) -> int:
    """
    Calculates points based on the total price:
    +50 if it's a whole number.
    +25 if it's divisible by 0.25.
    """
    points = 0
    if total.is_integer():
        points += 50
    if total % 0.25 == 0:
        points += 25
    return points


def get_item_points(items: List[Dict[str, str]]) -> int:
    """
    Calculates points for items:
    +5 points for every two items.
    +0.2 * price points if the item's description length is divisible by 3.
    """
    points = 5 * (len(items) // 2)  # Points for every two items
    hash_items = get_items(items)
    for desc, (_, price) in hash_items.items():
        if len(desc) % 3 == 0:
            points += math.ceil(0.2 * price)
    return points


def get_date_time_points(item_date: str, item_time: str) -> int:
    """
    Calculates points based on the purchase date and time:
    +6 if the purchase day is odd.
    +10 if the purchase time is between 2:00 PM and 4:00 PM.
    """
    points = 0
    item_day = int(item_date[-2:])
    if item_day % 2 != 0:
        points += 6

    hours = int(item_time[:2])
    if 14 <= hours < 16:
        points += 10

    return points

def calculate_points(receipt: Dict[str, Any]) -> int:
    """
    Main function to calculate total points for a receipt.
    """
    retailer_points = get_retailer_points(receipt["retailer"].strip())
    total_price_points = get_total_price_points(float(receipt["total"]))
    item_points = get_item_points(receipt["items"])
    date_time_points = get_date_time_points(receipt["purchaseDate"], receipt["purchaseTime"])

    # Sum all calculated points
    return retailer_points + total_price_points + item_points + date_time_points

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
