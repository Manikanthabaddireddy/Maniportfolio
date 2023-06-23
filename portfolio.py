import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="portfolio",page_icon=":tada:",layout="wide")
with st.container():
    text_col,dp_col=st.columns(2)
    with text_col:
        st.subheader("Hi,I am Mani :wave:")
        st.title("A Data Enginner From India")
        st.write("i am passionate about working with data, willingness to learn new technologies! ")
    with  dp_col:
        img=Image.open(r"resized_pspk.jpg")
        st.image(img)
def lottie_fun(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_coding=lottie_fun("https://assets7.lottiefiles.com/packages/lf20_44gjzh9a.json")
# what i do
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.subheader("What I Have")
        st.write("##")
        st.write("""
        - I am  a data engineer having 1+ years of experience with azure tech stack.
        - Have a good explosure on python, sql, aws,pyspark.
        - In free time will explore present trending tech stack related to data.
        
        
        """)
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")

# projects

with st.container():
    st.subheader("Projects")
    st.write("##")
    st.write("HR Workday data migration")



st.write("##")
st.subheader(":mailbox: Get in Touch!")
form="""<form action="https://formsubmit.co/manibaddireddy7571@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <textarea name="message" placeholder="Type your message"></textarea>
    <button type="submit">Send</button>
</form>"""
st.markdown(form,unsafe_allow_html=True)

def css_fun(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call the function with the CSS file path
css_fun("style/style.css")