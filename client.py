import requests


HOST = "http://127.0.0.1:8000/api/v1"


def get_collections():
    headers = {
        "Accept-Language": "uz",
    }

    data = requests.get(f"{HOST}/collections/", headers=headers)
    print(data.json())


get_collections()
