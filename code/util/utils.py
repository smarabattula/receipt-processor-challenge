import uuid

def get_unique_id() -> str:
    """
    Generates a 128 bit uuid string id
    """
    unique_id = uuid.uuid4()
    return str(unique_id)
