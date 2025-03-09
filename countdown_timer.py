import streamlit as st
import time

# Title of the app
st.title("Countdown Timer")

# Ask the user for the countdown time
seconds = st.number_input("**Enter the time in seconds:**", min_value=1, value=10)

# Start the countdown
if st.button("**Start Timer**"):
    with st.empty():  # Create an empty placeholder
        while seconds > 0:
            # Display the remaining time
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"  # Format as MM:SS
            st.header(timer)  # Display the timer
            time.sleep(1)  # Wait for 1 second
            seconds -= 1  # Decrease the time by 1 second

        st.success("Time's up!")  # Display when the timer ends