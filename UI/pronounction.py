from difflib import SequenceMatcher
import re

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

a = "나 전당포해. 금이빨은 받아. 금이빨 빼고 모조리 씹어 먹어줄게."
b = "나 전당포. 금이빨 받아. 금이빨 빼고 모리 씹어 먹어."
c = "우리보고 여를 지키라는 겁니까? 우리끼리만요?"

re_a = re.sub('[-=.#/?:$} ]', '', a)
re_b = re.sub('[-=.#/?:$} ]', '', b)
re_c = re.sub('[-=.#/?:$} ]', '', c)

print(similar(re_a, re_b)*100 , '%')
print(similar(re_a, re_c)*100 , '%')
