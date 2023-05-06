import streamlit as st
from langchain.document_loaders import YoutubeLoader
from rpunct import RestorePuncts

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
rpunct = RestorePuncts(use_cuda=False)
processed_text = rpunct.punctuate(text)

#st.write(processed_text)

# Display video thumbnail image
#st.image(yt_metadata.thumbnail_url, width=350) 
