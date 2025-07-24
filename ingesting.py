import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine
import logging
from sqlalchemy import text
import time
from IPython.display import display, Markdown
from sqlalchemy import create_engine, text
import urllib



class Database:

    def __init__ (self,database_name='master',server_name="ASUSYADAV\\SQLEXPRESS01"):

        """Initializes with the database name and server name.
        Default database is 'master'.
        """
        self.database_name = database_name
        self.server_name = server_name
        self.__conn = None
        self.__connect_to_database()
    

    def __connect_to_database(self,driver = "ODBC Driver 17 for SQL Server"):

        """Connecting to database."""
        try:
            # Step 3: Build the connection string for Windows Authentication
            connection_string = f"mssql+pyodbc://{self.server_name}/{self.database_name}?driver={urllib.parse.quote_plus(driver)}&trusted_connection=yes"

            self.__engine = create_engine(connection_string)
            self.__conn = self.__engine.connect()
            print(f'✅ Connected to database: {self.database_name}')

        except Exception as e:
            print(f"❌ Error connecting to the database: {e}")


    def SQL_script_execution(self,sql_script=None):

        """ To make changes in data in database permanently. To create and delete database permanently. """
        try:
            
            with self.__engine.connect().execution_options(isolation_level="AUTOCOMMIT") as temp_conn:
                result = temp_conn.execute(text("SELECT DB_NAME() AS current_db"))
                for row in result:
                    print(f"Current Database is : {row[0]}")
                    print(30 * '-')

        except Exception as e:
            print(f"❌ Error : {e}")
        
        
        try:
            with self.__engine.connect().execution_options(isolation_level="AUTOCOMMIT") as temp_conn:
                temp_conn.execute(text(sql_script))
            print("✅ Changes made successfully")

        except Exception as e:
            print(f"❌ Error : {e}")
        
        self.close_connection()

    
    def ingesting_data(self,df,table_name,if_exists='replace'):
        '''Ingesting the dataset in Database, If already exists, it will be replaced'''
        try:
            start = time.time()
            df.to_sql(name=table_name,con = self.__engine, if_exists=if_exists,index=False)
            end = time.time()
            print(f'Time taken in ingesting "{table_name}" is {(end-start)/60} minutes')
            print(f'"{table_name}" is now ingested in "{self.database_name}" database')
            self.close_connection()

        except Exception as e:
            print(f"❌ Error : {e}")

    def read_sql_query(self,sql_script):
        df =  pd.read_sql_query(sql_script,self.__conn)
        return df


    
    def close_connection(self):
        """Close connection if open."""
        try:
            if self.__conn:
                self.__conn.close()
                print("🔒 Connection closed.")
            else:
                print("⚠️ No open connection to close.")
        except Exception as e:
            print(f"❌ Error: {e}")




        