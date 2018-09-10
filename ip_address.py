import socket

def get_ip_address(url):
    result = socket.gethostbyname(url)
    return result


print(get_ip_address('google.com'))


