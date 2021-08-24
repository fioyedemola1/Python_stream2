import requests
from typing  import Optional





url = 'https://catfact.ninja/fact'


def status_code(url: str)-> bool:
     resp= requests.get(url)
     if resp.status_code == 200:
         return True
     return False
 
print(status_code(url))

