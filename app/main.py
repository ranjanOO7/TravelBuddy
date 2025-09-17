import streamlit as st
from TravelBuddy import TravelBuddy

travelBuddy = TravelBuddy()

def create_app():
    with st.form("travel_form"):
        destination = st.text_input("Destination")
        days = st.number_input("Days", min_value=1, step=1, format="%d")
        inputs = {
            "destination": destination,
            "days": days
        }
        submit = st.form_submit_button("Submit")
        if submit:
            response = travelBuddy.travelBuddyCrew().kickoff(inputs=inputs)
            st.write(f"Destination: {destination}")
            st.write(f"Days: {int(days)}")
            st.markdown(response)


if __name__ == "__main__":
    st.title("Travel Buddy 🛫")
    st.set_page_config(layout="wide", page_title="Travel Buddy", page_icon="🛫")
    create_app()