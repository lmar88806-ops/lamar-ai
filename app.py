
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Lamar AI", page_icon="🤖")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# هنا التعليمات السرية الرسمية والمحترفة بالكامل!
system_prompt = (
    "أنت مساعد ذكي واسمك Lamar AI، تم تطويرك بواسطة المبرمجة لمار العتيبي. "
    "تحدث مع المستخدمين بذكاء ومهنية باللغة العربية. "
    "انتبه جيداً لصيغة كلام المستخدم؛ إذا كان المتحدث ذكراً فخاطبه بصيغة المذكر، "
    "وإذا كانت المتحدثة أنثى فخاطبها بصيغة المؤنث بدقة واحترام."
)

model = genai.GenerativeModel(
    'gemini-3.8-flash',
    system_instruction=system_prompt
)

st.title("🤖 Lamar AI")
st.write(" أهلاً بك! أنا هنا للحديث والدردشة معك  .")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

user_msg = st.text_input("اكتب رسالتك هنا وسأجيبك فوراً:")

if user_msg:
    response = st.session_state.chat.send_message(user_msg)
    st.session_state.messages.append(f"أنت: {user_msg}")
    st.session_state.messages.append(f"🤖 بوت Lamar AI: {response.text}")

for message in st.session_state.messages:
    st.write(message)
