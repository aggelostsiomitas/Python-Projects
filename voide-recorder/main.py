import wavio as wv
from scipy.io.wavfile import write 
import sounddevice as sd

#declare the frequency sample of my recording 
freq=45000

#declare the seconds the recording will last  
duration=5

#start recording using the sounddevice library 
recording=sd.rec(
        int(duration*freq),
        samplerate=freq,
        channels=2)

sd.wait() #wait until the recording is finished

#save results with both scipy and wavio library
write("recording0.wav", freq, recording)


wv.write("recording1.wav", recording, freq, sampwidth=2)
