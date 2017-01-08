"""
    Utility Methods for Validation of POST of URL from Form
"""

def validate_url(url):
    print("URL IS: {0}".format(url))
    if "http://" not in url and "https://" not in url:
            print("HTTP not in URL")
            error = "Please add http:// to start of url"
            return error
    elif "academia.edu" not in url:
        print("Not an academia.edu URL")
        error = "Please input an Academia.edu url"
        return error
    else:
        return None
