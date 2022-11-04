import requests
import json
import re


class ClovaSpeechClient:
    # Clova Speech invoke URL
    invoke_url = ""
    # Clova Speech secret key
    secret = ""

    def req_upload(
        self,
        file,
        completion,
        callback=None,
        userdata=None,
        forbiddens=None,
        boostings=None,
        wordAlignment=True,
        fullText=True,
        diarization=None,
    ):
        request_body = {
            "language": "ko-KR",
            "completion": completion,
            "callback": callback,
            "userdata": userdata,
            "wordAlignment": wordAlignment,
            "fullText": fullText,
            "forbiddens": forbiddens,
            "boostings": boostings,
            "diarization": diarization,
        }
        headers = {
            "Accept": "application/json;UTF-8",
            "X-CLOVASPEECH-API-KEY": self.secret,
        }
        # print(json.dumps(request_body, ensure_ascii=False).encode('UTF-8'))
        files = {
            "media": open(file, "rb"),
            "params": (
                None,
                json.dumps(request_body, ensure_ascii=False).encode("UTF-8"),
                "application/json",
            ),
        }
        response = requests.post(
            headers=headers, url=self.invoke_url + "/recognizer/upload", files=files
        )
        return response


def voiceSTT(filepath):

    res = ClovaSpeechClient().req_upload(file=filepath, completion="sync")
    data = res.json()

    segments = data.get("segments")
    fulltext = data.get("text")
    start = segments[0].get("start")
    end = segments[len(segments) - 1].get("end")

    char_cnt = 0  # 전체 글자의 갯수
    word_time = 0  # 띄어쓰기를 제외한 단어별 시간들의 총합
    word_cnt = 0  # (띄어쓰기로 구분 된)단어의 갯수
    time = end - start

    print(filepath + " / fulltext : " + fulltext)
    # 단어별 말의 빠르기
    for segment in segments:
        for seg_list in segment["words"]:
            char_cnt = char_cnt + len(seg_list[2])
            word_time = word_time + seg_list[1] - seg_list[0]
            word_cnt = word_cnt + 1

    char_cnt_in_blank = char_cnt + word_cnt  # 띄어쓰기도 한 글자로 포함한 전체 글자의 갯수

    all_avg_time_in_blank = time / char_cnt  # 띄어쓰기 포함 글자당 걸리는 시간
    all_avg_time_in_blank_char = time / char_cnt_in_blank  # 띄어쓰기를 한 글자로 따진 글자당 걸리는 시간
    all_avg_time_no_blank = word_time / char_cnt  # 띄어쓰기 제외한 글자당 걸리는 시간
    word_avg_time = word_time / word_cnt  # (띄어쓰기로 구분 된) 단어별 걸리는 시간
    word_avg_cnt = char_cnt / word_cnt  # (띄어쓰기로 구분 된) 단어별 평균 갯수

    result_list = [
        all_avg_time_in_blank,
        all_avg_time_in_blank_char,
        all_avg_time_no_blank,
        word_avg_time,
        word_avg_cnt,
    ]

    return result_list


malist = []
walist = []
mnlist = []

for i in range(1, 6):
    filepath = "test/m" + str(i) + "a.wav"
    malist.append(voiceSTT(filepath))

for i in range(1, 6):
    filepath = "test/w" + str(i) + "a.wav"
    walist.append(voiceSTT(filepath))

for i in range(1, 4):
    filepath = "test/m" + str(i) + "n.wav"
    mnlist.append(voiceSTT(filepath))

print("남자 아나운서\n전체평균, 띄(글자)평균, 공백제외평균 , 단어별평균시간, 단어평균갯수")
for row in malist:
    print(row)

print("여자 아나운서\n단어평균, 글자갯수, 글자별 평균시간, 전체평균시간")
for row in walist:
    print(row)

print("일반인\n단어평균, 글자갯수, 글자별 평균시간, 전체평균시간")
for row in mnlist:
    print(row)
