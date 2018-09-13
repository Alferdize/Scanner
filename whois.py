import pythonwhois
from pprint import pprint
import pprint

def get_whois(url):
    details = pythonwhois.get_whois(url)
    return (pprint.pformat(details))

