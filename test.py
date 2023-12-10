import requests
from requests import get


r = requests.get('https://google.com')

a = 10

print(a)


class MyClass:
    def __init__(self, var) -> None:
        self.data = var
        
        
print(MyClass(10).data)