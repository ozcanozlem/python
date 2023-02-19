import requests
url = 'https://httpbin.org/post'
data={'title': 'RoboCop', 'description': 'The best movie ever.'}
r = requests.post(url, data=data).json()
print(r)