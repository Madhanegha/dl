import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import tensorflow as tf

  

def sample():
    return "working"
# defining the function which will make the prediction using 
# the data which the user inputs
def  prediction(indgred1,indgred2,indgred3,indgred4,indgred5,indgred6,indgred7,indgred8,indgred9):  
    model=tf.keras.models.load_model("file.h5")
    n=[[indgred1,indgred2,indgred3,indgred4,indgred5,indgred6,indgred7,indgred8,indgred9]]
    res=model.predict(n)
    if res>1:
        return "Transported"
    else:
       return "Not Transported"
       


  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Pulsar")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:red;padding:10px">
    <h1 style ="color:black;text-align:center;">Pulsars </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    indgred1= st.number_input("id")
    indgred2= st.number_input("Mean_Integrated")
    indgred3= st.number_input("SD")
    indgred4= st.number_input("EK")
    indgred5= st.number_input("Skewness ")
    indgred6= st.number_input("Mean_DMSNR_Curve")
    indgred7= st.number_input("SD_DMSNR_Curve")
    indgred8= st.number_input("EK_DMSNR_Curve")
    indgred9= st.number_input("Skewness_DMSNR_Curve")

    result=""
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
   # sample()
    if st.button("Predict"):
        result = prediction(indgred1,indgred2,indgred3,indgred4,indgred5,indgred6,indgred7,indgred8,indgred9)
    st.success('The Transported Status is {}'.format(result))
     
if __name__=='__main__':
    main()