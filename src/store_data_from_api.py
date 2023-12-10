"""
ETL pipeline to store data from the API to Azure Blob Storage.
"""

import os
from dotenv import load_dotenv
from scripts.extractor import Extractor

load_dotenv()

storage_account_name = os.getenv("STORAGE_ACCOUNT_NAME")
storage_account_key = os.getenv("STORAGE_ACCOUNT_KEY")
storage_bucket = "raw/moviesproject"
rapidapi_key = os.getenv("AUTH_RAPIDAPI_KEY")

extractor = Extractor(
        storage_account_name=storage_account_name,
        storage_account_key=storage_account_key,
        storage_bucket=storage_bucket,
        rapidapi_key=rapidapi_key
    )

if __name__ == "__main__":
    extractor.get_data_on_pages(endpoint="titles")
