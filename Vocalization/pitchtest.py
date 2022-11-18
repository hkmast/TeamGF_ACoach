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

def get_pitch_info(dir_path) :
    file_list = os.listdir(dir_path)

    mean_array = []
    std_array = []
    slope_array = []

    for file_num, soundpath in enumerate(file_list, 1):
        Sound = parselmouth.Sound(dir_path + soundpath)
        Sound = parselmouth.praat.call(Sound, "Convert to mono") 

        voice_pitch = Sound.to_pitch().interpolate()
        voice_pitch_array = voice_pitch.selected_array['frequency']

        mean = int(round(np.nanmean(voice_pitch_array)))
        std = int(round(np.nanstd(voice_pitch_array)))
        slope = int(round(voice_pitch.get_mean_absolute_slope()))

        mean_array.append(mean)
        std_array.append(std)
        slope_array.append(slope)
        
        #print(soundpath + '|    slope : ' + str(slope) + ',    mean : ' + str(mean) + ',   std : ' + str(std))

    man_mean = int(round(np.mean(mean_array)))
    man_std = int(round(np.mean(std_array)))
    man_slope = int(round(np.mean(slope_array)))

    print('mean : ' + str(man_mean) + '     std : ' + str(man_std) + '      slope : ' + str(man_slope))

print('Man')
get_pitch_info('C:/Users/KimTaeGyuPC/Desktop/test_data2/man/')
print('')
print('Woman')
get_pitch_info('C:/Users/KimTaeGyuPC/Desktop/test_data2/woman/')