import streamlit as st

def quiz_page():
    st.title("📝 Generate a Custom Quiz")

    st.write("Fill in the details below to generate a personalized quiz.")

    # Subject input
    subject = st.text_input("Enter the subject for the quiz (e.g., Math, Science, History)")

    # Topic input
    topic = st.text_input("Enter the specific topic within the subject (e.g., Algebra, Newton's Laws)")

    # Number of questions per difficulty level
    easy_questions = st.number_input("How many easy questions?", min_value=0, step=1, value=5 , max_value=5)
    medium_questions = st.number_input("How many medium questions?", min_value=0, step=1, value=5 , max_value=5)
    hard_questions = st.number_input("How many hard questions?", min_value=0, step=1, value=5 , max_value=5)

    # Submit button
    if st.button("Generate Quiz"):
        if not subject or not topic:
            st.error("Please enter both the subject and topic to proceed.")
        else:
            quiz_prompt = f"""
            Generate a multiple-choice quiz on the subject "{subject}" focusing on the topic "{topic}". 
            The quiz should contain:
            - {easy_questions} easy questions
            - {medium_questions} medium questions
            - {hard_questions} hard questions

            Each question should have:
            1. A clear and concise question statement.
            2. Four answer choices labeled (A), (B), (C), and (D).
            3. The correct answer indicated separately.

            Format the response as follows:
            [
                {{
                    "question": "What is 2 + 2?",
                    "options": {{"A": "3", "B": "4", "C": "5", "D": "6"}},
                    "correct_option": "B"
                }},
                ...
            ]
            """
            
            st.success(f"✅ Quiz request submitted!\n\n- **Subject:** {subject}\n- **Topic:** {topic}\n- **Easy:** {easy_questions} questions\n- **Medium:** {medium_questions} questions\n- **Hard:** {hard_questions} questions")
            

