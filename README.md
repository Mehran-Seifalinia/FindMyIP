# Find My IP
Find My IP is a user-friendly Python package that helps you find both your internal (local) and external IP addresses. It also lets you check your internet connection status effortlessly. By importing FindMyIP into your script, you can easily retrieve your IP addresses and quickly determine if your internet is connected. It's a simple and convenient tool for developers to use in their projects.

## Installing
To get started with Find My IP, you have two options for installation:

1. **Download from GitHub:** You can download the module directly from the GitHub repository.

2. **Install with `pip`:** Alternatively, you can use `pip` to install the package effortlessly. Open your terminal or command prompt and run the following command:

```shell
pip install FindMyIP
```

With just a simple installation step, you'll be ready to utilize Find My IP in your Python projects!

## How to use

Using Find My IP is straightforward. Here's a step-by-step guide to help you get started:

* **Import the module:**
   ```python3
   import FindMyIP as ip
   ```

* **Check Internet Connection Status:**
   To determine if your internet is connected or disconnected, use the `internet()` function:
   ```python3
   >>> ip.internet()
   True    # If the internet is connected.
   False   # If the internet is disconnected.
   ```

* **Retrieve Local IP Address:**
   To find your local (internal) IP address, use the `internal()` function:
   ```python3
   >>> local_ip = ip.internal()
   >>> print(local_ip)
   192.168.1.102
   ```

* **Retrieve External IP Address:**
   To get your external IP address, use the `external()` function:
   ```python3
   >>> real_ip = ip.external()
   >>> print(real_ip)
   82.212.251.142
   None  # When you are not connected to the internet
   ```

With these simple steps, you can easily find your IP addresses and check your internet connection status using the Find My IP package in your Python projects. Happy coding!
  
## Change Log:
We're continuously improving Find My IP to ensure the best experience. Here's a summary of the recent updates:

* **[v 1.1.0:](https://github.com/Mehran-Seifalinia/FindMyIP/commit/b47caa25bc8951f7223ceed6aca5df5ca4d899a6)**
  - Initial Release

* **[v 1.2.0:](https://github.com/Mehran-Seifalinia/FindMyIP/commit/64ce86dbe41d68aadd7b46167244fd7efff805fc)**
  - Minor bug fixed
    - Addressed a false positive issue in the `internet` function.
  - Improved code documentation
    - Added more comments to enhance code readability and understanding.

* **[v 2.0.0:](https://github.com/Mehran-Seifalinia/FindMyIP/commit/bf3566985587f2a4190091ef8826e431128a425a)**
  - Recoding as a class
  - Improve error handling
  - Get errors as log

Stay tuned for more updates as we continue to enhance Find My IP to meet your needs!
