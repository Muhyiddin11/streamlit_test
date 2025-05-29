import streamlit as st 
import requests

# Set the app title 
st.title('My First Streamlit Apps yow !!') 

# Add a welcome message 
st.write('Selamat datang ke website amba !') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Yow, Streamlit baka !') 

# Display the customized message 
st.write('Customized Message:', widgetuser_input)

# API call to get currency rates with base MYR
response = requests.get('https://api.vatcomply.com/rates?base=MYR')

if response.status_code == 200:
    data = response.json()
    
    # Get the list of available currencies
    currency_options = list(data['rates'].keys())
    currency_options.sort()  # sort alphabetically for convenience
    
    # Add a selectbox for currency selection
    selected_currency = st.selectbox('Pilih mata wang:', currency_options)
    
    # Display the selected currency rate
    selected_rate = data['rates'][selected_currency]
    st.write(f"Kadar tukaran MYR kepada {selected_currency}: {selected_rate}")
    
    # Show the full JSON response (optional)
    with st.expander("Lihat semua kadar tukaran"):
        st.json(data)

else:
    st.error(f"API call failed with status code: {response.status_code}")
