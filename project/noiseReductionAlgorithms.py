import noisereduce as nr
def noise_reduction(y, sr):
    return nr.reduce_noise(y=y, sr=sr, stationary=False)