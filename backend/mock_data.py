import random

def get_queue_status():
    """Simulates random waiting times for food stalls and washrooms."""
    return [
        {"stall": "Food Stall A", "wait": random.randint(5, 25)},
        {"stall": "Food Stall B", "wait": random.randint(2, 10)},
        {"stall": "Washroom 1", "wait": random.randint(1, 5)},
        {"stall": "Washroom 2", "wait": random.randint(5, 15)}
    ]

def get_crowd_data():
    """Simulates density at various destinations."""
    return {
        "Gate 1": {"crowd_level": "High", "time": "10 mins"},
        "Gate 2": {"crowd_level": "Low", "time": "3 mins"},
        "Gate 3": {"crowd_level": "Medium", "time": "6 mins"},
    }
