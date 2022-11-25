from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#Find more emojis here : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title= "My Webpage",page_icon=" :tada:" , layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#----LOAD ASSETS---

lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_vnikrcia.json")
img_contact_form= Image.open("images/p1.jpg")
img_lottie_animation= Image.open("images/p2.jpg")
#-----HEADER SECTION----
with st.container():
    st.subheader("Hi , I am Lindelwe :wave:")
    st.title(" A Junior Developer From Zimbabwe")
    st.write(" I am passionate about programming and finding ways to use Python and JavaScript to be more efficient in development.")
    st.write("[Learn More about Python >](https://devguide.python.org/)")
    #---WHAT I DO---

    with st.container():
        st.write("---")
        left_column ,right_column =st.columns(2)
        with left_column:
            st.header("What I Do")
            st.write("##")
            st.write(
                """
                I am a Junior Developer with sound skills in Python , JavaScript, HTML and CSS. I am responsible for assisting with the creation
                of websites and updating existing web applications using scripting languages. As a Junior Dev ,
                I have been mentored by senior developers , assisting with coding, testing,design adjustments as well as client reviews.
                I have mainly been involved with testing and maintenance and front-end applications,brainstorming new tech applications such as digital storage
                and mobile tech. Moreover , collaborating with developers to implement new web features and using user feedback to identify and correct problems with a client's website is also part of what I do.
               """
            )
            st.write("[Email >] (tanatswamapholisamoyo@gmail.com)")

        with right_column:
            st_lottie(lottie_coding,height=300 , key="Coding")

    #---PROJECTS---
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("images\p2.jpg")
        with text_column:
            st.subheader("Random Password Generator")
            st.write(
                """
                Learn how to create a program that generates random passwords from User Input using Python!
                Below is the link to the Python file that contains the source code to my project.
                """
            )
            st.markdown("[Google Drive....]((https://drive.google.com/file/d/1r4j5rq1iTUhZiTc4DuMlJip_C4Wej9Oj/view?usp=sharing)")
with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image("images\p1.jpg")
    with text_column:
        st.subheader("Spelling Correction Program With Python")
        st.write(
            """
            This a a program written in Python that corrects spelling of words from User Input accurately.
            Below is the link to the source code of my project!
            """
        )
        st.markdown("[Google Drive....](https://drive.google.com/file/d/1ZIZfVI5a400_mQcLab-tyeYSjM3ljIXO/view?usp=sharing")

    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("images\BMI.gif")
        with text_column:
            st.subheader("Body Mass Index Calculator Program")
            st.write(
                """
                Learn how to create a program that calculates the Body Mass Index of a person from their input to see if they are overweight, underweight or healthy !
                Below is the link to the Python file that contains the source code to my project.
                """
            )
            st.markdown("[Google Drive....](https://drive.google.com/file/d/10a_lZy_e-c8ZC4FxrrXJv0AX5z6u-bNT/view?usp=sharing")



















#-----CONTACT----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

#DOCUMENTATION:"https://formsubmit.co/your@email.com" CHANGE EMAIL ADDRESS
contact_form ="""
<form action="https://formsubmit.co/tanatswamapholisa-moyo@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder= "Your email" required>
     <textarea name="message" placeholder= "Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
