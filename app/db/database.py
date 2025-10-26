import mysql.connector
from mysql.connector import Error
from app.core.config import settings
from app.core.logger import logger

class DatabaseManager:
    def __init__(self):
        self.host = settings.DB_HOST
        self.user = settings.DB_USER
        self.password = settings.DB_PASSWORD
        self.database = settings.DB_NAME
    
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            logger.info("Database connection established")
            return connection
        except Error as e:
            logger.error(f"Database connection failed: {e}")
            return None
    
    def create_database_and_table(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = connection.cursor()
            
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            cursor.execute(f"USE {self.database}")
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    category VARCHAR(100) NOT NULL,
                    amount DECIMAL(10,2) NOT NULL,
                    description TEXT,
                    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            connection.commit()
            logger.info("Database and table created successfully")
            
        except Error as e:
            logger.error(f"Database setup failed: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

db_manager = DatabaseManager()