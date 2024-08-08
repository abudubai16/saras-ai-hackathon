import streamlit as st

def welcome_interface():
    st.title("Welcome to Streamlit App")
    st.write("Enter 'go' in the text box below to proceed to the next interface.")
    user_input = st.text_input("Enter text:")
    if user_input.lower() == "go":
        return True
    return False

def next_interface():
    st.title("Next Interface")
    st.write("You have successfully reached the next interface!")
    # Add more components or logic for the next interface here

def main():
    st.sidebar.title("Navigation")
    current_interface = st.sidebar.radio("Go to:", ["Welcome Interface", "Next Interface"])

    if current_interface == "Welcome Interface":
        if welcome_interface():
            st.empty()  # Clear the Welcome Interface components
            next_interface()

if __name__ == "__main__":
    main()
