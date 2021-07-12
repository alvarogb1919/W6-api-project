import os


import os
import dotenv
import sqlalchemy as alch

dotenv.load_dotenv()

passw = os.getenv("pass_sql")
print(passw)
dbName="The_Office_chat"

#Conecto con la base de datos 
connectionData=f"mysql+pymysql://root:admin@localhost/{dbName}"
engine = alch.create_engine(connectionData)