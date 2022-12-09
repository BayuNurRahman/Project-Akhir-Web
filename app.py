import streamlit as st
import base64
from scrape import getData

st.set_page_config(
    page_title='Project Akhir Web App',
    page_icon='🖥️'
)
st.title("Profil Github Scraper")

def add_background(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_background('sky.jpg')

userName = st.text_input('Enter Github Username')

if userName != '':
    try:
        info, repo_info = getData(userName)

        for key , value in info.items():
            if key != 'image_url':
                st.subheader(
                    '''
                    {} : {} 
                    '''.format(key, value)
                )
            else:
                st.image(value)
        st.subheader(" Recent Repositories")
        st.table(repo_info)
    except:
        st.subheader("User doesn't exist")


