import pymongo
#from us_visa.configuration.mango_db_configuration import MongoDBClient 
from us_visa.data_access.us_visa_data import USvisaData
from us_visa.constants import COLLECTION_NAME
from us_visa.logger import logging

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of USvisaData
        us_visa_data = USvisaData()

        # Call the method and pass the required arguments
        dataframe = us_visa_data.export_collection_as_dataframe(collection_name=COLLECTION_NAME)

        # Print the DataFrame or perform further operations
        print(dataframe)
    except Exception as e:
        logging.error(f"Error occurred: {e}")