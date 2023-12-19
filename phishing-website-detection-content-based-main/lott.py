import json

import requests  
import streamlit as st  
from streamlit_lottie import st_lottie  
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("animation_lmyfj2wj.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://lottie.host/ef2bb939-c3be-4876-96cb-7c7d23a37e8b/Bk8f8fHzt2.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    renderer="svg", # canvas
    height=None,
    width=None,
    key=None,
)
