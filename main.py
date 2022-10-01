import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import random

st.audio('riders.mp3')


def get_name():
    prefix = ['Yu', 'Em', 'Rin', 'Hae', 'Say', 'Ez', 'Nat', 'Ya', 'Re', 'Sa']
    suffix = ['Chun', 'Chi', 'Yul', 'Yue', 'Uril', 'Neil', 'Phae']

    return random.choice(prefix).lower() + random.choice(suffix).lower()


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_8qbuaxlc.json')

st.title('EMA NAME GENERATOR')
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        if st.button('--- Generate 10 Ema Names ---'):
            tables = pd.DataFrame({'Names': [get_name() for i in range(10)]})
            st.table(tables)

    with right_column:
        st_lottie(lottie_coding, height=300, key='coding2')

st.write('---')
