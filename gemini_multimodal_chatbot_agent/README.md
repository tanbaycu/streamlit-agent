# Trò chuyện Đa phương tiện với Gemini 🚀

Ứng dụng Streamlit này cho phép bạn trải nghiệm sức mạnh của các mô hình Gemini mới nhất với tùy chỉnh nâng cao. Tương tác với AI thông qua văn bản và hình ảnh, đồng thời tùy chỉnh các tham số mô hình để có trải nghiệm tối ưu.

## Tính năng chính

- 🤖 Tương tác với các mô hình Gemini mới nhất
- 🖼️ Hỗ trợ tải lên và phân tích hình ảnh
- ⚙️ Tùy chỉnh nâng cao các tham số mô hình
- 💬 Lưu trữ và xuất lịch sử trò chuyện
- 🔧 Tùy chỉnh system prompt
- 📊 Xuất và nhập cấu hình mô hình

## Cài đặt

1. Clone repository này:
```bash
git clone https://github.com/tanbaycu/streamlit-agent.git
cd streamlit-agent/gemini_multimodal_chatbot_agent
```
2. Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```
3. Chạy mã
```bash 
streamlit run gemini_multimodal_chatbot_agent.py
```

---

## Hướng dẫn sử dụng

### 1. Cài đặt API Key

- Nhập Google API Key của bạn vào ô "Nhập Google API Key" trong thanh bên.

### 2. Tùy chỉnh Mô hình

- Chọn mô hình Gemini từ danh sách có sẵn.
- Điều chỉnh các tham số:
- Độ sáng tạo (Temperature)
- Top P
- Top K
- Số token tối đa

### 3. Tùy chỉnh Prompt

- Chỉnh sửa System Prompt để định hướng hành vi của AI.

### 4. Tải lên Hình ảnh

- Tải lên hình ảnh để phân tích hoặc thảo luận.

### 5. Trò chuyện

- Nhập câu hỏi hoặc yêu cầu của bạn vào ô chat.
- Xem phản hồi của AI trong khung chat.

### 6. Quản lý Lịch sử Trò chuyện

- Xóa lịch sử trò chuyện bằng nút "Xóa Lịch sử Trò chuyện".
- Xuất lịch sử trò chuyện bằng nút "Xuất Lịch sử Trò chuyện".

### 7. Quản lý Cấu hình

- Xuất cấu hình hiện tại bằng nút "Xuất Cấu hình".
- Tải lên cấu hình đã lưu để áp dụng nhanh các tùy chỉnh.

## Các mô hình Gemini hỗ trợ

- gemini-1.5-flash-latest
- gemini-2.0-flash-exp
- gemini-1.5-flash-8b
- gemini-2.0-pro-exp-02-05
- gemini-2.0-flash-lite-preview-02-05

## Lưu ý

- Đảm bảo bạn có đủ quota và quyền truy cập cho API key của Google.
- Một số mô hình có thể yêu cầu quyền truy cập đặc biệt hoặc đang trong giai đoạn thử nghiệm.

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng tạo issue hoặc pull request nếu bạn có bất kỳ cải tiến hoặc tính năng mới nào.



