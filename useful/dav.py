import json

def put_json(client, path, obj):
    return client.put(
        path,
        data=json.dumps(obj),
        headers={"Content-Type": "application/json"}
    )

def move(client, src, dst):
    return client.request(
        "MOVE",
        src,
        headers={"Destination": dst}
    )