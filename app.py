import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# Page Configuration
st.set_page_config(
    page_title="AI Email Generator",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Email Generator")
st.write("Generate professional emails instantly using Google Gemini AI.")

# Input Fields
recipient = st.text_input("Recipient Name")

subject = st.text_input("Email Subject")

purpose = st.text_area("Purpose of the Email")

tone = st.selectbox(
    "Select Tone",
    [
        "Professional",
        "Friendly",
        "Formal",
        "Apology",
        "Request",
        "Thank You"
    ]
)

length = st.selectbox(
    "Email Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

# Generate Button
if st.button("Generate Email"):

    if recipient == "" or subject == "" or purpose == "":
        st.warning("Please fill all fields.")
    else:

        prompt = f"""
        Write a {tone} email.

        Recipient: {recipient}

        Subject: {subject}

        Purpose: {purpose}

        Length: {length}

        Generate only the email.
        """

        with st.spinner("Generating email..."):

            response = model.generate_content(prompt)

            st.success("Email Generated Successfully!")

            st.text_area(
                "Generated Email",
                response.text,
                height=350
            )
