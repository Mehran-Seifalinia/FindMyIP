from socket import socket, AF_INET, SOCK_DGRAM
from urllib.request import urlopen

def internet():
    url = "https://www.google.com/"
    try:
        urlopen(url)
        return True
    except:
        return False

def internal():
    try:
        connection = socket(AF_INET, SOCK_DGRAM)
        connection.connect(("8.8.8.8", 80))
        local_ip_address = connection.getsockname()[0]
        connection.close()
        return local_ip_address
    except Exception as e:
        print(e)
        exit()

def external():
    try:
        if internet():
            external_ip_address = urlopen("https://api.ipify.org/").read().decode("UTF-8")
            return external_ip_address
        else:
            print("You are not connected to the internet!\nPlase check your connection.")
            return None
    except Exception as e:
        print(e)
        exit()
