
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.markdown("""
    <style>
    .reportview-container .markdown-text-container {
        padding-top: 2rem; /* Adjust the top padding of the text container */
    }
    .reportview-container .row-widget.stRadio > div {
        padding-top: 1rem; /* Adjust the top padding of the radio buttons */
    }
    /* You can add more styles here to target specific containers or widgets */
    </style>
    """, unsafe_allow_html=True)

# Load Lottie animations

def load_lottiefile(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None  # Or handle the error as you see fit


# Update this path
animation1_path = "https://lottie.host/34d43ec5-0e11-4a22-b958-9de09c373759/kHHlciiywS.json"
# Update this path
animation2_path = "https://lottie.host/799f6224-4087-4d91-838b-9e812e7cc146/BnvPSRZN4H.json"

animation1 = load_lottiefile(animation1_path)
animation2 = load_lottiefile(animation2_path)


# Header Section
with st.container():
    st.subheader("Hi :wave: I am Sreenija Jallipeta ")
    st.title("Looking for Opportunities as Software Developer / Data analyst")
    st.write("---")

st.header("**About Me**")
# About Me Section
with st.container():
    custom_bullet_points = """
        <ul style="list-style: none;">
            <li>* I am currently pursuing my final semester of Master's in Information Technology and Management at University of Texas at Dallas</li>
            <li>* I am very passionate about learning new ways to code efficiently using different technologies</li>
            <li>* I always try to look into improving myself by working more on developing my skills and knowledge</li>
        </ul>
    """
# Use the markdown function to render the HTML
st.markdown(custom_bullet_points, unsafe_allow_html=True)
st.write("---")

st.header(f"**Professional Experience**")
# What I Did - Section 1
with st.container():
    col1, col2 = st.columns([2, 2])
    with col1:
        st.subheader("Spectral MD, Dallas - System Engineering Intern")
        st.write("""
            - **Healthcare App Development**: Spearheaded the foundational development of a cutting-edge healthcare application, significantly enhancing user interaction and experience.
            - **Prototype Design**: Crafted an intuitive account management prototype, streamlining the end-user experience.
            - **Full Stack Development**: Designed and implemented a complete account management system from the ground up, integrating both front-end usability and back-end functionality to streamline user experiences across platforms.
        """)
    with col2:
        st_lottie(animation1, height=250, key="animation1")

# What I Did - Section 2
with st.container():
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader(
            "Tata Consultancy Services, Hyderabad - Software Developer")
        st.write("""
        - **Software Development and Innovation**: Enhanced software development practices by automating routine tasks and refining deployment processes, significantly boosting development speed and quality.
        - **Data Analytics and Integration**: Engineered robust data analysis systems that integrate seamlessly with backend operations, supporting critical decision-making and operational intelligence.
        - **Full Stack Development**: Leveraged a comprehensive stack of technologies including Python, SQL, and modern JavaScript frameworks to build dynamic, scalable full-stack applications, enhancing both client-side and server-side performance.
        - **DevOps Efficiency**: Advanced the automation of deployment pipelines and cloud environments using cutting-edge DevOps tools, optimizing infrastructure management and operational workflows.
        """)
    with col2:
        st_lottie(animation2, height=300, key="animation2")
st.write("---")

# Projects Section
st.header(f"**Projects**")
# Projects Data
projects = [
    {
        "title": "Hans Woodcrafts Digital Presence Enhancement",
        "description": "Crafted and enhanced the digital presence of Hans Woodcrafts, increasing client visibility by 40% through a meticulously designed website hosted on GoDaddy."
        st.markdown(Explore the website at [Visit Hans Woodcrafts](https://www.hanswoodcraft.com))
    },
    {
        "title": "ATS-Tracker",
        "description": "Developed an ATS Tracker on Streamlit that evaluates resumes against job descriptions using AI, offering immediate feedback on compatibility. This interactive tool converts PDF resumes, analyzes them with Google's Gemini Pro Vision AI, and provides a detailed compatibility percentage."
        st.markdown(Explore the website at (https://ats-tracker-of01.onrender.com/))
    },
    {
        "title": "Research Study on Data Analysis - Pricing in Healthcare",
        "description": "Led a detailed analysis of healthcare pricing, employing Excel and Python for robust data cleaning and preprocessing. Designed and implemented insightful visualizations using Python and Tableau, which enabled healthcare administrators to refine and optimize pricing strategies effectively."
    },
]

custom_css = """
<style>
.big-title {
    font-size: 25px !important;
    font-weight: bold !important;
}
.small-text {
    font-size: 16px !important;
}
</style>
"""

# Inject custom CSS with the above styles
st.markdown(custom_css, unsafe_allow_html=True)

# Display projects with titles in a slightly larger font size
for project in projects:
    with st.expander(project["title"]):
        # Use markdown for the description with a smaller font size class
        st.markdown(
            f"<div class='small-text'>{project['description']}</div>", unsafe_allow_html=True)


# Contact Section
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")

    st.write("Feel free to reach out to me directly:")
    st.write("**Email:** sreenija.jallipeta@gmail.com")
    st.write("**Phone:** (945)-249-2029")

    contact_form = """
                <form action="https://formsubmit.co/sreenija.jallipeta@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required><br>
                    <input type="email" name="email" placeholder="Your email" required><br>
                    <textarea name="message" placeholder="Your message here" required></textarea> <br>
                    <button type="submit">Send</button>
                </form>
                """
    st.markdown(contact_form, unsafe_allow_html=True)
    st.markdown("""
                <style>
/* Style inputs with type="text", select elements and textareas */
input[type=text],input[type=email], select, textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */
  border: 1px solid black; /* lack border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 12px; /* Add a top margin, increase if you want more space */
  margin-bottom: 12px; /* Bottom margin, increase if you want more space */
  resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
  background-color: white; /* Change the background color inside the box */
}

/* Style the submit button with a specific background color etc */
input[type=submit] {
  background-color: black;
  color: black;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 12px; /* Add a top margin, same as input for consistent spacing */
}

/* When moving the mouse over the submit button, add a darker green color */
input[type=submit]:hover {
  background-color: #45a049;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
