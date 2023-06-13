# YouTube-links_summary

This is a Python script that uses OpenAI, the Langchain library and Streamlit to create a web application that can summarize YouTube video content. 

## Overview

The application prompts a user to input a YouTube URL and then uses the Langchain library to load the video data and the OpenAI API to generate a summary. The summarized output is then displayed on the web application. 

## Dependencies

* [Langchain](https://github.com/Langchain/langchain) - A Python library for handling Language models and tasks.
* [OpenAI](https://www.openai.com/) - AI models for generating human-like text.
* [Streamlit](https://streamlit.io/) - An open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.
* [YoutubeLoader](https://github.com/Langchain/langchain/blob/main/langchain/document_loaders/youtube_loader.py) - A tool provided by Langchain to fetch video data from YouTube.


## How to Run

1. To start the Streamlit application, use the following command:
```
streamlit run app.py
```
2. Go to the URL provided in the terminal to view and interact with the application.
3. Input a YouTube video URL in the provided text input field and the app will display the summarized content.

## Limitations

* As the OpenAI API can be expensive to use, please ensure that you monitor your usage.
* As with any AI generated text, results may vary based on the input and the settings for the language model.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
