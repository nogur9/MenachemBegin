import streamlit as st
import time
from PIL import Image

if 'screen_num' not in st.session_state:
    st.session_state.screen_num = 1

st.title("Menachem Begin's Timer")

#  ---  Screen I  ---

if st.session_state.screen_num == 1:

    # Display a video and a cute message after countdown
    st.write("?אז, מה הקטע")
    video_file = open("images/startup-idea.mp4", "rb")  # Replace with your video file
    st.video(video_file.read(), format="video/mp4")
    if st.button("...המשך"):
        st.session_state.screen_num = 2
        st.rerun()


#  ---  Screen II  ---

if st.session_state.screen_num == 2:
    image = Image.open("images/בגין נגד פסיכולוג.png")  # Make sure you have a suitable image file
    st.image(image, width=300)
    st.write("אני כאן בשבילך")
    st.write("?לכמה זמן תרצה.י שאני אהיה בדיכאון ובחרדה במקומך")
    st.write("אשאר עבורך עם כל המחשבות הרעות, מבלי לצאת מהבית כל היום")
    st.write("תמשיכו את היום שלכם כרגיל")
    # Timer input
    timer_hours = st.number_input("שעות", min_value=0, value=0)
    timer_minutes = st.number_input("דקות", min_value=0, value=0)
    timer_seconds = st.number_input("שניות", min_value=0, value=10)

    # Convert the time to seconds
    total_seconds = int(timer_hours * 3600 + timer_minutes * 60 + timer_seconds)
    if st.button("Start Countdown"):
        st.session_state.screen_num = 3
        st.session_state.total_seconds = total_seconds
        st.rerun()

# ---  Screen III  ---

if st.session_state.screen_num == 3:
    # Countdown mechanism
    image = Image.open("images/Menachem_Begin_sitting.jpg")  # Make sure you have a suitable image file
    st.image(image, caption="Stay positive and keep smiling! 😊")
    with st.empty():
        for remaining in range(st.session_state.total_seconds, 0, -1):
            minutes, seconds = divmod(remaining, 60)
            st.subheader(f"{minutes:03d}:{seconds:02d}")
            time.sleep(1)
        st.subheader("00:00")
    st.session_state.screen_num = 4
    st.rerun()

#  ---  Screen IV  ---

if st.session_state.screen_num == 4:
    image = Image.open("images/Begin.jpg")  # Make sure you have a suitable image file
    st.image(image, width=400)
    st.write("")
    st.text_input("?איך עבר עליכם היום")
    st.write("")
    st.write("""
            
    
א.פרידריך ניטשה –
         לחיות זה לסבול, לשרוד זה למצוא משמעות בסבל

ב.אלבר קאמי – 
    המשמעות המילולית של החיים היא כל דבר שאתה עושה שמונע ממך להרוג את עצמך

ג.סרן קירקגור – 
        החיים ניתנים להבנה רק לאחור; אבל יש לחיות אותם קדימה

ד.פרידריך ניטשה – 
    מי שיש לו למה לחיות, יוכל לשאת כמעט כל איך

    """
             )


    st.write("good vibes only! 😊")

