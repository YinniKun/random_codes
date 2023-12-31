## Create a FFT picture from a given sound file
## works by first taking the FFT of the sound file, then draw the image at each time step

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def main(file):
    # Read the sound file
    rate, data = wav.read(file)
    # Take the FFT
    out = np.fft.fft(data,axis=0)
    yf = np.array([i[0] for i in out]) #only get the first component
    
    # plot FFT
    x = [ele.real for ele in yf] 
    y = [ele.imag for ele in yf] 
    plt.plot(x, y) 
    plt.ylabel('Imaginary') 
    plt.xlabel('Real') 
    plt.show() 


main("test.wav")