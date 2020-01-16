import json


def print_api_status(a_status_code):

    if a_status_code == 200:
        print("Everything's OK")
        return True
    elif a_status_code == 301:
        print("The API has redirected you to a new endpoint")
        return True
    elif a_status_code == 400:
        print("Bad request")
        return False
    elif a_status_code == 401:
        print("Server thinks you're not authenticated")
        return False
    elif a_status_code == 403:
        print("The resource is forbidden")
        return False
    elif a_status_code == 404:
        print("Resource not found")
        return False
    elif a_status_code == 503:
        print("The server is not ready to handle your request")
        return False
    else:
        print("Unknown response")
        return True


def json_print(json_object):

    text = json.dumps(json_object, sort_keys=True, indent=4)
    print(text)
    return text
