from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, setdefaulttimeout, error
from urllib.request import urlopen

# Check if internet connection is available by attempting to connect to www.google.com on port 80.
def internet():
    host = "www.google.com"
    port = 80
    timeout = 5  # 5 seconds

    try:
        setdefaulttimeout(timeout)
        socket(AF_INET, SOCK_STREAM).connect((host, port))
        return True
    except error:
        return False

# Get the local IP address by connecting to Google's public DNS server (8.8.8.8) on port 80.
def internal():
    google_dns = "8.8.8.8"
    port = 80

    try:
        connection = socket(AF_INET, SOCK_DGRAM)
        connection.connect((google_dns, port))
        local_ip_address = connection.getsockname()[0]
        return local_ip_address
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()

# Get the external (public) IP address by fetching it from the ipify.org API.
def external():
    api_url = "https://api.ipify.org/"
    decode_type = "UTF-8"

    try:
        if internet():
            response = urlopen(api_url)
            external_ip_address = response.read().decode(decode_type)
            response.close()
            return external_ip_address
        else:
            print("You are not connected to the internet!\nPlase check your connection.")
            return None
    except Exception as e:
        print(e)
        exit()
