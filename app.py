import streamlit as st
import requests

ACCESS_TOKEN = "EAARwqiIhocUBOyHxGXhlIayjUSGdhxQG8EfedEpqcTZBI9lm5YeQVxZApply8v4juc6PXaBcYW9KeiyHE0KodD6DZBInymVTpP784fk4Tb0gN5oMFVUF4aH9ueJ18Uwv6q2P4KUvEI6KkW22VHIkBFT9H2HFZBsrxrodmYizaz3Fh3YnscdKZAxsmImhMKg0i70on79Vy5uUPYzRVQgZDZD"
GRAPH_API_VERSION = "v22.0"
BASE_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}"

st.set_page_config(page_title="Facebook Page Info Viewer", layout="wide")
st.title("🔍 Facebook Page Info Viewer")

page_id = st.text_input("ใส่ Page ID ที่ต้องการดึงข้อมูล", value="124360584280318")

@st.cache_data(show_spinner=False)
def get_page_info(page_id: str):
    fields = "name,followers_count,fan_count"
    url = f"{BASE_URL}/{page_id}?fields={fields}&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    return response.json()
  
if st.button("ดึงข้อมูลเพจ"):
    if not page_id.strip():
        st.warning("กรุณาใส่ Page ID ก่อน")
    else:
        with st.spinner("กำลังดึงข้อมูล..."):
            data = get_page_info(page_id)

        if "error" in data:
            st.error(f"เกิดข้อผิดพลาด: {data['error']['message']}")
        else:
            st.success("🎉 ดึงข้อมูลสำเร็จแล้ว")
            st.markdown(f"**ชื่อเพจ:** {data['name']}")
            st.metric(label="👥 จำนวนผู้ติดตาม (followers)", value=data['followers_count'])
            st.metric(label="👍 จำนวนผู้ถูกใจเพจ (fans)", value=data['fan_count'])
