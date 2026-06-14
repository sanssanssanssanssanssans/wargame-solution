# 풀이

- 코드에서 `document[_0x374fd6(0x183)](_0x374fd6(0x182))['value']`는 `document.getElementById("flag").value`와 동치고, $|flag| \neq 36$면 실패이다. 

```js
operator = [
 (a,b)=>a+b,
 (a,b)=>a-b,
 (a,b)=>a*b,
 (a,b)=>a^b
];
```

이 operator의 연산은 +, -, *, ^, + - .....를 반복합니다. 즉, `flag.charCodeAt(i) == operator[i%4](_0x4949[i], _0x42931[i])` 입니다. 다음 코드를 C++로 짜서 풀 수 있습니다.

```