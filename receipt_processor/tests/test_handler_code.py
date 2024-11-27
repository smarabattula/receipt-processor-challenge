import pytest
from unittest.mock import patch
from receipt_processor.handlers import handler_code
from receipt_processor.util.calculate_points import calculate_points

# Helper function to reset the receipts dictionary before each test
@pytest.fixture(autouse=True)
def reset_receipts():
    handler_code.receipts.clear()
    handler_code.points.clear()
    yield
    handler_code.receipts.clear()
    handler_code.points.clear()

def test_search_id_found():
    # Arrange
    receipt_id = 'test_receipt_id'
    receipt_data = {
        "retailer": "Test Store",
        "purchaseDate": "2022-03-21",
        "purchaseTime": "15:33",
        "items": [],
        "total": "0.00"
    }
    handler_code.receipts[receipt_id] = receipt_data

    # Act
    result = handler_code.search_id(receipt_id)

    # Assert
    assert result == receipt_data

def test_search_id_not_found():
    # Act
    result = handler_code.search_id('nonexistent_id')

    # Assert
    assert result is None

def test_get_receipt_points_by_id_found():
    # Arrange
    receipt_id = 'test_receipt_id'
    receipt_data = {
        "retailer": "Test Store",
        "purchaseDate": "2022-03-21",
        "purchaseTime": "15:33",
        "items": [
            {"shortDescription": "Item A", "price": "1.00"}
        ],
        "total": "1.00"
    }
    handler_code.receipts[receipt_id] = receipt_data

    # Act
    response, status_code = handler_code.get_receipt_points_by_id(receipt_id)

    # Calculate expected points
    expected_points = calculate_points(receipt_data)

    # Assert
    assert status_code == 200
    assert response == {"points": expected_points}

def test_get_receipt_points_by_id_not_found():
    # Act
    response, status_code = handler_code.get_receipt_points_by_id('nonexistent_id')

    # Assert
    assert status_code == 404
    assert response == {"Error": "No receipt found for that id"}

def test_post_receipt():
    # Arrange
    receipt_data = {
        "retailer": "Test Store",
        "purchaseDate": "2022-03-21",
        "purchaseTime": "15:33",
        "items": [
            {"shortDescription": "Item A", "price": "1.00"}
        ],
        "total": "1.00"
    }

    # Mock get_unique_id
    with patch('receipt_processor.handlers.handler_code.get_unique_id', return_value='test_receipt_id'):
        # Act
        response, status_code = handler_code.post_receipt(receipt_data)

    # Assert
    assert status_code == 200
    assert response == {"id": "test_receipt_id"}
    assert handler_code.receipts["test_receipt_id"] == receipt_data

def test_post_receipt_multiple():
    # Arrange
    receipt_data_1 = {
        "retailer": "Store One",
        "purchaseDate": "2022-03-21",
        "purchaseTime": "10:00",
        "items": [],
        "total": "0.00"
    }
    receipt_data_2 = {
        "retailer": "Store Two",
        "purchaseDate": "2022-03-22",
        "purchaseTime": "12:00",
        "items": [],
        "total": "0.00"
    }

    # Mock get_unique_id to return different IDs
    with patch('receipt_processor.handlers.handler_code.get_unique_id', side_effect=['id1', 'id2']):
        # Act
        response1, status_code1 = handler_code.post_receipt(receipt_data_1)
        response2, status_code2 = handler_code.post_receipt(receipt_data_2)

    # Assert
    assert status_code1 == 200
    assert response1 == {"id": "id1"}
    assert handler_code.receipts["id1"] == receipt_data_1

    assert status_code2 == 200
    assert response2 == {"id": "id2"}
    assert handler_code.receipts["id2"] == receipt_data_2

def test_get_receipt_points_by_id_after_post():
    # Arrange
    receipt_data = {
        "retailer": "Test Store",
        "purchaseDate": "2022-03-21",
        "purchaseTime": "15:33",
        "items": [
            {"shortDescription": "Item A", "price": "1.00"}
        ],
        "total": "1.00"
    }

    with patch('receipt_processor.handlers.handler_code.get_unique_id', return_value='test_receipt_id'):
        # Post the receipt
        handler_code.post_receipt(receipt_data)

    # Act
    response, status_code = handler_code.get_receipt_points_by_id('test_receipt_id')

    # Calculate expected points
    expected_points = calculate_points(receipt_data)

    # Assert
    assert status_code == 200
    assert response == {"points": expected_points}
