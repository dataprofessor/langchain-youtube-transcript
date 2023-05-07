import streamlit as st
from langchain.document_loaders import YoutubeLoader
from punctuator import Punctuator

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
model = Punctuator('model.pcl')
processed_text = model.punctuate(yt_text)
st.write(processed_text)

#tokenizer = 
#model = PunctCapSegModelONNX.from_pretrained("pcs_en")
#processed_text = model.infer(yt_text)
#st.write(processed_text)

# Display video thumbnail image
def extract_yt_id(input_url):
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

yt_img_url = extract_yt_id(yt_url)
st.image(yt_img_url, width=350)

