import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Lamar AI", page_icon="🤖")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-3.8-flash')

st.title("🤖 Lamar AI")
# هنا العبارة الجديدة الفخمة والمرحبة!
st.write(" أهلاً بكِ! أنا هنا للحديث والدردشة معك  .")
 

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

user_msg = st.text_input("اكتبي رسالتكِ هنا وسأجيبكِ فوراً:")

if user_msg:
    response = st.session_state.chat.send_message(user_msg)
    st.session_state.messages.append(f"أنتِ: {user_msg}")
    st.session_state.messages.append(f"🤖 بوت Lamar AI: {response.text}")

for message in st.session_state.messages:
    st.write(message)
