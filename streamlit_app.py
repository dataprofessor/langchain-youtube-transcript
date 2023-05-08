import streamlit as st
from langchain.document_loaders import YoutubeLoader

st.set_page_config(page_title="YouTube Transcription App")

st.title('📺 YouTube Transcription App')

with st.sidebar:
  st.header('About')
  st.markdown('''
  This app retrieves the transcript from a YouTube video.
  
  Powered by:
  - Streamlit
  - Langchain
  ''')

# YouTube URL
# yt_url = 'https://youtu.be/n_3XDVOVraI'
yt_url = st.text_input('Enter YouTube video URL', '')

# Get YouTube video ID
def extract_yt_id2(input_url):
  processed_url = []
  if input_url.startswith('https://www.youtube.com') or input_url.startswith('https://youtube.com'):
    input_url_split = input_url.split('=')[-1]
    processed_url.append(input_url_split)
    #return f'http://i.ytimg.com/vi/{input_url_split}/maxresdefault.jpg'
  if input_url.startswith('https://youtu.be/'):
    input_url_split = input_url.split('/')[-1]
    processed_url.append(input_url_split)
    #return f'http://i.ytimg.com/vi/{input_url_split}/maxresdefault.jpg'
  return f'http://i.ytimg.com/vi/{processed_url[0]}/maxresdefault.jpg'

def extract_yt_id(input_url):
  processed_url = []
  if input_url.startswith('https://www.youtube.com') or input_url.startswith('https://youtube.com'):
    input_url_split = input_url.split('=')[-1]
    processed_url.append(input_url_split)
  if input_url.startswith('https://youtu.be/'):
    input_url_split = input_url.split('/')[-1]
    processed_url.append(input_url_split)
  return processed_url

# Get YouTube thumbnail image
def get_yt_img(input_id):
  return st.image(f'http://i.ytimg.com/vi/{processed_url[0]}/maxresdefault.jpg', width=350)

# Retrieve transcript from YouTube video
def get_transcript(input_url):
  loader = YoutubeLoader.from_youtube_url(yt_url, add_video_info=False)
  results = loader.load()
  yt_text = results[0].page_content
  return st.write(yt_text)

# Conditional display of content
if yt_url == '':
  st.warning('👆 Please enter a YouTube video URL to get started!')
  # st.code('https://youtu.be/n_3XDVOVraI')
  st.code('https://www.youtube.com/watch?v=n_3XDVOVraI')
else: 
  ## Display YouTube thumbnail image
  yt_id = extract_yt_id(yt_url)
  get_yt_img(yt_id)
  #st.image(yt_img_url, width=350)
  #st.write(yt_img_url)
  
  ## Display transcription
  with st.expander('See video transcript'):
    get_transcript(yt_url)
