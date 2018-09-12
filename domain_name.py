from tld import get_tld 
import tldextract

def get_domain_name(url):
    spltAr = url.split("://www.");
    i = (0,1)[len(spltAr)>1];
    dm = spltAr[i].split("?")[0].split('/')[0].split(':')[0].lower();
    return dm

