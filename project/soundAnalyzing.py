from sys import exit
import librosa
from matplotlib import pyplot as plt
import numpy as np
if __name__ == "__main__":
    exit()

def showDifference_wave(file1, file2):
    y, sr = librosa.load(file1, sr=None)
    y1, sr1 = librosa.load(file2, sr=None)
    fig, axs = plt.subplots(2, figsize=(10, 6), gridspec_kw={'hspace': 0.5})
    fig.suptitle('Wave Difference')
    librosa.display.waveshow(y, sr=sr, ax=axs[0])
    axs[0].set_title("Original")
    librosa.display.waveshow(y1, sr=sr1, ax=axs[1])
    axs[1].set_title("Modified")
    plt.xlabel("Time (s)")
    plt.show()

def showDifference_wave2(file1, file2):
    y, sr = librosa.load(file1, sr=None)
    y1, sr1 = librosa.load(file2, sr=None)
    plt.figure(figsize=(10, 6))
    librosa.display.waveshow(y, sr=sr, color='blue', alpha=0.5, label='Original')
    librosa.display.waveshow(y1, sr=sr1, color='orange', alpha=0.5, label='Modified')
    plt.title("Overlayed Waves")
    plt.xlabel("Time (s)")
    plt.legend()
    plt.show()


def showDifference_spectrum(file1, file2):
    y, sr = librosa.load(file1, sr=None)
    y1, sr1 = librosa.load(file2, sr=None)
    fig, axs = plt.subplots(2, figsize=(10, 6), gridspec_kw={'hspace': 0.5})
    fig.suptitle('Spectrum Difference')
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    axs[0].set_title("Original")
    librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="linear", ax=axs[0])
    D1 = librosa.amplitude_to_db(np.abs(librosa.stft(y1)), ref=np.max)
    axs[1].set_title("Modified")
    librosa.display.specshow(D1, sr=sr1, x_axis="time", y_axis="linear", ax=axs[1])
    plt.show()