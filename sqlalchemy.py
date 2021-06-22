import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:hadoop@localhost') # connect to server
engine.execute("CREATE DATABASE jira") #create db
engine.execute("USE jira") 