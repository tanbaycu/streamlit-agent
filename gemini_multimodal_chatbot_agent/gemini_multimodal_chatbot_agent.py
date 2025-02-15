import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import base64
import json


st.set_page_config(page_title="Trò chuyện Đa phương tiện với Gemini", layout="wide")
st.title("Trò chuyện Đa phương tiện với Gemini 🚀")
st.caption("Trải nghiệm sức mạnh của các mô hình Gemini mới nhất với tùy chỉnh nâng cao. 🌟")


if "messages" not in st.session_state:
    st.session_state.messages = []
if "image" not in st.session_state:
    st.session_state.image = None
if "model_config" not in st.session_state:
    st.session_state.model_config = {
        "model_name": "gemini-1.5-flash-latest",
        "temperature": 0.7,
        "top_p": 1.0,
        "top_k": 40,
        "max_output_tokens": 2048,
    }
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "Bạn là một trợ lý AI hữu ích và thân thiện."


GEMINI_MODELS = [
    "gemini-1.5-flash-latest",
    "gemini-2.0-flash-exp",
    "gemini-1.5-flash-8b",
    "gemini-2.0-pro-exp-02-05",
    "gemini-2.0-flash-lite-preview-02-05"
]


with st.sidebar:
    st.title("Cài đặt")
    api_key = st.text_input("Nhập Google API Key", type="password")
    
    st.title("Tùy chỉnh Mô hình")
    selected_model = st.selectbox("Chọn mô hình Gemini", GEMINI_MODELS, index=GEMINI_MODELS.index(st.session_state.model_config["model_name"]))
    st.session_state.model_config["model_name"] = selected_model
    
    st.session_state.model_config["temperature"] = st.slider("Độ sáng tạo", min_value=0.0, max_value=1.0, value=st.session_state.model_config["temperature"], step=0.1)
    st.session_state.model_config["top_p"] = st.slider("Top P", min_value=0.0, max_value=1.0, value=st.session_state.model_config["top_p"], step=0.1)
    st.session_state.model_config["top_k"] = st.number_input("Top K", min_value=1, max_value=100, value=st.session_state.model_config["top_k"])
    st.session_state.model_config["max_output_tokens"] = st.number_input("Số token tối đa", min_value=1, max_value=8192, value=st.session_state.model_config["max_output_tokens"])
    
    st.title("Tùy chỉnh Prompt")
    st.session_state.system_prompt = st.text_area("System Prompt", value=st.session_state.system_prompt, height=100)
    
    st.title("Tải lên Hình ảnh")
    uploaded_file = st.file_uploader("Tải lên một hình ảnh...", type=["jpg", "jpeg", "png"])


@st.cache_resource
def load_model(api_key, model_name):
    try:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel(model_name=model_name)
    except Exception as e:
        st.error(f"Lỗi khởi tạo mô hình: {str(e)}")
        return None

def get_image_download_link(img, filename, text):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{filename}">{text}</a>'
    return href

if api_key:
    model = load_model(api_key, st.session_state.model_config["model_name"])
    
    if uploaded_file:
        st.session_state.image = Image.open(uploaded_file)
        st.sidebar.image(st.session_state.image, caption='Hình ảnh đã tải lên', use_column_width=True)
        st.sidebar.markdown(get_image_download_link(st.session_state.image, "hình_ảnh_đã_tải.png", "Tải xuống hình ảnh"), unsafe_allow_html=True)

    
    chat_placeholder = st.container()

    with chat_placeholder:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


    prompt = st.chat_input("Bạn muốn biết gì?")

    if prompt:
        full_prompt = f"{st.session_state.system_prompt}\n\nNgười dùng: {prompt}\n\nTrợ lý:"
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with chat_placeholder:
            with st.chat_message("user"):
                st.markdown(prompt)
        
        inputs = [full_prompt]
        if st.session_state.image:
            inputs.append(st.session_state.image)

        with st.spinner('Đang tạo phản hồi...'):
            try:
                response = model.generate_content(
                    inputs,
                    generation_config=genai.types.GenerationConfig(
                        temperature=st.session_state.model_config["temperature"],
                        top_p=st.session_state.model_config["top_p"],
                        top_k=st.session_state.model_config["top_k"],
                        max_output_tokens=st.session_state.model_config["max_output_tokens"],
                    )
                )
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
                with chat_placeholder:
                    with st.chat_message("assistant"):
                        st.markdown(response.text)
            except Exception as e:
                st.error(f"Lỗi tạo phản hồi: {str(e)}")

    if st.session_state.image and not prompt:
        st.warning("Vui lòng nhập câu hỏi để đi kèm với hình ảnh.")

else:
    st.warning("Vui lòng nhập Google API Key của bạn ở thanh bên để bắt đầu trò chuyện.")


if st.button("Xóa Lịch sử Trò chuyện"):
    st.session_state.messages = []
    st.session_state.image = None
    st.rerun()


if st.button("Xuất Lịch sử Trò chuyện"):
    chat_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
    st.download_button(
        label="Tải xuống Lịch sử Trò chuyện",
        data=chat_history,
        file_name="lich_su_tro_chuyen.txt",
        mime="text/plain"
    )


st.sidebar.title("Thông tin Mô hình")
st.sidebar.info(f"""
- Mô hình: {st.session_state.model_config['model_name']}
- Độ sáng tạo: {st.session_state.model_config['temperature']:.2f}
- Top P: {st.session_state.model_config['top_p']:.2f}
- Top K: {st.session_state.model_config['top_k']}
- Số token tối đa: {st.session_state.model_config['max_output_tokens']}
- Số lượng tin nhắn: {len(st.session_state.messages)}
""")


if st.sidebar.button("Xuất Cấu hình"):
    config_data = {
        "model_config": st.session_state.model_config,
        "system_prompt": st.session_state.system_prompt
    }
    st.sidebar.download_button(
        label="Tải xuống Cấu hình",
        data=json.dumps(config_data, indent=2),
        file_name="cau_hinh_mo_hinh.json",
        mime="application/json"
    )


uploaded_config = st.sidebar.file_uploader("Tải lên Cấu hình", type=["json"])
if uploaded_config:
    config_data = json.load(uploaded_config)
    st.session_state.model_config = config_data["model_config"]
    st.session_state.system_prompt = config_data["system_prompt"]
    st.sidebar.success("Đã tải cấu hình thành công!")
    st.rerun()