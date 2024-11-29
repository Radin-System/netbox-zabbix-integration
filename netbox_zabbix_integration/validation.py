from urllib.parse import urlparse

def validate_url(url) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme in ["http", "https"], result.netloc])
    except ValueError:
        return False

def validate_authentication(token, username, password) -> bool:
    return (token is not None) or (username is not None and password is not None)

def validate_bool(obj) -> bool:
    return isinstance(obj, bool)