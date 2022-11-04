import wave

with open("C:/Users/KimTaeGyuPC/Desktop/test_data/woman1_태규.raw", "rb") as inp_f:
    data = inp_f.read()
    with wave.open("woman1_태규.wav", "wb") as out_f:
        out_f.setnchannels(1)
        out_f.setsampwidth(2) # number of bytes
        out_f.setframerate(16000)
        out_f.writeframesraw(data)


#with wave.open("C:/Users/KimTaeGyuPC/OneDrive/바탕 화면/test_data/woman1_태규.wav", "rb") as in_f:
#    print(repr(in_f.getparams()))