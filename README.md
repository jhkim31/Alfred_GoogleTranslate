# 1. Google-Translate
실시간 구글 번역 워크플로우

GCP translate-v2 를 사용한다. 해당 API를 사용하기 위해선 키를 발급받아야함.
[gcp-translate/v2](https://cloud.google.com/translate/docs/reference/rpc/google.cloud.translate.v2)

## Usage
소스코드의 {your-api-key} 에 발급받은 gcp API키를 삽입해 사용한다.


## 1.1 영어 => 한글 번역 [en2ko]
![image](/image/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-30%2015.10.42.png)
## 1.2 한글 => 영어 번역 [ko2en]
![image](/image/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-30%2015.10.25.png)


# 2. Timestamp
timestamp <=> human date 변환 워크플로우

KST, GST 기준으로 동작한다.

## 2.1 현재시간 출력[now] 
![image](/image/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-30%2015.12.08.png)

## 2.2 timestamp => human date [timestamp]
타임스탬프 => human date 변환 (s, ms 단위 사용 가능)
![image](/image/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-30%2015.13.28.png)
![image](/image/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-30%2015.13.53.png)

## 2.3 human date => timestamp [YYYYmmdd, YYYYmmddHHMMSS]
human date => timestamp 변환 [YYYYmmdd포맷, YYYYmmddHHMMSS] 포맷 사용 가능
![image](/image/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-30%2015.14.36.png)
![image](/image/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-30%2015.15.07.png)
