import pythonwhois
from pprint import pprint
import pprint

def get_whois(url):
    details = pythonwhois.get_whois('google.com')
    return (pprint.pformat(details))

