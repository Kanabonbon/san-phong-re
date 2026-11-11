---
name: mo-dashboard
description: Mở, tạo hoặc cập nhật dashboard "Săn Phòng Rẻ" — trang có form nhập điểm đến, ngày, số người, số phòng, tiền tệ, vị trí, tiện ích, yêu cầu thanh toán, rồi tự tìm chỗ ở rẻ nhất trên Booking.com và Airbnb, so giá Agoda. Dùng khi người dùng nói "mở dashboard Săn Phòng Rẻ", "tạo dashboard tìm khách sạn", "cập nhật dashboard Săn Phòng Rẻ", hoặc muốn tìm phòng bằng form thay vì chat.
---

# Mở / cập nhật dashboard Săn Phòng Rẻ

Dashboard là một trang Artifact trên claude.ai. Trang điều khiển trình duyệt tích hợp của app Claude desktop và hỏi Claude để đọc, chấm các chỗ ở. Hiện chỉ **chủ sở hữu** trang mới dùng được trình duyệt từ trang, nên mỗi người dùng cần **bản của riêng họ**. Skill này xuất bản bản đó.

Mã trang nằm ở `dashboard/index.html`, cạnh file SKILL.md này (trong thư mục gốc của skill).

## Điều kiện

- Cần công cụ **Artifact** (có trong app Claude desktop và Claude Code đã đăng nhập claude.ai). Nếu phiên này không có công cụ Artifact, nói với người dùng: "Dashboard cần mở từ app Claude desktop (tab Code). Bạn vẫn có thể tìm bằng chat với lệnh /tim-khach-san." rồi dừng.
- Dashboard chỉ **tìm được** khi người dùng mở trang trong **app Claude desktop**. Mở trên trình duyệt web thì chỉ xem được kết quả cũ.

## Các bước

1. **Tìm bản cũ (để giữ nguyên link):** gọi Artifact `action: "list"` và tìm artifact có tiêu đề **"Săn Phòng Rẻ"** của người dùng.
   - Có → đây là cập nhật: gọi `action: "read"` với `url` của nó trước, rồi ở bước 4 publish với `url` đó.
   - Không có → tạo mới.
2. **Đọc toàn bộ** `dashboard/index.html` của skill (bắt buộc đọc trước khi xuất bản file mình không tự viết).
3. **Chép file** vào thư mục scratchpad của phiên (hoặc thư mục làm việc nếu không có scratchpad), giữ tên `index.html`. Không sửa nội dung.
4. **Xuất bản** bằng Artifact (publish) với:
   - `file_path`: đường dẫn bản vừa chép
   - `url`: link bản cũ nếu có (bước 1)
   - `icon`: `"hotel"` (chỉ khi tạo mới)
   - `description`: "Tìm chỗ ở rẻ nhất đúng số người, số phòng và yêu cầu trên Booking.com và Airbnb, so giá Agoda."
   - `capabilities` (bắt buộc, đúng nguyên văn):
     ```json
     {"mcp": {"servers": [{"server": "host:claude_browser", "tools": ["preview_start", "navigate", "get_page_text", "find", "read_page"]}]}, "sample": {}}
     ```
5. **Báo cho người dùng**, ngắn gọn:
   - Link trang và lời khuyên **ghim** trang để mở nhanh (chỉ ghim khi họ đồng ý).
   - Lần đầu bấm **Tìm**, app sẽ hỏi quyền dùng trình duyệt và quyền hỏi Claude: chọn **Cho phép**.
   - Mỗi lượt tìm mất khoảng 1–3 phút và dùng hạn mức Claude của chính họ.
   - Agent chỉ tìm và so sánh, **không đặt phòng**.

## Lưu ý

- Không thêm, bớt hay sửa capability nào ngoài danh sách trên.
- Không chia sẻ trang công khai thay người dùng; việc chia sẻ do họ tự làm từ menu Share.
- Nếu publish báo xung đột phiên bản, đọc lại bản đang có rồi publish lại với `url` đó.
