import streamlit as st
import requests

def preferences_page():
    st.title("⚙ Preferences")

    st.write("Please fill out the form to personalize your learning experience.")

    st.subheader("Student Profile & Learning Preferences")

    # Initialize session state for grade and sub-options
    if "selected_grade" not in st.session_state:
        st.session_state.selected_grade = None
    if "selected_stream" not in st.session_state:
        st.session_state.selected_stream = None
    if "selected_degree" not in st.session_state:
        st.session_state.selected_degree = None

    #Q1
    # Dropdown for grade/class level
    grade_options = [
        "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th",
        "9th", "10th", "11th", "12th", "Undergraduate", "Postgraduate"
    ]
    st.session_state.selected_grade = st.selectbox(
        "What is your current grade/class level?", grade_options
    )

    # Show sub-questions dynamically
    if st.session_state.selected_grade in ["11th", "12th"]:
        stream_options = ["Science (Maths)", "Science (Biology)", "Commerce", "Arts"]
        st.session_state.selected_stream = st.selectbox("Which stream are you in?", stream_options , index=0)

    if st.session_state.selected_grade == "Undergraduate":
        ug_degrees = ["B.Tech", "BBA", "B.Com", "B.Sc"]
        st.session_state.selected_degree = st.selectbox("Which UG degree are you pursuing?", ug_degrees , index=0)

    elif st.session_state.selected_grade == "Postgraduate":
        pg_degrees = ["M.Tech", "MBA", "M.Com", "M.Sc"]
        st.session_state.selected_degree = st.selectbox("Which PG degree are you pursuing?", pg_degrees)

    #Q2 
    subjects_help = st.text_input(
        "Which subjects do you need the most help with? (E.g., Math, Science, English, Social Studies)"
    )

    #Q3 
    preferred_lang = st.text_input(
        "What is your preferred language for learning? (E.g., Hindi, English, Tamil)"
    )

    #Q4 
    hobbies = st.text_input( 
        "What are your hobbies? (E.g., Drawing, Coding, Sports, Reading)"  
    )

    #Q5 
    career_asp = st.text_input( 
        "Do you have any career aspirations? (E.g., Doctor, Engineer, Scientist, Teacher)" 
    )  

    #Q6
    real_world_application = st.radio(
    "Would you like to relate your studies to real-world applications in your field of interest?",
    ("Yes", "No")
    )

    #Q7 
    study_hours = st.radio(
    "How many hours per day do you dedicate to studying?",
    ("Less than 1 hour", "1-2 hours", "2-4 hours", "More than 4 hours")
    )

    #Q8 
    preparing_for_exam = st.radio("Are you preparing for any upcoming exams?", ("Yes", "No"))

    if preparing_for_exam == "Yes":
        exam_options = [
            "School Exams", "Board Exams", "JEE", "NEET", "CUET", 
            "College Exams", "GATE", "CAT" , "UPSC"
        ]
        selected_exams = st.multiselect("Which exam(s) are you preparing for?", exam_options)
    else : 
        selected_exams = "None"

    #Q9 
    faces_study_challenges = st.radio("Do you face any challenges while studying?", ("Yes", "No"))

    if faces_study_challenges == "Yes":
        study_challenges = st.multiselect(
            "What is your biggest challenge in studying?",
            [
                "Time management", 
                "Understanding concepts", 
                "Memorization", 
                "Practice problems", 
                "Lack of motivation", 
                "Distractions"
            ]
        )
    else : 
        study_challenges = "None"






    # Submit button
    if st.button("Save Preferences"):
        # Prepare user preference data
        preferences_data = {
            "grade": st.session_state.selected_grade,
            "stream": st.session_state.selected_stream if st.session_state.selected_grade in ["11th", "12th"] else "None",
            "degree": st.session_state.selected_degree if st.session_state.selected_grade in ["Undergraduate", "Postgraduate"] else "None",
            "subjects_help": subjects_help,
            "preferred_lang": preferred_lang,
            "hobbies": hobbies,
            "career_asp": career_asp,
            "real_world_application": real_world_application,
            "study_hours": study_hours,
            "preparing_for_exam": preparing_for_exam,
            "selected_exams": selected_exams,
            "faces_study_challenges": faces_study_challenges,
            "study_challenges": study_challenges
        }

        BACKEND_URL = "http://127.0.0.1:5000"  # Change this if needed
        # Send POST request to Flask backend
        response = requests.post(f"{BACKEND_URL}/save_preference", json=preferences_data)

        # Handle response
        if response.status_code == 200:
            st.success("✅ Preferences saved successfully!")
        else:
            st.error("❌ Failed to save preferences. Please try again.")
        



