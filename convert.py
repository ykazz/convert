from os import path
from pydub import AudioSegment

#filesinuse
source = "filename.mp3"
destination = "test.wav"

#process
sound= AudioSegment.from_mp3(source)
sound.export(destination, format="wav") 