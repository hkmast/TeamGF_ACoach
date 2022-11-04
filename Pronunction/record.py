# 이 파이썬 코드를 실행하면 마이크를 통해 녹음한 음성을 PCM 형식의 음성파일로 바꿔서 저장합니다.
# sounddevice 모듈을 먼저 설치 하자!
# sounddevice 설치 방법 -> pip install sounddevice 으로 설치!

import sounddevice as sd

duration = 10 # seconds 녹음 시간 (초)
fs = 16000 # sampling frequency 샘플링 주파수

# default channel 은 2로, stereo 타입이니 변경 필요!
print('start')
rec = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='int16')
sd.wait()
pcm = rec.tostring()

# ETRI 에서 답변받은 것처럼 PCM 으로 된 RAW 파일을 저장!
with open('sampleAudio.raw', 'wb') as w: 
    w.write(pcm)