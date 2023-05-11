# Create email
# from email.message import EmailMessage
# import base64
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
#
# newMail = EmailMessage()
# newMail['Subject'] = "Email from Python code"
# newMail['From'] = "sachinarora133@gmail.com"
# newMail['To'] = "sachinarora133@gmail.com"
# newMail.set_content("Hello.. This email is sent from python code on 5th May")
# with open('/Users/abc/Desktop/My Docs/General docs/me.png', 'rb') as f:
#     newMail.add_attachment(f.read(), maintype="image", subtype='.png', filename=f.name)
#
# # Encoding
# byteData = newMail.as_bytes()
# rawData = base64.urlsafe_b64encode(byteData).decode()
# finalData = {'raw': rawData}
#
# # Verify on Google
# flow = InstalledAppFlow.from_client_secrets_file('/Users/abc/Downloads/key.json', ['https://mail.google.com/'])
# cred = flow.run_local_server(port=0)
#
# # Create the service which you want to use from Google
# service = build('gmail', 'v1', credentials=cred)
#
# # Send the mail
# service.users().messages().send(userId="sachinarora133@gmail.com", body=finalData).execute()
#
# # want to fetch user profile data
# response = service.users().getProfile(userId="sachinarora133@gmail.com").execute()
# print(response)


# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
#
# cred = credentials.Certificate("/Users/abc/Desktop/key.json")
# app = firebase_admin.initialize_app(cred, {'databaseUrl': 'https://pythondatabase-49f14-default-rtdb.firebaseio.com/'})
#
# # Retrieve data from db
# ref = db.reference('/', url='https://pythondatabase-49f14-default-rtdb.firebaseio.com/')
# d = ref.get()
# print(d)
#
# # Insert data to db
# emp_id = input('Enter emplyeee id \n')
# emp_name = input('Enter emplyeee name \n')
# emp_age = int(input('Enter emplyeee age \n'))
# emp_salary = int(input('Enter emplyeee salary \n'))
#
# dictToInsert = {"Name": emp_name, "Age": emp_age, "Salary": emp_salary}
#
# refToInsert = db.reference('/' + emp_id, url='https://pythondatabase-49f14-default-rtdb.firebaseio.com/')
# refToInsert.update(dictToInsert)


import streamlit as st
st.set_page_config(page_title="My Streamlit", page_icon='random' )
menu = st.sidebar.selectbox('My Menu', ('Home', 'Fill the form', 'Downloads'))
st.title('StreamLit tutorial')
st.header('This is a basic tutorial on streamlit library usage')

if menu == 'Home':
    st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/Untitled_design__6_-removebg-preview-1-300x169.png')
elif menu == 'Fill the form':
    with st.form('My Form') :
        name = st.text_input('Enter the name')
        dob = st.date_input('Enter the Date of birth')
        marks = st.slider('Select the marks')
        result = st.form_submit_button('Submit the form')
        if result:
            st.write('Name:', name, 'DOB:', dob, 'Marks:', marks)

elif menu == 'Downloads':
    st.header('Downloads Page')
    st.download_button('Download now', 'This is some Dummy data', 'sachin.txt')
