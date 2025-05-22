# GraphQL Request Parser
- GraphQL QURL 요청을 파싱하여 응답 Key값을 추출하는 모듈입니다.
- 요청 raw 데이터는 아래와 같은 형식으로 input경로에 txt파일로 저장되어 있어야 합니다.
```text
curl 'https://url/graphql' \
-H 'Accept: */*' \
-H 'Accept-Language: ko,en;q=0.9,en-US;q=0.8' \
-H 'Authorization: Bearer .... \
-H 'Connection: keep-alive' \
-H 'Content-Type: application/json' \
-H 'Origin: https://oncoflow.oncosoft.io' \
-H 'Referer: https://oncoflow.oncosoft.io/dashboard' \
-H 'Sec-Fetch-Dest: empty' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: same-origin' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0' \
-H 'sec-ch-ua: "Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"' \
-H 'sec-ch-ua-mobile: ?0' \
-H 'sec-ch-ua-platform: "macOS"' \
--data-raw $'{"query":"\\n            query Data($input: DataInput\u0021) {\\n                datas(input: $input) {\\n                    id\\n                    child\\n         ...}'
```
- 파싱된 데이터는 다음과 같은 형시으로 output 경로에 txt파일로 저장됩니다.
```text
data
data.id
data.child
data.child.id
data.createdAt
...
```

## 실행
- Python 3.11 이상
- `python main.py` 명령어로 실행합니다.
- 근데 활용도가 없을듯...
