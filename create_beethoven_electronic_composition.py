import music21
from music21 import stream, note, tempo, meter
import mido
from mido import MidiFile, MidiTrack, Message
from pydub import AudioSegment
import subprocess

# Function to create composition
def create_beethoven_style_composition():
  s = stream.Score()
  part = stream.Part()

  part.append(tempo.MetronomeMark(number=120))
  part.append(meter.TimeSignature('4/4'))

  for i in range(8):
    n = note.Note('C4')
    n.duration.type = 'half'
    part.append(n)

  electronic_part = stream.Part()
  for i in range(8):
    n = note.Note('C2', duration=music21.duration.Duration(1))
    electronic_part.append(n)

  s.insert(0, part)
  s.insert(0, electronic_part)
  return s

def convert_stream_to_midi(s):

  midi_file = music21.midi.MidiFile()

  mf = music21.midi.translate.streamToMidiFile(s)

  midi_data = mf.writestr()
  
  midi_filename = 'output.mid'

  midi_file.open(midi_filename)
  midi_file.write(midi_data)
  midi_file.close()

  return midi_file

# Function to save MIDI to MP3
def save_midi_to_mp3(midi_file, mp3_filename='Beethoven_Reimagined.mp3'):

  midi_filename = 'temp.mid'
  
  midi_file_fp = open(midi_filename, 'wb')

  midi_data = midi_file.write()

  midi_file_fp.write(midi_data)

  midi_file_fp.close()

  subprocess.run(['fluidsynth', '-ni', 'soundfont.sf2', midi_filename, '-F', 'output.wav', '-r', '44100'])

  AudioSegment.from_wav('output.wav').export(mp3_filename, format='mp3')

  subprocess.run(['rm', midi_filename])
  subprocess.run(['rm', 'output.wav'])


# Main execution
beethoven_composition = create_beethoven_style_composition()
midi_file = convert_stream_to_midi(beethoven_composition)
save_midi_to_mp3(midi_file)