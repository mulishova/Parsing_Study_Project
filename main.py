import requests
from fake_useragent import UserAgent  # import fake_useragent

url = 'http://httpbin.org/user-agent'

for i in range(10):
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)
