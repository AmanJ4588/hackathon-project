from flask import Flask, request, jsonify , render_template
import google.generativeai as genai
import threading
import os


app = Flask(__name__)

def run_streamlit():
    os.system("streamlit run streamlit_app/main.py --server.port 8501 --server.headless true")

# Start Streamlit when Flask starts
threading.Thread(target=run_streamlit, daemon=True).start()

# Configure Gemini API
genai.configure(api_key="AIzaSyB_FZUX2L87MWS561tti3qyoN1qsvRHWpc")
# Use Gemini API for response
model = genai.GenerativeModel("gemini-pro")

messages = [] 

@app.route("/chat", methods=["POST"])
def chat():
    global messages

    data = request.json
    messages.extend( data.get("messages", []) ) 

    if not messages:
        return jsonify({"error": "No messages provided"}), 400
    

    try:
        response = model.generate_content(messages)
        reply = response.text
        # Store AI response in messages for context
        messages.append({"role": "model", "parts": [{"text": reply}]})
    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"response": reply})


@app.route("/save_preference", methods=["POST"])
def save_preference():
    global messages

    messages = []

    
    data = request.json

    # Generate a structured prompt for AI to understand the student profile
    prompt = f"""
    Here is my learning profile and preferences:

    - My Grade/Class Level: {data.get('grade')}
    - My Stream (if applicable): {data.get('stream')}
    - My Degree (if applicable): {data.get('degree')}
    - Subjects I need help with: {data.get('subjects_help')}
    - My Preferred Language for Learning: {data.get('preferred_lang')}
    - My Hobbies: {data.get('hobbies')}
    - My Career Aspirations: {data.get('career_asp')}
    - Am I interested in real-world applications? {data.get('real_world_application')}
    - My Study Hours per day: {data.get('study_hours')}
    - Am I preparing for exams? {data.get('preparing_for_exam')}
    - Exam(s) I'm preparing for: {", ".join(data.get('selected_exams', []))}
    - Challenges I face while studying: {", ".join(data.get('study_challenges', []))}

    Based on this, please provide me with personalized learning guidance and study recommendations that match my academic needs and interests.
    """


    try:
     
        # Save the structured prompt in the correct format
        messages.append({"role": "user", "parts": [{"text": prompt}]})

        # Send only the latest message to Gemini API
        response = model.generate_content([messages[-1]])
        ai_response = response.text

        # Store AI's response in messages for future context
        messages.append({"role": "model", "parts": [{"text": ai_response}]})


    except Exception as e:
        ai_response = f"Error generating response: {str(e)}"

    return jsonify({"message": "Preferences saved successfully!", "ai_response": ai_response})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
