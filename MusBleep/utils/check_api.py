import requests

from .read_conf import conf

def check_api() -> bool:
    """
        Checks wither the API is up or not
    """
    API = conf()["api"]

    try:
        requests.get(f"{API}/api/v1")
        return True
    except requests.exceptions.ConnectionError:
        return False
