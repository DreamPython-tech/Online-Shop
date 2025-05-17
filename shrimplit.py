import streamlit as st
from datetime import time, datetime
st.header('Welcome to Dream tea website')


option = st.selectbox(
     'Which drink do you want?',
     ('Passion fruit pearl tea', 'classic bubble tea', 'brown sugar milk tea'))

st.write('Your selected drink is', option)

st.subheader('sweet level ')

sweet  = st.slider('How sweet do you want', 0, 130, 25)
st.write("I want ", sweet, 'sweet level')

st.subheader('ice level ')

ice  = st.slider('how cold do you want your drink to be', 0, 50, 100)
st.write("I want ", ice, 'ice level')

st.header('Extra toppings')

options = st.multiselect(
     'What would you want to add as toppings',
     ['Extra pearls', 'Grass Jelly', 'Aloe Jelly', 'Taro balls'],
     ['Grass Jelly', 'Aloe Jelly'])

st.write('You selected:', options)


st.header('Extra snacks ')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
chickenwings = st.checkbox('Chicken wings')
ramen = st.checkbox('Ramen')

if icecream:
     st.write("Great! Here's some more 🍦")

if chickenwings: 
     st.write("Okay, here's some chickenwings 🍗")

if ramen:
     st.write("Here you go 🍜")

st.write("Enjoy your meal and have a nice day! :)")

quit()
