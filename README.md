# Săn Phòng Rẻ · Stay Hunter

**🇬🇧 English:** this repository also contains **Stay Hunter**, the English version of the plugin. Install it with `claude plugin marketplace add Kanabonbon/san-phong-re` then `claude plugin install stay-hunter@san-phong-re`. Full guide: [plugins/stay-hunter/README.md](plugins/stay-hunter/README.md).

**🇻🇳 Tiếng Việt:** bản tiếng Việt là plugin `san-phong-re`, hướng dẫn bên dưới.

---

Trợ lý tìm **khách sạn, nhà nghỉ, homestay có tổng chi phí rẻ nhất** đúng số người, số phòng, ngày ở và yêu cầu của bạn — chạy trong Claude.

- Tìm trên **Booking.com** và **Airbnb**, so giá với **Agoda**
- Kiểm tra từng chỗ: đủ phòng cho cả nhóm, tổng tiền đã gồm thuế phí, lễ tân 24/24, trả trước hay trả tại chỗ, tiền mặt hay thẻ, huỷ miễn phí
- Lọc theo **vị trí** (gần một địa điểm, trong vòng 1/3/5 km) và **tiện ích** (đỗ xe, bữa sáng, bếp, thang máy…)
- Báo giá theo **10 loại tiền** (mặc định VND), sắp xếp theo giá, khoảng cách, đánh giá
- Nguồn nào bị chặn thì tự chuyển sang nguồn khác và ghi rõ trong báo cáo
- **Không đặt phòng**: agent chỉ tìm và so sánh, bạn tự bấm link để đặt

## Yêu cầu

- Tài khoản **Claude** (gói có Claude Code)
- **App Claude desktop** (macOS / Windows) — trình duyệt tích hợp của app là thứ agent dùng để đọc các trang đặt phòng
- Mỗi lượt tìm dùng hạn mức Claude của chính bạn, mất khoảng 1–3 phút

## Cài đặt

Chạy 2 lệnh trong Terminal (cần đã cài Claude Code):

```bash
claude plugin marketplace add Kanabonbon/san-phong-re
```

```bash
claude plugin install san-phong-re@san-phong-re
```

Mở lại app Claude desktop để plugin được nạp.

## Sử dụng

**Cách 1 — Dashboard (khuyên dùng):** trong app Claude desktop, tab **Code**, gõ:

> Mở dashboard Săn Phòng Rẻ

Claude tạo cho bạn một trang dashboard riêng. Ghim trang lại, sau đó mỗi lần cần tìm chỉ việc mở trang, điền form, bấm **Tìm** và xác nhận tiêu chí. Lần đầu tìm, chọn **Cho phép** khi app hỏi quyền dùng trình duyệt và quyền hỏi Claude.

**Cách 2 — Chat:** gõ yêu cầu bằng lời, ví dụ:

> /tim-khach-san Đà Lạt, 20–22/12, 4 người lớn, 2 phòng, cần lễ tân 24/24, trả tiền mặt tại chỗ

## Cập nhật

```bash
claude plugin marketplace update san-phong-re
```

```bash
claude plugin update san-phong-re@san-phong-re
```

Sau đó trong app Claude gõ "Cập nhật dashboard Săn Phòng Rẻ" để dashboard của bạn nhận bản mới (giữ nguyên link).

## Gỡ cài đặt

```bash
claude plugin uninstall san-phong-re@san-phong-re
```

## Hạn chế

- Agent đọc trang web như người dùng, nên có thể hỏng khi các trang đổi giao diện, và có thể bị chặn nếu tìm quá nhiều.
- Agoda chỉ dùng để so giá (giá thấp nhất mỗi phòng mỗi đêm, chưa gồm thuế phí).
- Airbnb luôn thanh toán online, nên tự bị bỏ qua khi bạn cần trả tại chỗ hoặc tiền mặt.
- Giá thay đổi liên tục — luôn kiểm tra lại trên trang đặt phòng trước khi đặt.

## Miễn trừ trách nhiệm

Công cụ dành cho **mục đích cá nhân, lượng tìm kiếm ít**. Booking.com, Airbnb, Agoda có điều khoản hạn chế việc tự động truy cập; người dùng tự chịu trách nhiệm tuân thủ điều khoản của các trang này. Công cụ không đặt phòng, không đăng nhập, không nhập thông tin thanh toán. Kết quả chỉ mang tính tham khảo; tác giả không chịu trách nhiệm về giá, tình trạng phòng hay quyết định đặt phòng.

Dự án không liên kết với Booking.com, Airbnb, Agoda hay Anthropic.

## Giấy phép

[MIT](LICENSE)
