import streamlit as st
from time import sleep
from stqdm import stqdm # for getting animation after submit event 


import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler


#from src.pipeline.predict_pipeline import CustomData, PredictPipeline
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
        #menu = ["--Select--","Review Analysis","Stores Strengths and Weaknesses"]
        #choice = st.sidebar.selectbox("Choose your Analysis", menu)
        st.write("""
                        This MLOps Project aims to be a practice of CICD pipeline Deployment in AWS Cloud Service
            """)
            
        st.write("""                    
                The objective of the model is to predict the Math score of a student given the following set of
                    features:
                    
                    - gender : sex of students  -> (Male/female)
                    - race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)
                    - parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)
                    - lunch : having lunch before test (standard or free/reduced) 
                    - test preparation course : complete or not complete before test
                    - reading score
                    - writing score
                """)
        
        st.write("Let's choose your features!")
        menu_gender = ["--Select--",
                    "Male",
                    "Female"
                    ]
        choice_gender = st.sidebar.selectbox("Choose your Gender", menu_gender)

        menu_ethnicity = [   "--Select--",
                            "Group A",
                            "Group B",
                            "Group C",
                            "Group D",
                            "Group E"
                            ]
        choice_ethnicity = st.sidebar.selectbox("Choose your Ethnicity", menu_ethnicity)

        menu_parental = [   "--Select--",
                            "Associate's degree",
                            "Bachelor's degree",
                            "High school",
                            "Master's degree",
                            "Some college"
                            ]
        choice_parental = st.sidebar.selectbox("Choose your Parents' final education", menu_parental)

        menu_lunch = ["--Select--",
                    "Standard",
                    "Free"
                    ]
        choice_lunch = st.sidebar.selectbox("Choose your Lunch", menu_lunch)
        
        if choice_lunch == "Standard":
            choice_lunch = 1
        elif choice_lunch == "Free":
            choice_lunch = 0

        menu_test_preparation = [   "--Select--",
                                    "Completed",
                                    "Not Completed"
                                    ]
        choice_test_preparation = st.sidebar.selectbox("Choose your Preparation", menu_test_preparation)

        if choice_test_preparation == "Completed":
            choice_test_preparation = 1
        elif choice_test_preparation == "Not Completed":
            choice_test_preparation = 0



        


        
            


'''
#data should store the form characteristics
pred_df = data.get_data_as_data_frame()
print(pred_df)
predict_pipeline = PredictPipeline()
result = predict_pipeline.predict(pred_df)
print(result)
return result

'''


if __name__ == '__main__':
    main()