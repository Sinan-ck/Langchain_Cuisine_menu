import streamlit as st
import resto_cuisine
st.title("Hello❤️ Every one , Welcome Todays Match *🍲*")
cuisine = st.sidebar.selectbox("Pick cuisine",("Indian","italian","Arabic","Spanish","Mexican","German","Turkish","African","US","Canadian","Kerala","malappuram","malabar","kozikode","kannur"),
                               index = None,
                               placeholder="Choose a cuisine...")

 


if  cuisine:
    response = resto_cuisine.cuisine_name(cuisine)
    st.header(response.content)
    response2 = resto_cuisine.menu_items(response)
    st.write(response2.content)
     


