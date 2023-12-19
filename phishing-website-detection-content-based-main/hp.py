import streamlit as st
import time
def app():
    

# Custom CSS for styling
    st.markdown(
        """
        <style>
        .stButton > button {
            background-color: #FF5733;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }
        .stButton > button:hover {
            background-color: #FF4500;
        }
        .stMarkdown {
            font-size: 16px;
            line-height: 1.6;
        }
        .stProgress > div > div {
            background-color: #FF5733;
        }
        .stSelectbox, .stText {
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Main content
    st.title("Phishing Awareness")

    # Add a colorful and informative banner
    st.image("phishing-security-freepik1170x658v4.jpg")

    # Create a sidebar with navigation options
    sidebar_choice = st.sidebar.radio("Select a Section", ["Home", "What is Phishing", "How to Spot Phishing", "Protecting Yourself"])

    # Animated loading indicator
    with st.spinner("Loading..."):
        time.sleep(2)

    # Content for different sections
    if sidebar_choice == "Home":
        st.markdown(
            """
            Welcome to the Phishing Awareness app! 
            Learn how to protect yourself from phishing attacks.
            """
        )

    if sidebar_choice == "What is Phishing":
        st.header("What is Phishing?")
        st.markdown(
            """
            Phishing is a cyberattack method where attackers impersonate legitimate entities to steal sensitive information. 
            They often use fake emails and websites to deceive users.
            """
        )

    if sidebar_choice == "How to Spot Phishing":
        st.header("How to Spot Phishing")
        st.markdown(
            """
            Here are some tips to help you spot phishing attempts:

            - **Check sender's email:** Verify the sender's email address.
            - **Look for errors:** Phishing emails often contain spelling and grammar mistakes.
            - **Hover over links:** Check where links lead before clicking.
            - **Avoid downloading:** Don't download suspicious attachments.
            - **Stay updated:** Keep software and antivirus updated.
            """
        )

    if sidebar_choice == "Protecting Yourself":
        st.header("Protecting Yourself")
        st.markdown(
            """
            Protect yourself from phishing:

            - **Use strong passwords:** Use a password manager.
            - **Enable two-factor authentication (2FA):** For added security.
            - **Stay informed:** Keep up with phishing trends.
            - **Install antivirus:** It can detect phishing attempts.
            - **Report phishing:** Report suspicious emails to authorities.
            """
        )

    # Add an interactive button at the end
    st.markdown("---")
    if st.button("Learn More"):
        st.write("You can find more information on our website.")

    # Add a footer-like text
    st.markdown("---")
    st.markdown("Stay safe online and protect your digital identity!")


