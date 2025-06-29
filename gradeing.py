import streamlit as st

st.title ('Grading system')

marks = st.number_input('enter obtain marks:', min_value=1)

total = st.number_input('enter total marks:',min_value=1)

p = marks/total  * 100

st.subheader (f'your persentage: :blue{p} %')

if p >= 80:
    st.sucess('Excellent')
elif p >= 60:
    st.info('pass')
else:
    st.error('fail')
