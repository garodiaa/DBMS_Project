import streamlit as st

st.title('Counter: example of session state')


if 'count' not in st.session_state:
    st.session_state.count = 0 # Initialize count to 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= 1

st.write('Count = ', st.session_state.count)

if st.button('Go to Profile'):
    st.session_state.page = 'profile'

if 'page' in st.session_state and st.session_state.page == 'profile':
    st.write('Profile Page')
    st.write('Count = ', st.session_state.count)