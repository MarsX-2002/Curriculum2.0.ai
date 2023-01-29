import streamlit as st
# from latex_template_1 import get_latex_text
import os
from PIL import Image

st.set_page_config(page_title="Curriculum.ai",
                   page_icon=":guardsman:", layout="wide")




# Header
st.header("Personal Information")
full_name = st.text_input("Full Name:")
email = st.text_input("Email:")
phone_number = st.text_input("Phone Number:")
linkedin_profile_url = st.text_input("LinkedIn URL:")
github_profile_url = st.text_input("Github URL:")

# Skills
st.header("Skills")
languages = st.text_input("Languages:")
frameworks = st.text_input("Frameworks:")
tools = st.text_input("Tools:")

# Education
st.header("Education")
EDUCATIONS = []
if st.button("Add Education"):
    EDUCATIONS.append(st.text_input("Enter Education"))

# Experience
st.header("Experience")
EXPERIENCES = []
if st.button("Add Experience"):
    EXPERIENCES.append(st.text_input("Enter Experience"))

# Projects
st.header("Projects")
PROJECTS = []
if st.button("Add Project"):
    PROJECTS.append(st.text_input("Enter Project"))

# Make the resume
if st.button("Create Resume"):
    heading = [full_name, email, phone_number,
               linkedin_profile_url, github_profile_url]
    skills = [languages, frameworks, tools]
    # get_latex_text(heading, skills, EDUCATIONS, EXPERIENCES, PROJECTS)
    os.system("cd result && pdflatex -interaction=nonstopmode Resume.tex")
    # st.success("Resume created!")

    if os.path.exists("result/Resume.pdf"):
        st.success("Resume created!")
        with open("result/Resume.pdf", "rb") as file:
            st.file(file, "application/pdf", "Resume.pdf")
    else:
        st.error("Resume not created. Please try again.")






# # List of image URLs
# images = [
#     Image.open("D:\streamlit\str1.png"),
#     Image.open("D:\streamlit\str2.png"),
#     Image.open("D:\streamlit\str3.png")
# ]

# # Create the carousel
# image_number = st.slider("Select Image", 0, len(images) - 1)
# st.image(images[image_number])
