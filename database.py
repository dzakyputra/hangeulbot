from google.cloud import texttospeech
from bs4 import BeautifulSoup

import pandas as pd
import requests
import re


def get_hangeul():

  # Scrape the website and get list of titles
  url = 'https://www.bbc.com/korean/popular/read'
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  titles = soup.findAll('span', 
                       {'class': 'most-popular-list-item__headline'})
  
  # Iterate through titles -> remove punctuation -> append to the list
  result = []
  for title in titles:
    title = re.sub(r'[^\w\s]','',title.text)
    words = title.split()
    result += words
  
  # Return the unique words
  return set(result)

def create_audio(text, language='ko-KR'):

  # Instantiates a client
  client = texttospeech.TextToSpeechClient()

  # Set the text input to be synthesized
  synthesis_input = texttospeech.types.SynthesisInput(text=text)

  # Build the voice request, select the language code ("ko-KR") and the ssml
  # voice gender ("neutral")
  voice = texttospeech.types.VoiceSelectionParams(
    language_code=language,
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

  # Select the type of audio file you want returned
  audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

  # Perform the text-to-speech request on the text input with the selected
  # voice parameters and audio file type
  response = client.synthesize_speech(synthesis_input, voice, audio_config)

  # The response's audio_content is binary.
  with open('audio/{}.mp3'.format(text), 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)

if __name__ == "__main__":

  # Get list of korean words and get the audio for each word
  words = get_hangeul()

  for word in words:
    create_audio(word)

  # Create the dataframe of words and save it as .csv file
  dictionary = pd.DataFrame(words, columns=['word'])
  dictionary.to_csv('dictionary.csv', index=False)
