import json
import streamlit as st
import requests
from streamlit_lottie import st_lottie

def app():

    def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code!=200:
            return None
        return r.json
    lottie_coding="https://lottie.host/ef2bb939-c3be-4876-96cb-7c7d23a37e8b/Bk8f8fHzt2.json"
    lottie_hello = "https://lottie.host/1dd7926f-a913-4e8e-a5dc-0a2f7e9c20e7/Fr4YlZK3R6.json"
    

    
    with st.container():

        st.title("Home")
        st.subheader("Welcome to this ride")
        st.write("Here you can discover if the URL is malicious or not")
    with st.container():
        st.write("---")    
        left_column,right_column=st.columns(2)
        with left_column:
            st.header("What is Phishing ?")
            st.write('##')
            st.write(
                """
                
                 Phishing is like a sneaky chameleon of the internet world. Imagine you're walking through a virtual forest of emails and websites,
                  and suddenly, you come across a colorful, enticing flower. This flower seems so attractive that you can't resist clicking on it.
                  But here's the trick – that flower isn't a real one;
                  it's a crafty digital predator in disguise."""
                
               
            )
            st.write("""Phishing is the art of deception in the online realm. It's when cyber-criminals disguise themselves as trustworthy entities, using alluring bait to lure you into their traps. They mimic your bank, your favorite online store, or even your boss, making you feel like you're in a safe garden.
                      But when you interact with them, they steal your personal information, like a sly chameleon snatching its prey.""")
        with right_column:
            st.write('##')
            st.write("---")
            st_lottie(lottie_coding,height=300) 
        #----Next section----
        with st.container():
            st.write("---")
            st.header("How to spot Phishing?")
            st.write('##')
            st_lottie(lottie_hello,height=600,width=1000)
            st.write('##')
            st.write('##')
            st.write(
                """
                Here are some key points to help you spot phishing attempts:

                - Check the Sender's Email Address: Examine the sender's email address closely. Phishing emails often use slightly altered or fake email addresses that mimic legitimate ones.
                  Look for misspellings or unusual domain names.
                - Watch for Urgent or Threatening Language: Phishing emails often create a sense of urgency or fear to prompt quick action.
                  Be skeptical of emails that threaten dire consequences if you don't respond immediately.
                - Inspect URLs Carefully: Hover your mouse pointer over any links in the email without clicking on them. Check if the URL displayed matches the website it claims to be.
                  Be cautious of URLs with misspelled domain names or extra characters.  
                - Check for Spelling and Grammar Mistakes: Phishing emails often contain noticeable spelling and grammatical errors.
                  Professional organizations typically proofread their messages.  
            """)



