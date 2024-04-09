import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")


dessert = st.sidebar.selectbox('Pick a dessert',('Indian', 'American', 'Mexican', 'Arabic', 'Caribbean', 'Italian', 'Japanese '))


if dessert:
    response = langchain_helper.generate_restaurant_name_and_dessert_items(dessert)

    st.header(response['restaurant_name'].strip())
    dessert_items = response['dessert_items'].strip().split(", ")
    st.write('**Dessert Items**')
    for item in dessert_items:
        st.write('-', item)

