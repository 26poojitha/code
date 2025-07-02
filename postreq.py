import requests
url = "http://jsonplaceholder.typicode.com/posts"
data={
    "title": "Hi Students",
    "body": "Wipro geeks",
    "userid":1
}
response = requests.post(url,json=data)
print(response.status_code)
print(response.json())