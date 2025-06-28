def individual_serial(todo) ->dict:
    
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"]
    }
    
def list_serial(todos) -> list:
    """
    Serializes a list of todo items into a list of dictionaries.
    
    Args:
        todos (list): List of todo items.
        
    Returns:
        list: List of serialized todo items.
    """
    return [individual_serial(todo) for todo in todos]