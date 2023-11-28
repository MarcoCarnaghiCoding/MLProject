import streamlit as st
from time import sleep
from stqdm import stqdm # for getting animation after submit event 


import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler


from src.pipeline.predict_pipeline import CustomData, PredictPipeline
#======================================================
#               Sidebar
#======================================================
def draw_all(
    key,
    plot=False,
):
    st.write(
        """
        BASIC MLOps Project
        """
    )
    
with st.sidebar:
    draw_all("sidebar")


    def main():
        st.title("BASIC MLOps Project")
        menu = ["--Select--","Review Analysis","Stores Strengths and Weaknesses"]
        choice = st.sidebar.selectbox("Choose your Analysis", menu)


        if choice=="--Select--":
            #folder_path = 'Streamlit2/TopicModellingStreamlit-main'
            folder_path = '.'
            st.image(folder_path + '/figures/indatalogo.jpg')

            st.write("""
                    
                    This Natural Language Processing Based Web App was trained using 
                    Google and Yelp datasets, which include reviews from various stores across the USA.
            """)
            
            st.write("""
                    
                    This NLP web app is based on two main models:
                    1. A BERT model for sentiment analysis, which identifies whether a review has a positive,
                    negative, or neutral connotation.
                    2. An LDA unsupervised model for topic modeling, which recognizes the presence of 10 topics in a review.
            """)


'''
#data should store the form characteristics
pred_df = data.get_data_as_data_frame()
print(pred_df)
predict_pipeline = PredictPipeline()
result = predict_pipeline.predict(pred_df)
print(result)
return result

'''