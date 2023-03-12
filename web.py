import streamlit as st


with st.expander("Click here to open Camera"):
    myimage =  st.camera_input('camera')

print (myimage)
print ('M V SIVAKUMAR')

