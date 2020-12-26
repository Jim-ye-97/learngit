import requests
from requests.auth import HTTPBasicAuth

r=requests.get('http://pythonscraping.com/pages/auth/login.php',auth=HTTPBasicAuth('Jim.ye','123456'))
print(r.status_code)