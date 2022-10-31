import warnings
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
import librosa
import librosa.display
import glob
import parselmouth
import pandas as pd
import os
import csv

warnings.filterwarnings(action="ignore")

def find_formant(file_path):

    file_list = os.listdir(file_path)  # path에 있는 데이터들을 file_list에 삽입

    data = pd.DataFrame({
        "times": [],
        "pitch(tone)": [],
        "F1": [],
        "F2": [],
        'F3': [],
        "F4": [],
        "F5": [],
        "filename": []
    })
    formants_value = ['F1', 'F2', "F3", "F4", "F5"]

    for file_num, soundpath in enumerate(file_list, 1):
        try:
            Sound = parselmouth.Sound(file_path + soundpath)  # 샘플의 위치를 Sound 객체로 변환

            voice_pitch = Sound.to_pitch()

            formant = Sound.to_formant_burg(time_step=0.1)  # time_step초 당 포먼트 변환

            df = pd.DataFrame({"times": formant.ts()})  # formant에서 추출 시간을 표시한다.

            for idx, col in enumerate(formants_value, 1):  # 시간대별 포먼트 추출
                df[col] = df['times'].map(lambda x: formant.get_value_at_time(formant_number=idx, time=x))

            df['pitch'] = df['times'].map(lambda x: voice_pitch.get_value_at_time(time=x))  # 음성 피치 저장

            # 데이터 저장

            df['filename'] = soundpath

            data = data.append(df)

            print(soundpath + ' 포먼트 검출 완료')

        except Exception as e:
            print(e)
            print(soundpath + ' 포먼트 검출 완료')

    data.to_csv("voice_formant.csv")

    return 0


def find_pitchnf3to5_range(file_path):
    csv_file = open(file_path, "r", encoding="utf-8", newline="")
    rdr = csv.reader(csv_file)

    pitch_data = pd.DataFrame({"F3": [], "F4": [], "F5": [], "filename": []})

    tmp = ""

    for line in rdr:

        name = line[8]
        pitch = line[2]
        F3 = line[5]
        F4 = line[6]
        F5 = line[7]

        tmp_data = {}

        if name == "filename":
            continue

        if tmp == "":
            tmp = name
            print("nextfile: " + tmp)
            tmp_data["filename"] = tmp

        if tmp != name:
            tmp = name
            tmp_data["filename"] = tmp
            print("nextfile: " + tmp)

        tmp_data["filename"] = tmp

        if pitch != "":
            if F3 != "":
                tmp_data["F3"] = (
                                         min(
                                             (float(F3) % float(pitch)),
                                             abs((float(F3) % float(pitch)) - float(pitch)),
                                         )
                                         / float(pitch)
                                 ) * 100
            if F4 != "":
                tmp_data["F4"] = (
                                         min(
                                             (float(F4) % float(pitch)),
                                             abs((float(F4) % float(pitch)) - float(pitch)),
                                         )
                                         / float(pitch)
                                 ) * 100
            if F5 != "":
                tmp_data["F5"] = (
                                         min(
                                             (float(F5) % float(pitch)),
                                             abs((float(F5) % float(pitch)) - float(pitch)),
                                         )
                                         / float(pitch)
                                 ) * 100

            df = pd.DataFrame(tmp_data, index=[0])
            pitch_data = pitch_data.append(df)

    pitch_data.to_csv("pitch_formant_range.csv")

    csv_file.close()

    return 0


if __name__ == "__main__":

    if find_formant('test_sample/') != 0:
        print("find_formant 오류")

    if find_pitchnf3to5_range('voice_formant.csv') != 0:
        print("find_pitchnf3to5_range 오류")

