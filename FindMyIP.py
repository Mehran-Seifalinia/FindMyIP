from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, setdefaulttimeout, error
from urllib.request import urlopen

class FindMyIP:
    def __init__(self):
        self.timeout = 5
        self.google_dns = "8.8.8.8"
        self.api_url = "https://api.ipify.org/"
        self.decode_type = "UTF-8"

    def internet(self):
        """Check if internet connection is available by attempting to connect to www.google.com on port 80."""
        host = "www.google.com"
        port = 80

        try:
            setdefaulttimeout(self.timeout)
            socket(AF_INET, SOCK_STREAM).connect((host, port))
            return True
        except error:
            return False

    def internal(self):
        """Get the local IP address by connecting to Google's public DNS server (8.8.8.8) on port 80."""
        try:
            connection = socket(AF_INET, SOCK_DGRAM)
            connection.connect((self.google_dns, 80))
            local_ip_address = connection.getsockname()[0]
            return local_ip_address
        except Exception as e:
            print(f"Error getting internal IP: {e}")
            return None
        finally:
            connection.close()

    def external(self):
        """Get the external (public) IP address by fetching it from the ipify.org API."""
        if not self.internet():
            print("You are not connected to the internet!\nPlease check your connection.")
            return None

        try:
            response = urlopen(self.api_url)
            external_ip_address = response.read().decode(self.decode_type)
            response.close()
            return external_ip_address
        except Exception as e:
            print(f"Error getting external IP: {e}")
            return None
