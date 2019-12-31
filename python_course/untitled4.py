# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:30:22 2019

@author: EGLOBAL
"""

from __future__ import print_function
import seaborn
import numpy, scipy, matplotlib.pyplot as plt, sklearn, pandas, librosa, urllib, IPython.display, os.path

plt.rcParams['figure.figsize'] = (14, 5)





# We'll need numpy for some mathematical operations
import numpy as np

# matplotlib for displaying the output
import matplotlib.pyplot as plt

# and IPython.display for audio output
import IPython.display

# Librosa for audio
# And the display module for visualization
import librosa.display
audio_path = librosa.util.example_audio_file()

# or uncomment the line below and point it at your favorite song:
#
# audio_path = '/path/to/your/favorite/song.mp3'

y, sr = librosa.load(audio_path)




>>> import matplotlib.pyplot as plt
>>> y, sr = librosa.load(librosa.util.example_audio_file(), duration=10)
>>> plt.figure()
>>> plt.subplot(3, 1, 1)
>>> librosa.display.waveplot(y, sr=sr)
>>> plt.title('Monophonic')





class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value






















