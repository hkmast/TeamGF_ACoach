import requests
import json

class ClovaSpeechClient:
    # Clova Speech invoke URL
    invoke_url = 'https://clovaspeech-gw.ncloud.com/external/v1/3973/a2280ba182f84d8331ca0cad1b66910bfcb17f1f8a482f711ece02b795c3712b'
    # Clova Speech secret key
    secret = 'de087cbc6e9d440bbe6dae6f3ebc74da'

    def req_upload(self, file, completion, callback=None, userdata=None, forbiddens=None, boostings=None,
                   wordAlignment=True, fullText=True, diarization=None):
        request_body = {
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        print(json.dumps(request_body, ensure_ascii=False).encode('UTF-8'))
        files = {
            'media': open(file, 'rb'),
            'params': (None, json.dumps(request_body, ensure_ascii=False).encode('UTF-8'), 'application/json')
        }
        response = requests.post(headers=headers, url=self.invoke_url + '/recognizer/upload', files=files)
        return response

if __name__ == '__main__':
    res = ClovaSpeechClient().req_upload(file='C:/Users/KimTaeGyuPC/Desktop/test_data/woman1_태규.wav', completion='sync')
    data = res.json()
    segments = data.get("segments")
    fulltext = data.get("text")
    for segment in segments : 
        for words in segment["words"] : 
            print(words)
    print('fulltext : \n' + fulltext + '\n')