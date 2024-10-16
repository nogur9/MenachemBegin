import streamlit as st
import time
from PIL import Image

if 'screen_num' not in st.session_state:
    st.session_state.screen_num = 1

st.title("Menachem Begin's Timer")

#  ---  Screen I  ---

if st.session_state.screen_num == 1:

    # Display a video and a cute message after countdown
    st.write("So what is it all about?")
    video_file = open("images/startup-idea.mp4", "rb")  # Replace with your video file
    st.video(video_file.read(), format="video/mp4")
    if st.button("Continue to the app..."):
        st.session_state.screen_num = 2
        st.rerun()


#  ---  Screen II  ---

if st.session_state.screen_num == 2:
    image = Image.open("images/בגין נגד פסיכולוג.png")  # Make sure you have a suitable image file
    st.image(image, width=400)
    st.write("How long do you want me to be depressed and stay indoors for you? 😊")
    # Timer input
    timer_hours = st.number_input("Set the timer (hours):", min_value=0, value=0)
    timer_minutes = st.number_input("Set the timer (minutes):", min_value=0, value=0)
    timer_seconds = st.number_input("Set the timer (seconds):", min_value=0, value=10)

    # Convert the time to seconds
    total_seconds = int(timer_minutes * 60 + timer_minutes * 60 + timer_seconds)
    print(f"before button {st.session_state.screen_num =}")
    if st.button("Start Countdown"):
        st.session_state.screen_num = 3
        st.session_state.total_seconds = total_seconds
        st.rerun()

    # ---  Screen III  ---

if st.session_state.screen_num == 3:
    # Countdown mechanism
    image = Image.open("images/Menachem_Begin_sitting.jpg")  # Make sure you have a suitable image file
    st.image(image, caption="Stay positive and keep smiling! 😊")
    print(f"in stage 3 {st.session_state.screen_num =}")
    with st.empty():
        for remaining in range(st.session_state.total_seconds, 0, -1):
            print(f"counting in 3 {st.session_state.screen_num =}")

            minutes, seconds = divmod(remaining, 60)
            st.subheader(f"{minutes:02d}:{seconds:02d}")
            time.sleep(1)
        st.subheader("00:00")
    st.session_state.screen_num = 4
    st.rerun()



    # ---  Screen IV  ---
if st.session_state.screen_num == 4:
    image = Image.open("images/Begin.jpg")  # Make sure you have a suitable image file
    st.image(image, width=400)
    st.write("Stay positive and keep smiling! 😊")