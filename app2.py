from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
import streamlit as st 
#from apikey import apikey 
import time
#os.environ['OPENAI_API_KEY'] = apikey
#OPENAI_API_KEY = 'Your key'

st.title('✍️🔗 YouTube Links Summary ✍️')

st.markdown("<h2 style='color:blue;'>Enter Your openai API KEY</h2>", unsafe_allow_html=True)
key= st.text_input('Ex: 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') 

st.markdown("<h1>Enter Your YouTube Link </h1>", unsafe_allow_html=True)
link = st.text_input('Plug in your link here') 

loader = YoutubeLoader.from_youtube_url(link, add_video_info=True)

result = loader.load()

#print (type(result))
#print (f"Found video from {result[0].metadata['author']} that is {result[0].metadata['length']} seconds long")
# print ("")
# print (result)

llm = OpenAI(temperature=0, openai_api_key=key)

chain = load_summarize_chain(llm, chain_type="stuff", verbose=False)
#chain.run(result)

#print(chain.run(result))

if link: 
    res= chain.run(result)

    st.write(res)
    with st.spinner('Loading...'):
    # Simulate long running computation
    time.sleep(2)
    st.success('Done!')


