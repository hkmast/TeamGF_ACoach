#-*- coding:utf-8 -*-
# 미리 설치해야 하는 모듈이다. 바로 아래 명령문 3개를 사용해서 설치해주자.
# pip install urllib3
# pip install jsonlib
# pip install pybase64

import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/PronunciationKor"
accessKey = "2ed3f29a-3581-4201-bc56-2c5dea7e4c42" #필수
audioFilePath = "C:/Users/KimTaeGyuPC/Desktop/test_data/짧은문장.raw" #필수 (예시 : audio/test.raw)
languageCode = "korean" #필수, 어차피 english 밖에 없다.
#script = "지난 7월 북한 선박으로 추정되는 목선을 발견하고도 별도의 대공 혐의 조사 없이 부수라고 지시한 혐의를 받는 해병대 2사단 소속 중대장. 지난 주 직무 유기 혐의로 군 경찰에 입건되었습니다."
script = "지난 7월 북한 선박으로 추정되는 목선을 발견하고도 별도의 대공 혐의 조사 없이 부수라고 지시한 혐의를 받는 해병대 2사단 소속 중대장."
#script = "안녕하세요. 김태규입니다."
#필수가 아니지만 발음 평가할 때 기준이 되는 문장을 의미한다.
 
file = open(audioFilePath, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "language_code": languageCode,
        "script": script, #필수가 아니기에 지워줘도 사용 가능하다.
        "audio": audioContents
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))