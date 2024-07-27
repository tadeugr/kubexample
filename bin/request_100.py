import requests
url = "http://localhost:8080/payload"

for i in range(100):
    print("----------------------------")
    print(f"Interation: {i}")
    response = requests.get(url)
    print(response.content)