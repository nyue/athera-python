"""
Helpers for the Athera API
"""
import os

def headers(group_id, token):
    """
    Generate the headers expected by the Athera API. All queries require the active group, as well as authentication.
    """
    return { 
        "active-group": group_id,
        "Authorization" : "Bearer: {}".format(token) 
    }


def api_debug(func):
    if os.getenv("ATHERA_API_DEBUG"):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            #print(response.request.url)
            #print(response.request.headers)
            #print(response.request.body)
            print("{} {} [{}]".format(response.request.method, response.url, response.status_code))
            return response
        return wrapper
    else:
        return func
    