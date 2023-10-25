import time
import json
import requests

"""
Approach 1
Load the sentences from a json file, so that we won't need to make changes in the code
We can just edit the json file and read it and make inference
"""
input_file = "test.json"
with open(input_file) as f:
    data = json.load(f)


"""
Approach 2
Pass the sentences as a dictionary from the code itself.
Make changes in the code.
"""
# data = {
#     "text1": "This is a test sentence",
#     "text2": "This is also a test sentence"
# }


# Cloud Run request url
# request_url = "https://sample_url_link"

# Local test
# response = requests.post("http://127.0.0.1:8080/similarity", json=data)

# Cloud run test
response = requests.post(f"{request_url}/similarity", json=data)


print(response.json())