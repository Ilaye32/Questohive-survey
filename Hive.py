import streamlit as st
import pandas as pd
import os
from datetime import datetime

# CSV filename (saved in the same folder as your app)
csv_file = "questohive_feedback.csv"

# Optional: create file with header if it doesn't exist yet
if not os.path.exists(csv_file):
    df_init = pd.DataFrame(columns=[
        "timestamp","level","faculty","category","past_questions_freq",
        "favorite_ai","ai_accuracy_trust","exam_type_same",
        "website_engagement","website_user_friendly","suggestion"
    ])
    df_init.to_csv(csv_file, index=False)

# UI
questohive_link = "https://questohive.com"
st.link_button("Visit Questohive", questohive_link)

st.header('📝 Questohive Customer Satisfaction Survey')

st.write(
    "Thank you for taking a moment to help us improve! This brief survey is designed to gather "
    "feedback from university students and graduates. No personal information is required. "
    "Your responses will guide us in enhancing our services to better meet your academic needs."
)

st.write(
    f"If this is your first time hearing about Questohive, feel free to explore our platform at "
    f"[Questohive.com]({questohive_link}) — your one-stop destination for verified past questions "
    f"and academic support."
)
st.divider()

with st.form(key="sample_form"):
    st.subheader('🎓 Section 1: Academic Background')
    level = st.selectbox('What is your current academic level?',
                         ['100 level','200 level','300 level','400 level','500 level','Graduate'])
    Faculty = st.selectbox("2. Which faculty are you affiliated with?",
                           ['Faculty of Engineering', 'Faculty of Science', 'Faculty of Law',
                            'Faculty of Management Sciences', 'Faculty of Agriculture',
                            'Faculty of Education', 'Faculty of Humanities', 'Faculty of Social Sciences',
                            'Faculty of Communication and Media Studies', 'College of medical Sciences'])
    Category = st.selectbox("3. Does your discipline primarily involve:",
                            ['Numbers (e.g., Engineering, Mathematics, Economics)',
                             'Theories (e.g., Law, Philosophy, History)','A mix of both'])

    st.subheader("📚 Section 2: Study Habits")
    PQ = st.radio('On a scale of 1–5, how often do you use past questions to prepare for exams and tests? (1 = Never, 5 = Always)',
                  ['1','2','3','4','5'])

    st.subheader('🤖 Section 3: AI Preferences')
    AI = st.radio('Which of the following is your favorite AI tool for studying?',
                  ['Chat-GPT',"Grok",'Gemini','Deepseek','Microsoft Capilot'])
    # Fixed syntax here:
    Accuracy = st.selectbox('On a scale of 1–10, how much do you trust your selected AI to generate accurate answers in your field of study? (1 = Not at all, 10 = Completely)',
                            ['1','2','3','4','5','6','7','8','9','10'])
    Exam_type = st.radio('Do you think preparing for an objective exam is the same as preparing for a theoretical exam?',
                         ['Yes','No'])

    st.subheader('🌐 Section 4: Website Experience')
    Web_eng = st.radio('On a scale of 1–5, how engaging was the website experience? (1 = Not engaging, 5 = Very engaging)',
                       ['1','2','3','4','5'])
    Web_friend = st.radio('How user friendly was the website?', ['1','2','3','4','5'])
    Suggestion = st.text_input('What suggestions do you have to improve the user experience?')

    submit_button = st.form_submit_button('Submit')

# Handle submission: append to CSV
if submit_button:
    # Build the row as a dict
    new_row = {
        "timestamp": datetime.now().isoformat(),
        "level": level,
        "faculty": Faculty,
        "category": Category,
        "past_questions_freq": PQ,
        "favorite_ai": AI,
        "ai_accuracy_trust": Accuracy,
        "exam_type_same": Exam_type,
        "website_engagement": Web_eng,
        "website_user_friendly": Web_friend,
        "suggestion": Suggestion
    }

    # Append to CSV (write header only if file did not exist)
    try:
        df_new = pd.DataFrame([new_row])
        df_new.to_csv(csv_file, mode='a', header=not os.path.exists(csv_file), index=False)
        st.success('Thank you — your response has been saved!')
    except Exception as e:
        st.error(f"Failed to save response: {e}")
