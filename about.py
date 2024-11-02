import streamlit as st

def app():
    st.title("About")
    st.write('This model will give a idea like how much you have to spend Annually on your health and ')
    st.write('checkup(in USD) so that you live long and your family be happy.')
    st.write('The Various Parameters used in our model are as follows :')
    st.write('- Age: The age of the individual (ranging from 18 to 65 years).')
    st.write('- Sex: Gender of the individual (male or female).')
    st.write('- BMI: Body Mass Index of the individual, indicating the level of obesity (ranging from 15 to 40).')
    st.write('- Children: Number of children covered by health insurance (ranging from 0 to 5).')
    st.write('- Smoker: Smoking status of the individual (yes or no).')
    st.write('- Region: Residential area in the US (northeast, northwest, southeast, southwest).')
    st.write('The output you get is')
    st.write('- Medical Cost: Annual medical costs incurred by the individual (in USD).')