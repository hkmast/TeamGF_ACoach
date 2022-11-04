# Imports
from scipy.io import wavfile
import scipy.signal as sps
import numpy as np

# Your new sampling rate
new_rate = 16000

path = "C:/Users/KimTaeGyuPC/OneDrive/바탕 화면/test_data/woman1-1.wav"

# Read file
sampling_rate, data = wavfile.read(path)

# Resample data
number_of_samples = round(len(data) * float(new_rate) / sampling_rate)
data = sps.resample(data, number_of_samples)
wavfile.write("test2.pcm", new_rate, data.astype(np.int16))