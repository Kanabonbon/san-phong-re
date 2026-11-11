# Săn Phòng Rẻ · Stay Hunter

**🇻🇳 Tiếng Việt** bên dưới · **🇬🇧 [English](#english)**

Dashboard có nút **VI | EN** ở góc trên bên phải để chọn ngôn ngữ hiển thị. / The dashboard has a **VI | EN** switch in the top-right corner.

---

Trợ lý tìm **khách sạn, nhà nghỉ, homestay có tổng chi phí rẻ nhất** đúng số người, số phòng, ngày ở và yêu cầu của bạn — chạy trong Claude.

- Tìm trên **Booking.com** và **Airbnb**, so giá với **Agoda**
- Kiểm tra từng chỗ: đủ phòng cho cả nhóm, tổng tiền đã gồm thuế phí, lễ tân 24/24, trả trước hay trả tại chỗ, tiền mặt hay thẻ, huỷ miễn phí
- Lọc theo **vị trí** (gần một địa điểm, trong vòng 1/3/5 km) và **tiện ích** (đỗ xe, bữa sáng, bếp, thang máy…)
- Báo giá theo **10 loại tiền** (mặc định VND), sắp xếp theo giá, khoảng cách, đánh giá
- Giao diện **tiếng Việt hoặc tiếng Anh** (nút VI | EN)
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

## Bạn đã cài bản tiếng Anh `stay-hunter` trước đây?

Bản đó đã được gộp vào `san-phong-re`. Gỡ bản cũ rồi cài bản chung:

```bash
claude plugin uninstall stay-hunter@san-phong-re
```

```bash
claude plugin install san-phong-re@san-phong-re
```

## Sửa dashboard (cho người phát triển)

Mã nguồn ở `dashboard-src/`: `vi.html` và `en.html` cùng cấu trúc, khác chữ. Sửa cả hai rồi chạy `python3 dashboard-src/build.py` để tạo trang song ngữ `plugins/san-phong-re/skills/mo-dashboard/dashboard/index.html`.

## Miễn trừ trách nhiệm

Công cụ dành cho **mục đích cá nhân, lượng tìm kiếm ít**. Booking.com, Airbnb, Agoda có điều khoản hạn chế việc tự động truy cập; người dùng tự chịu trách nhiệm tuân thủ điều khoản của các trang này. Công cụ không đặt phòng, không đăng nhập, không nhập thông tin thanh toán. Kết quả chỉ mang tính tham khảo; tác giả không chịu trách nhiệm về giá, tình trạng phòng hay quyết định đặt phòng.

Dự án không liên kết với Booking.com, Airbnb, Agoda hay Anthropic.

## Giấy phép

[MIT](LICENSE)

---

<a id="english"></a>
## English

An assistant that finds the **hotel, guesthouse or homestay with the lowest total cost** for your exact group, rooms, dates and requirements (24-hour front desk, prepay or pay at property, cash or card, location, amenities). It searches **Booking.com** and **Airbnb** with an **Agoda** price check, and it **never books**.

**Install** (Claude Code required):

```bash
claude plugin marketplace add Kanabonbon/san-phong-re
```

```bash
claude plugin install san-phong-re@san-phong-re
```

Restart the Claude desktop app. In the **Code** tab, type "Open the Stay Hunter dashboard" (or "Mở dashboard Săn Phòng Rẻ"), then press **EN** in the top-right corner of the page. Prices can be shown in 10 currencies. You can also search by chat, e.g. `/tim-khach-san Bangkok, Dec 20–22, 4 adults, 2 rooms, 24-hour front desk, pay at the property in cash`; the agent replies in English.

Previously installed `stay-hunter`? It is now part of `san-phong-re`: run `claude plugin uninstall stay-hunter@san-phong-re`, then install as above.

For personal, low-volume use; you are responsible for complying with the booking sites' terms. Not affiliated with Booking.com, Airbnb, Agoda or Anthropic. License: [MIT](LICENSE).
