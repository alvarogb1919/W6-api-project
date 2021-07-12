# W6-api-project
API creation project

![The Office](https://www.laprimerapiedra.com.ar/wp-content/uploads/the-office-1200.jpg)

### Welcome to my fourth Ironhack project! The purpose of this project was mainly to create an API that will be able to receive information, store it, or serve it when needed.


# Scope of the project
The main goal of the project was to create an API that serves information to clients (in response to their GET requests) and receives data from your clients (via their POST requests) and saves it in the corresponding database, in this case , "The Office chat" database.

# Approach and result

## 1.0: Data source 
The first step of the project was to find an existing database in Kaggle from which I could source data in order to feed it to a newly created database. I was able to find a database containing all the sripts from every season of the show "The Office" which included key information such as scene number, character name, and message.

## 2.0: Data handling and cleaning
With this data, I then manipulated it and cleaned it in order to get just the data from one specific episode which will recreate a virtual office chat. This cleaning process can be explored in the notebook: "Dataset_cleaning" within the "Dataset" file inside the "Notebooks" file.

## 3.0: Database creation and feeding in SQL
The next step was to create the database in which to store this information. The database platform I decided to use for this case is SQL. Consequently, I created the database called "The_Office_chat" in which I inserted four tables:
 - Users: Including the user_id (PK) and user_name
 - Groups: Including the group_id (PK) and group number
 - Connections: Including the connection id (PK), user_id (FK), and group_id (FK)
 - Messages: Including the message_id (PK), message, user_id (FK), and group_id (FK)

The entire process can be explored in the notebook: "SQL_DBCreation_&_feeding" within the "SQL" file inside the "Notebooks" file.

## 4.0: API creation
In order for clients to be able to access the database that has been created and to modify it, and API needs to be created using Flask library in Python. This process is fully visible and transparent in the "The_Office_API" python file in the main folder. It is important to mention that this file feeds from 2 main python files: "getdata" and "postdata", both located in the "tools" folder. Basically each file contains the defined functions I have created that will allow the client to extract (GET) specific data by calling the API and also include data (POST).

## 5.0: API testing
Finally, I wanted to actually test that the API was working correctly and it was possible to call it without any problem. Fortunately the API worked just fine in both ways ;). This process can be explored in the notebook: "API_testing" within the "API_call" folder inside the "Notebooks" file.

## 6.0: Pending steps - Sentiment analysis
One additional step that remained pending was to extract the emotional value of the messages in the "The_Office_chat" via NLTK (sentiment analysis.)

## Sources and libraries used
- Pandas - https://pandas.pydata.org/
- Flask - https://pypi.org/project/Flask/
- SQL Alchemy - https://docs.sqlalchemy.org/en/14/
- Requests - https://docs.python-requests.org/en/master/
- Kaggle - https://www.kaggle.com/datasets

## Files structure
Simple structure ;):
- "config_API" folder containing the required configuration code for the API that is then exported in the "The_Office_API" python file
- "Notebooks" folder containig the jupyter notebooks used for different purposes: 1) API call testing; 2) Dataset handling; 3) SQL via python
- "tools" folder including the "getdata" and "postdata" python files that have the defined functions to be included in the API interaction context
- "The_Office_API" python file including the main code for the API creation
- "The_Office_chat" SQL file including the database so that the process can be replicated with the same database in another terminal / computer

# That's all! Thank you for your interest :)