from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(url):
    url_validator = URLValidator()
    if not url.startswith("http://") and not url.startswith("https://") : 
        url = "http://" + url
    print(url)
    try:
        url_validator(url)
    except:
        raise ValidationError("Invalid URL")    
    return url

def validate_dot_com(url):
    if '.com' not in url:
        raise ValidationError("The domain is not a dot com")
    return url
    