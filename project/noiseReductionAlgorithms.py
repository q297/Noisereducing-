import noisereduce as nr
from df.enhance import enhance, init_df, load_audio
import librosa

def noise_reduction(file, sr=16000):
    y, sr = librosa.load(file, sr=sr)
    return nr.reduce_noise(y=y, sr=sr, stationary=False), sr
def noise_reduction2(file):
    model, df_state, _ = init_df()
    audio, _ = load_audio(file, sr=df_state.sr())
    return enhance(model, df_state, audio), df_state.sr()



