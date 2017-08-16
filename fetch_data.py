import re
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def fetch_lyrics(artist, song):
  lyrics = ""
  artist = artist.lower()
  song = song.lower()
  artist = re.sub('[^A-Za-z0-9]', "", artist)
  song = re.sub('[^A-Za-z0-9]', "", song)
  if artist.startswith("the"):
    artist = artist[3:]
  url = "https://azlyrics.com/lyrics/"+artist+"/"+song+".html"
  user_agent = UserAgent()
  header = {'User-Agent': str(user_agent.random)}

  site = requests.get(url, headers=header)
  soup = BeautifulSoup(site.text, 'html.parser')
  for words in soup.find_all("div", {"class":""}):
    lyrics += words.text
  return lyrics
