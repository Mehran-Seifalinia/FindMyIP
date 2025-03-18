from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, setdefaulttimeout, error
from urllib.request import urlopen

class FindMyIP:
    def __init__(self, timeout=5, google_dns="8.8.8.8", api_url="https://api.ipify.org/", decode_type="UTF-8"):
        self.timeout = timeout
        self.google_dns = google_dns
        self.api_url = api_url
        self.decode_type = decode_type

    def internet(self):
        """
        Check if an internet connection is available by attempting to connect to www.google.com on port 80.
        
        This method creates a socket and attempts to connect to Google's DNS server on port 80. If the connection
        is successful, it returns True, indicating that the system has internet access. If there is any issue (like
        timeout or unreachable server), it returns False.

        Raises:
            socket.timeout: If the connection times out based on the defined timeout value.
            socket.error: If there is a general connection error.
        """
        host = "www.google.com"
        port = 80

        try:
            # Use a context manager to ensure the socket is properly closed after use
            with socket(AF_INET, SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                s.connect((host, port))
            return True
        except timeout:
            print("Connection timed out.")
            return False
        except error as e:
            print(f"Socket error occurred: {e}")
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
