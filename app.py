import streamlit as st

# Define functions for each page
def first_page():
    st.title("Holy day, thank you for being the biggest blessing. 01/08/2023")
    
    # Display the image from Google Drive
    st.image("https://drive.google.com/uc?export=view&id=1FBQb0dAUPUBHgYSTLc8DHvE8g48LZnHd", use_column_width=True)
    
    
    # Display the text
    st.write("""
    ### Shinjini and Anurag <3
    **The start of us**

    From what was just an instant connection between the headboy and the prefect, we have come a long way. 
    From asking you if everything was alright in class IV, to asking you if everything was alright at home... 
    a bond strong enough for a lifetime was formed.

    I take a moment to thank you for bearing with me. I am not the easiest guy. I am grateful I have you. 
    I am grateful I have a girl with whom even a day of fights is nothing short of an anniversary. 
    And with whom, every single day is a summer in the hills or a winter by the beach. Relaxing, soothing, 
    comforting, a feeling worth letting go the world for. The feeling of true love, as rare as it is, 
    is basically an umbrella word for so many feelings together. Companionship, friendship, partnership, 
    a guide, a soul to look up to and so much more :).
    """)

    # Add the surprise button
    if st.button("Surprise"):
        st.write("[Click here to see the surprise!](#upload link here)")
def second_page():
    st.title("Second Page")
    st.write("Content for the second page goes here.")

# Page navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Second Page"])

if page == "Home":
    first_page()
elif page == "Second Page":
    second_page()
