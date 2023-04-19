from matplotlib import pyplot
import numpy
import librosa
from extract_features import get_mfcc,get_melspectrogram,get_chroma_vector,get_tonnetz

# Sample audio path
audio = 'juliana_2.wav'

# Mel Frequency Cepstral Coefficients (MFCC)
mfcc = get_mfcc(sample)
pyplot.imshow(mfcc, interpolation='nearest', aspect='auto')