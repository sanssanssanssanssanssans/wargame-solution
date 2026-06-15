import requests

r = requests.put(
    "http://host3.dreamhack.games:21667/api/board",
    json={
        "title": "test",
        "author": "guest",
        "body": "hello",
        "secret": False
    }
)

print(r.text)