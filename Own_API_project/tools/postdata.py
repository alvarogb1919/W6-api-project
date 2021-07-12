from config_API.config import engine

# Function to add a message by a specific character to a specific group

def insert_message(message, user_id, group_id):
    engine.execute(
        f"""
        INSERT INTO Messages (message, user_id, group_id) VALUES
        ('{message}',{user_id},{group_id});
       """
    )

# Function to create a new group in the chat (must be a group number that doesn't exist already)

def create_group(group_number):
    engine.execute(
        f"""
        INSERT INTO Groups_chats (group_number) VALUES
        ({group_number});
       """
    )

# Function to add an existing user to a chat

def add_user(user_id, group_id):
    
    engine.execute(
        f"""
        INSERT INTO Connections (user_id, group_id) VALUES
        ({user_id}, {group_id});
       """
    )

# Function to create a new user

def create_user(character_name):
    
    engine.execute(
        f"""
        INSERT INTO Users (character_name) VALUES
        ('{character_name}');
       """
    )