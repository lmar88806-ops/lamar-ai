import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Lamar AI", page_icon="🤖")

# هنا الاسم الكبير والفخم الذي سيظهر للناس بأعلى الموقع!
st.title("🤖 Lamar AI")
st.write("مرحباً بكِ في تطبيقي الخاص للذكاء الاصطناعي!")

# إعداد مربع الدردشة والذاكرة
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# مربع كتابة الرسائل للمستخدمين
user_msg = st.text_input("اكتبي رسالتكِ هنا وسأجيبكِ فوراً:")

if user_msg:
    st.session_state.chat_history.append(f"أنتِ: {user_msg}")
    st.session_state.chat_history.append("🤖 بوت Lamar AI: أهلاً بكِ! موقع الويب الخاص بكِ قيد التشغيل والربط الآن بنجاح!")

# عرض الدردشة بشكل أنيق
for message in st.session_state.chat_history:
    st.write(message)
