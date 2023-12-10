"""
Extractor module for the ETL pipeline.
"""

from datetime import datetime
import requests
from pytz import timezone
from .utils import initialize_azure_blob_storage, upload_file_to_azure

class Extractor:
    """
    Extractor class for the ETL pipeline.

    Args:
        storage_account_name (str): Your Azure Storage account name.
        storage_account_key (str): Your Azure Storage account key.
        storage_bucket (str): The Azure Storage container where you want to store the files.
        rapidapi_key (str): Your RapidAPI key.

    Returns:
        Extractor: An Extractor instance.
    """
    def __init__(
        self,
        storage_account_name,
        storage_account_key,
        storage_bucket,
        rapidapi_key
    ):
        self.storage_account_name = storage_account_name
        self.storage_account_key = storage_account_key
        self.storage_bucket = storage_bucket
        self.rapidapi_key = rapidapi_key

    def get_raw_json_data(self, endpoint: str):
        """
        Get the raw JSON data from the API.

        Args:
            endpoint (str): The endpoint to be called.

        Returns:
            dict: The raw JSON data.
        """
        url = "https://moviesdatabase.p.rapidapi.com" + endpoint
        headers = {
            "X-RapidAPI-Key": f"{self.rapidapi_key}",
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, timeout=25)

        return response.json()

    def get_data_on_pages(self, endpoint: str):
        """
        Get the data from the API on paginated endpoints.

        Args:
            endpoint (str): The endpoint to be called.
        """
        paginated_endpoint = f"/{endpoint}?page=1"

        while True:
            data = self.get_raw_json_data(paginated_endpoint)

            current_datetime = datetime.now(timezone("Brazil/East")).strftime('%Y%m%d_%H%M%S')
            object_path = f"{endpoint}/{current_datetime}.json"

            #call initialize_azure_blob_storage function
            client = initialize_azure_blob_storage(self.storage_account_name,
                                                   self.storage_account_key)

            #call upload_file_to_azure function passing client
            if upload_file_to_azure(client, data, object_path, self.storage_bucket):
                print(f"File '{object_path}' uploaded to storage successfully.")
            else:
                print(f"Failed to upload '{object_path}' to storage.")

            next_page = data.get("next")

            if next_page == f"{endpoint}?page=1":
                break

            paginated_endpoint = next_page
