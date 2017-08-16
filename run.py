from fetch_data import fetch_lyrics
from markov_python.cc_markov import MarkovChain

def gather_info():
  artist = str(raw_input("Enter the name of an artist or band: ")).lower()
  song = str(raw_input("Enter a song title: ")).lower()
  return fetch_lyrics(artist, song)

print gather_info()
