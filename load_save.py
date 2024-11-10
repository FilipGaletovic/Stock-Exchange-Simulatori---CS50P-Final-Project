import json
import os
import sys

#Load users function, returns a list of users if they exist, otherwise it returns empty list
def load_users(filename="users.json"):
    """Load user data from a JSON file, handling empty or missing files."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []

#Save function saves users data in a JSON file
def save_users(user, filename="users.json"):
    """Save user data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(user, file, indent=4)



