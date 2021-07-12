from config_API.config import engine
import pandas as pd

# Function to get all users name with their corresponding id (needed to post data into the Messages table)
def users_list():
    query_1 = f""" SELECT user_id, character_name
FROM Users
"""
    data_1 = pd.read_sql_query(query_1,engine)
    return data_1.to_json(orient="records")

# Function to get all groups with their corresponding id (needed to post data into the Messages table)
def groups_list():
    query_2 = f""" SELECT group_id, group_number
FROM Groups_chats
"""
    data_2 = pd.read_sql_query(query_2,engine)
    return data_2.to_json(orient="records")

# Function to get all messages sent in the the different groups in the chat by every user
def message_list():
    query_3 = f""" SELECT message, user_id, group_id
FROM Messages
"""
    data_3 = pd.read_sql_query(query_3,engine)
    return data_3.to_json(orient="records")    

# Function to get all messages sent in a specific chat
def messages_group(group):
    query_4 = f""" SELECT message_id, message, user_id
FROM Messages
WHERE group_id = "{group}"

"""
    data_4 = pd.read_sql_query(query_4,engine)
    return data_4.to_json(orient="records")

# Function to get all messages sent by a given user
def messages_user(user):
    query_5 = f""" SELECT message_id, message, user_id
FROM Messages
WHERE user_id = "{user}"

"""
    data_5 = pd.read_sql_query(query_5,engine)
    return data_5.to_json(orient="records")