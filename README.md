# url_check
Python script for checking url status using the status code. It will not only notify the problem but will also suggest possible solutions, thus saving troubleshooting time. 

Usage: 

url_check.py -u[--url] url1, url2


It will notify with possible problems in the below cases:

1. If the ip given in the url is not reachable.
2. If the port is not listening in the IP, thus connection is refused. 
3. If there is a problem in the dns resolution


Example Usage: 

url_check.py -u https://google.com,https://facebook.com
