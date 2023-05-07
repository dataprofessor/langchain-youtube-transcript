import streamlit as st
from langchain.document_loaders import YoutubeLoader
from deepmultilingualpunctuation import PunctuationModel

st.title('📺 YouTube Transcription App')

with st.sidebar:
  st.header('About')
  st.markdown('''
  This app retrieves the transcript from a YouTube video.
  
  Powered by:
  - Streamlit
  - Langchain
  ''')

# Retrieve transcript from YouTube video
yt_url = 'https://www.youtube.com/watch?v=-3Kf2ZZU-dg'
loader = YoutubeLoader.from_youtube_url(yt_url, add_video_info=False)
results = loader.load()

## Extract only text content
yt_text = results[0].page_content
#st.write(yt_text)

## Text processing

#model = PunctuationModel()
#processed_text = model.restore_punctuation(text)
#st.write(processed_text)

# Display video thumbnail image
#def extract_yt_id(input_url):
#  if input_url.
#  return input_url.split('=')[-1]

yt_url.startswith('https://www.youtube.com')

yt_id = yt_url.split('=')[-1]
st.write(yt_id)
#st.image(yt_metadata.thumbnail_url, width=350) 
