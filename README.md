# Find-My-IP
This module helps you to find out your both internal(local) and external IP also you can figure out your internet connection status.
Import **Find-Your-IP** in your script and use it easily.

Installing
----------
Download this module directly on github or install it with ```pip``` installation.
```shell
pip install FindMyIP
```

How to use
----------
```python3
import FindMyIP as ip
```

* Internet connection status:
  ```python3
  >>> ip.internet()
  
  True    # If the internet is connected.
  False   # If the internet is disconnected.
  ```
  
* Local IP:
  ```python3
  >>> local_ip = ip.internal()
  >>> print(local_ip)
  
  192.168.1.102
  ```
  
* External IP:
  ```python3
  >>> real_ip = ip.external()
  >>> print(real_ip)
  
  82.212.251.142
  ```
  
  # Change Log:
* [v 1.0.0:]()
  * Released
