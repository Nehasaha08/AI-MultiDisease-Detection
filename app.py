import streamlit as st
from utils.chatbot import ask_medical_ai
from Auth.register import register_user
from Auth.login import login_user
from utils.pdf_generator import generate_pdf
from utils.prediction import predict_disease

from utils.database import (
    create_prediction_table,
    save_prediction,
    get_history
)


create_prediction_table()

st.set_page_config(
    page_title="AI Multi Disease Detection",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Login",
        "Register"
    ]
)

if not st.session_state.logged_in:

    if menu == "Register":

        st.title("Register")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Register"):

            if register_user(
                username,
                password
            ):
                st.success(
                    "Registration Successful"
                )
            else:
                st.error(
                    "User Already Exists"
                )

    if menu == "Login":

        st.title("Login")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if login_user(
                username,
                password
            ):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.rerun()

            else:
                st.error(
                    "Invalid Credentials"
                )

else:

        st.sidebar.success(
            f"Welcome {st.session_state.username}"
        )

        if st.sidebar.button("Logout" ,key="logout-btn"):
            st.session_state.logged_in = False
            st.rerun()

        # Navigation appears ONLY after login
        menu = st.sidebar.radio(
            "🏥 Navigation",
            [
                "🏠 Dashboard",
                "🩺 Disease Detection",
                "📊 Prediction History",
                "📄 Medical Reports",
                "🤖 AI Health Assistant"
            ]
        )

        # ==========================
        # DASHBOARD
        # ==========================
        if menu == "🏠 Dashboard":

            st.title("🏠 Dashboard")

            st.info(
                f"Welcome {st.session_state.username}"
            )
            history = get_history(st.session_state.username)

            prediction_count = len(history)

            import os

            report_count = 0

            if os.path.exists("reports"):
                report_count = len(
                    [
                        f for f in os.listdir("reports")
                        if f.endswith(".pdf")
                    ]
                )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Predictions", prediction_count)

            with col2:
                st.metric("Reports", report_count)

            with col3:
                st.metric("AI Chats", len(st.session_state.get("messages", [])))

        # ==========================
        # DISEASE DETECTION
        # ==========================
        elif menu == "🩺 Disease Detection":

            st.title(
                "🩺 Disease Detection"
            )

            uploaded = st.file_uploader(
                "Upload Medical Image",
                type=["png", "jpg", "jpeg"]
            )

            if uploaded:

                from PIL import Image

                image = Image.open(uploaded)

                st.image(image)

                if st.button(
                        "Predict Disease"
                ):
                        image_type, disease, confidence = predict_disease(image)

                        st.success(f"Image Type : {image_type}")
                        st.success(f"Disease : {disease}")
                        st.success(f"Confidence : {confidence:.2f}%")

                        # Save prediction
                        save_prediction(
                            st.session_state.username,
                            image_type,
                            disease,
                            confidence
                        )

                        # Generate PDF
                        pdf_path = generate_pdf(
                            st.session_state.username,
                            image_type,
                            disease,
                            confidence
                        )

                        st.success("✅ Medical report generated successfully.")

                        # Download Button
                        with open(pdf_path, "rb") as pdf_file:
                            st.download_button(
                                label="📄 Download Medical Report",
                                data=pdf_file,
                                file_name=f"{st.session_state.username}_report.pdf",
                                mime="application/pdf"
                            )

        # ==========================
        # HISTORY
        # ==========================
        elif menu == "📊 Prediction History":

            st.title(
                "📊 Prediction History"
            )

            history = get_history(
                st.session_state.username
            )

            st.dataframe(history)

        # ==========================
        # REPORTS
        # ==========================
        elif menu == "📄 Medical Reports":



            import os

            st.title("📄 Medical Reports")

            report_folder = "reports"

            if os.path.exists(report_folder):

                files = [
                    f for f in os.listdir(report_folder)
                    if f.endswith(".pdf")
                ]

                if files:

                    for file in files:
                        path = os.path.join(report_folder, file)

                        with open(path, "rb") as pdf:
                            st.download_button(
                                label=f"📄 {file}",
                                data=pdf,
                                file_name=file,
                                mime="application/pdf"
                            )

                else:
                    st.info("No reports generated yet.")

            else:
                st.info("Reports folder not found.")
        # ==========================
        # AI ASSISTANT
        # ==========================
        elif menu == "🤖 AI Health Assistant":

            st.title(
                "🤖 AI Health Assistant"
            )

            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(
                        message["role"]
                ):
                    st.markdown(
                        message["content"]
                    )

            prompt = st.chat_input(
                "Ask a medical question..."
            )

            if prompt:
                st.session_state.messages.append({
                    "role": "user",
                    "content": prompt
                })

                with st.chat_message("user"):
                    st.markdown(prompt)

                response = ask_medical_ai(prompt)

                with st.chat_message(
                        "assistant"
                ):
                    st.markdown(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

                st.rerun()