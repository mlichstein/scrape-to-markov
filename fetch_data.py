import re
import requests
from bs4 import BeautifulSoup

def fetch_lyrics(artist, song):
  artist = artist.lower()
  song = song.lower()
  artist = re.sub('[^A-Za-z0-9]+', "", artist)
  song = re.sub('[^A-Za-z0-9]+', "", song)
  if artist.startswith("the"):
    artist = artist[3:]
  url = "https://azlyrics.com/lyrics/"+artist+"/"+song+".html"
  header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}

  site = requests.get(url, headers=header)
  soup = BeautifulSoup(site.text, 'html.parser')
  lyrics = str(soup)
  top = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
  bottom = '<!-- MxM banner -->'
  lyrics = lyrics.split(top)[1]
  lyrics = lyrics.split(bottom)[0]
  lyrics = lyrics.replace('<br>', '').replace('<br/>', '').replace('<i>', '').replace('</i>', '').replace('</div>', '')
  lyrics = lyrics.strip()
  return lyrics

print fetch_lyrics("Foo Fighters", "My Hero")