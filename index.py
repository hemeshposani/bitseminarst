import streamlit as st

st.title('CPSC Application')
page1 = st.Page('db.py' , title = 'test database')
page2 = st.Page('recalleddata.py' , title = 'load recalled data')
page3 = st.Page('sendemail.py' , title = 'send email')

selected_page = st.navigation([page1 , page2 , page3])
selected_page.run()
