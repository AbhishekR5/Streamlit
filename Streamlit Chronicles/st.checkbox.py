import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream',key="global_icecream")
coffee = st.checkbox('Coffee',key="global_coffee")
cola = st.checkbox('Cola',key="global_cola")

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

############################################################################

st.title('st.checkbox examples')
st.title('radio button , checkbox, and buttons')
page_names = ["checkbox", "radio button", "button"]
page = st.selectbox("Select a page", page_names)
if page == "checkbox":
    st.write("You selected checkbox")
    icecream = st.checkbox("Ice cream")
    coffee = st.checkbox("Coffee")
    cola = st.checkbox("Cola")

    if icecream:
        st.write("Great! Here's some more 🍦")

    if coffee:
        st.write("Okay, here's some coffee ☕")

    if cola:
        st.write("Here you go 🥤")

elif page == "radio button":
    st.write("You selected radio button")
    icecream = st.radio("Ice cream", ["Yes", "No"])
    coffee = st.radio("Coffee", ["Yes", "No"])
    cola = st.radio("Cola", ["Yes", "No"])

    if icecream == "Yes":
        st.write("Great! Here's some more 🍦")

    if coffee == "Yes":
        st.write("Okay, here's some coffee ☕")

    if cola == "Yes":
        st.write("Here you go 🥤")

elif page == "button":
    st.write("You selected button")
    icecream = st.button("Ice cream")
    coffee = st.button("Coffee")
    cola = st.button("Cola")

    if icecream:
        st.write("Great! Here's some more 🍦")

    if coffee:
        st.write("Okay, here's some coffee ☕")

    if cola:
        st.write("Here you go 🥤")