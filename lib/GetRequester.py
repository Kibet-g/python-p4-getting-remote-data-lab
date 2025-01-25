import requests
import json
from typing import Union, List, Dict, Any

class GetRequester:
    def __init__(self, url: str):
        """
        Initialize the GetRequester with a URL.
        :param url: The URL to send GET requests to.
        """
        self.url = url

    def get_response_body(self) -> Union[bytes, None]:
        """
        Sends a GET request to the initialized URL and returns the response body as bytes.
        Handles HTTP errors and other request exceptions.
        
        :return: The response body as bytes, or None if an error occurred.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises HTTPError for 4xx/5xx responses
            return response.content  # Return as bytes
        except requests.RequestException as e:
            print(f"An error occurred while making the request: {e}")
            return None

    def load_json(self) -> Union[List[Any], Dict[str, Any], None]:
        """
        Parses the response body as JSON and returns it as a Python object.
        Handles JSON decoding errors.

        :return: A Python object (list or dict) parsed from the JSON response, or None if parsing failed.
        """
        response_body = self.get_response_body()
        if response_body:
            try:
                return json.loads(response_body.decode('utf-8'))  # Decode bytes to string before parsing
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON: {e}")
                return None
        return None
