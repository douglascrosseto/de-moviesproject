"""
Utility functions for the scripts.
"""

import json
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import AzureError

def initialize_azure_blob_storage(account_name, account_key):
    """
    Initialize an Azure Blob Storage client.

    Args:
        account_name (str): Your Azure Storage account name.
        account_key (str): Your Azure Storage account key.

    Returns:
        BlobServiceClient: An Azure Blob Storage client instance.
    """
    try:
        # Initialize an Azure Blob Storage client
        connection_string = f"""DefaultEndpointsProtocol=https;
                                AccountName={account_name};
                                AccountKey={account_key};
                                EndpointSuffix=core.windows.net
                            """
        client = BlobServiceClient.from_connection_string(connection_string)
        return client
    except AzureError as e:
        print(f"Azure Blob Storage initialization error: {e}")
        return None

def upload_file_to_azure(client, data, filename, container_name):
    """
    Upload a file to Azure Blob Storage.

    Args:
        client (BlobServiceClient): The Azure Blob Storage client instance.
        data (dict): The data to be saved.
        filename (str): The name of the file to be created in Azure Blob Storage.
        container_name (str): The Azure Blob Storage container where you want to store the file.

    Returns:
        bool: True if the upload is successful, False otherwise.
    """
    try:
        # Convert the data dictionary to a JSON string
        data_as_json = json.dumps(data)

        # Convert the JSON string to bytes
        data_as_bytes = data_as_json.encode('utf-8')

        # Get a BlobClient for the file
        blob_client = client.get_blob_client(container=container_name, blob=filename)

        # Upload the bytes to Azure Blob Storage
        blob_client.upload_blob(data_as_bytes, overwrite=True)
        return True

    except AzureError as e:
        print(f"Azure Blob Storage error: {e}")
        return False
