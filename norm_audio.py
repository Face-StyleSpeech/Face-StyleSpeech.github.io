import glob
import torch
import librosa
import sys, os
import unicodedata
from tqdm import tqdm
import numpy as np
import soundfile as sf
from pathlib import Path

def normalize_audio(audio, rms_level=-10):
    r = 10**(rms_level / 10.0)
    a = torch.sqrt((len(audio) * r**2) / torch.sum(audio**2))

    y = audio * a

    return y

path = Path('static/wavs/')
wav_files = [*path.glob('*.wav')]

for wav_file in tqdm(wav_files):
    wav, _ = librosa.load(wav_file, sr=16000)
    # wav = wav.squeeze().cpu().numpy()
    new_wav = normalize_audio(torch.Tensor(wav), rms_level=-12)
    sf.write(wav_file, new_wav, 16000)