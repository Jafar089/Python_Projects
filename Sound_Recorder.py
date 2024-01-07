# Voice Recorder

#import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

#sampling frequency
freq = 44100
#Recording Duration
duration = 30

#Start Recoder With The Given Values of duration and sample frequency
print('Recording started. Please speak...')
recording = sd.rec(int(duration * freq), samplerate = freq, channels = 2)

#Recode audio for the given number of seconds
sd.wait()

#this will convert the Numpy array to an Audio
#File with The Given Sampling Frequency
write("recording0.wav", freq, recording)

#Convert the Numpy Array To Audio File
wv.write("recording1.way", recording, freq, sampwidth = 2)

if duration == 30:
    print("Your voice has been recorded!")