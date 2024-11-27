import pytest
from receipt_processor.util.calculate_points import (
    get_retailer_points,
    get_total_price_points,
    get_item_points,
    get_date_time_points,
    calculate_points
)

def test_get_retailer_points():
    assert get_retailer_points("M&M Corner Market") == 14 #
    assert get_retailer_points("123") == 3
    assert get_retailer_points("!@#$") == 0

def test_get_total_price_points():
    assert get_total_price_points(3.00) == 75  # Whole number and multiple of 0.25
    assert get_total_price_points(2.50) == 25  # Multiple of 0.25
    assert get_total_price_points(2.99) == 0   # None

def test_get_item_points():
    items =  [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ]
    assert get_item_points(items) == 16

def test_get_date_time_points():
    assert get_date_time_points("2022-03-21", "15:00") == 16  # Odd day and between 2-4 PM
    assert get_date_time_points("2022-03-22", "13:00") == 0   # Even day and outside time range
    assert get_date_time_points("2022-03-22", "14:00") == 10  # Time edge case ()
    assert get_date_time_points("2022-03-22", "16:00") == 0   # Time edge case
    assert get_date_time_points("2022-03-21", "16:01") == 6   # Odd day

def test_calculate_points():
    receipt = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
    assert calculate_points(receipt) == 109  # Total points
