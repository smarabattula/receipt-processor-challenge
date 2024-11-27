import uuid

def get_unique_id() -> str:
    """
    Generates 128 bit uuid string
    """
    unique_id = uuid.uuid4()
    return str(unique_id)
