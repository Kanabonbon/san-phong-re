# Nguồn tìm kiếm và nơi kiểm tra tiêu chí

Các mẫu link dưới đây dùng để mở nhanh trang kết quả. Trang đặt phòng hay đổi tham số — **luôn kiểm tra trang hiển thị đúng ngày/số người/số phòng**; nếu sai thì nhập tay vào form tìm kiếm.

Quy ước: ngày dạng `YYYY-MM-DD`; địa điểm mã hoá URL (dấu cách → `+` hoặc `%20`).

---

## Booking.com (VN + quốc tế)

**Link tìm kiếm:**
```
https://www.booking.com/searchresults.vi.html?ss={DIA_DIEM}&checkin={NGAY_NHAN}&checkout={NGAY_TRA}&group_adults={NGUOI_LON}&no_rooms={SO_PHONG}&group_children={SO_TRE}&order=price
```
- Có trẻ em: thêm `&age={TUOI}` cho mỗi trẻ (ví dụ 2 trẻ 6 và 9 tuổi: `&group_children=2&age=6&age=9`).
- `order=price` = sắp xếp giá thấp nhất. Nếu không có hiệu lực, chọn "Sắp xếp theo: Giá (ưu tiên thấp nhất)".
- Đổi `.vi.html` thành `.html` nếu muốn tiếng Anh.

**Bộ lọc — đưa thẳng vào link bằng `&nflt=` (đã kiểm chứng 11/2026, nhanh hơn bấm chuột):**
| Bộ lọc | Mã |
|---|---|
| Lễ tân 24 giờ | `hotelfacility=8` |
| Không cần thanh toán trước | `fc=5` |
| Miễn phí hủy | `fc=2` |
| Trong vòng 1 / 3 / 5 km (tính từ địa điểm trong `ss`) | `distance=1000` / `3000` / `5000` |
| Chỗ đỗ xe | `hotelfacility=2` |
| WiFi miễn phí | `hotelfacility=107` |
| Hồ bơi | `hotelfacility=433` |
| Bao gồm bữa sáng | `mealplan=1` |
| Tự nấu (có bếp) | `mealplan=999` |
| Phòng tắm riêng | `roomfacility=38` |
| Thang máy | `accessible_room_facilities=132` |

**Tìm gần một địa điểm:** đặt `ss={DIA_DANH}, {THANH_PHO}` (vd `ss=Chợ Đà Lạt, Đà Lạt`). Mỗi thẻ kết quả sẽ ghi "cách 450m từ Chợ Đà Lạt"; không đặt thì thẻ ghi "Cách trung tâm …".

Nhiều mã nối bằng `;` và mã hoá URL, ví dụ: `&nflt=hotelfacility%3D8%3Bfc%3D5`. Nếu mã không còn đúng: chạy JS liệt kê `input[type=checkbox]` (thuộc tính `name`/`value` + `aria-label`) trên trang kết quả để lấy mã mới.

**Đọc nhanh danh sách kết quả bằng JS:** mỗi chỗ nghỉ là `[data-testid="property-card"]`; tên `[data-testid="title"]`; link `a[data-testid="title-link"]`; phòng gợi ý `[data-testid="recommended-units"]`; tổng tiền là dòng chứa "Tổng cộng" trong thẻ (đã gồm thuế phí, cho cả kỳ ở và tất cả các phòng).

**Cẩn thận sức chứa:** kết quả rẻ nhất hay là phòng tập thể/giường tầng hoặc "Phòng 4 người" (1 phòng) — không đạt nếu người dùng cần đúng số phòng. Kiểm tra dòng "2 × ..." trong phòng gợi ý.

**Kiểm tra ở trang chi tiết:**
- Tổng tiền: bảng phòng → cột giá cho số đêm, dòng "Đã bao gồm thuế và phí" / "+ thuế và phí".
- Lễ tân 24 giờ: mục "Tiện nghi" → "Dịch vụ lễ tân".
- Trả trước / tại chỗ: trong bảng phòng từng gói ghi "Không cần thanh toán trước" hoặc "Thanh toán trước".
- Thẻ / tiền mặt: mục "Quy tắc chung" / "Điều cần biết" → "Thẻ được chấp nhận ở chỗ nghỉ này", "Chỉ thanh toán bằng tiền mặt".
- Huỷ: từng gói ghi "Miễn phí hủy trước {ngày}".

---

## Agoda (mạnh ở Việt Nam & châu Á)

**Link tìm kiếm — cần mã thành phố `city=`** (link chỉ có `textToSearch` sẽ bị chuyển về trang chủ):
```
https://www.agoda.com/vi-vn/search?city={MA_TP}&checkIn={NGAY_NHAN}&checkOut={NGAY_TRA}&los={SO_DEM}&rooms={SO_PHONG}&adults={NGUOI_LON}&children={SO_TRE}&childAges={TUOI1},{TUOI2}&currency=VND&sort=priceLowToHigh
```
Mã thành phố đã biết: Đà Lạt `15932`. Chưa biết mã: mở trang chủ Agoda, gõ địa điểm, chọn gợi ý thành phố, bấm TÌM, rồi đọc tham số `city=` trong URL kết quả và ghi thêm vào đây.

**Bộ lọc — thêm vào link (đã kiểm chứng 11/2026):**
| Bộ lọc | Mã |
|---|---|
| Thanh toán tại nơi ở | `paymentOptions=56649` |
| Bàn tiếp tân [24 giờ] | `hotelFacility=116` |

**Giá trên danh sách Agoda là giá MỖI PHÒNG MỖI ĐÊM, CHƯA gồm thuế phí** → tổng ≈ giá × số phòng × số đêm + thuế phí (thường ~8–15%). Giá rất thấp (dưới ~100.000 ₫) thường là giá một giường phòng tập thể — mở trang chi tiết xem có lựa chọn đúng số phòng không.

Danh sách tải dần khi cuộn: cuộn từng đoạn rồi mới đọc. Mỗi chỗ nghỉ là `li[data-hotelid]`; link chi tiết là `/vi-vn/accom/property?propertyId=...` kèm ngày/số người.

**Kiểm tra ở trang chi tiết:**
- Tổng tiền: chọn số phòng trong bảng giá → xem tổng ở khung đặt phòng (chưa cần bấm đặt).
- Lễ tân 24 giờ: mục "Tiện nghi và cơ sở vật chất" → "Dịch vụ".
- Thanh toán: nhãn từng gói "Thanh toán tại nơi ở", "Trả sau", "Thanh toán ngay"; mục "Chính sách" có thể ghi phương thức thanh toán được chấp nhận.

---

**Tra mã thành phố / mã chỗ nghỉ không cần bấm (API gợi ý, trả JSON đọc được bằng `get_page_text`):**
```
https://www.agoda.com/api/cronos/search/GetUnifiedSuggestResult/3/24/24/0/vi-vn/?searchText={TEN}&origin=VN&cid=-1&pageTypeId=1
```
Trong `ViewModelList`: phần tử thành phố có `ObjectTypeId: 1` và `CityId`; phần tử chỗ nghỉ có `IsHotel: true`, `ObjectId` = propertyId. Trang chỗ nghỉ: `/vi-vn/accom/property?propertyId={ID}&finalPriceView=1&adults=..&rooms=..&checkIn=..&los=..&currencyCode=VND`. Sau ~5–10 giây, nút "từ X ₫ Xem giá" (tìm bằng `find "Xem giá"`) cho giá thấp nhất/phòng/đêm chưa thuế.

**Hạn chế (11/2026):** danh sách kết quả và bảng phòng của Agoda chỉ tải khi khung trình duyệt đang hiện trên màn hình. Khi khung bị ẩn, chỉ 3 chỗ đầu có giá, và `scroll_to` không kích hoạt được phần tải thêm. Dashboard vì vậy chỉ dùng Agoda để so giá các chỗ đã chọn từ Booking.

## Airbnb (nhà, căn hộ, phòng trong nhà dân)

**Link tìm kiếm (nhận tên địa điểm trực tiếp):**
```
https://www.airbnb.com.vn/s/{DIA_DIEM}/homes?checkin={NGAY_NHAN}&checkout={NGAY_TRA}&adults={NGUOI_LON}&children={SO_TRE}&min_bedrooms={SO_PHONG}&currency=VND
```
- Không có sắp xếp theo giá → đọc hết thẻ trên trang (~18) rồi tự chọn rẻ nhất.
- Đọc bằng `read_page` (filter all): mỗi chỗ ở là một khối `group` có link `/rooms/{ID}`, loại chỗ ở ("Căn hộ tại …"), số phòng ngủ, giường, đánh giá (thang 5), **"X ₫ cho N đêm" = tổng cả kỳ ở đã gồm mọi khoản phí**, và "Hủy miễn phí" nếu có. `get_page_text` chỉ ra tiêu đề, không dùng được.
- Trang chi tiết `/rooms/{ID}` không tải nội dung khi khung trình duyệt ẩn.
- Quy định cố định: luôn thanh toán online qua Airbnb (thẻ / ví) → không đạt "trả tại chỗ" và "tiền mặt"; đạt "trả trước" và "thẻ tín dụng". Không có lễ tân, thường tự nhận phòng → lễ tân 24/24 để "chưa rõ".

## Đã thử, không dùng được
- **Google Hotels** (`google.com/travel/search?...&checkin=&checkout=`): không nhận ngày qua link, báo "Không có kết quả".
- **Expedia** (`expedia.com.vn/Hotel-Search?...`): trả về trang chặn bot (HTTP 429, "Hãy thể hiện mình là con người"). Không vượt.

## Traveloka (Việt Nam, Đông Nam Á)

Link tham số không ổn định → mở `https://www.traveloka.com/vi-vn/hotel` rồi nhập tay: địa điểm, ngày nhận/trả, số khách, số phòng.

Sau khi có kết quả: "Sắp xếp" → "Giá thấp nhất". Bộ lọc: "Thanh toán tại khách sạn", "Miễn phí hủy phòng", "Lễ tân 24h" (Tiện nghi).

Kiểm tra: trang chi tiết → "Tiện nghi" và "Chính sách", nhãn gói phòng "Thanh toán tại khách sạn".

---

## Google Hotels (quốc tế; tổng hợp giá nhiều trang)

**Link:**
```
https://www.google.com/travel/search?q=hotels+in+{DIA_DIEM}&hl=vi
```
Sau khi mở: đặt ngày nhận/trả và số khách trên thanh trên cùng; "Sắp xếp theo" → "Giá thấp nhất". Bật hiển thị "Tổng giá" (gồm thuế phí) nếu có.

Dùng Google Hotels để **so sánh giá giữa các trang đặt phòng** cho cùng một khách sạn. Tiện nghi (lễ tân 24 giờ) thường có ở tab "Giới thiệu"; còn **chính sách thanh toán thì phải mở trang đặt phòng gốc** (Booking/Agoda/website khách sạn) để kiểm tra.

---

## Bảng tra nhanh: từ khoá theo tiêu chí

| Tiêu chí | Tiếng Việt | Tiếng Anh |
|---|---|---|
| Lễ tân 24/24 | Lễ tân 24 giờ, Quầy lễ tân 24/7 | 24-hour front desk |
| Trả tại chỗ | Không cần thanh toán trước, Thanh toán tại chỗ nghỉ / tại khách sạn | No prepayment needed, Pay at the property |
| Trả trước | Thanh toán trước, Thanh toán ngay | Prepayment, Pay now |
| Thẻ tín dụng | Thẻ được chấp nhận, Visa, Mastercard | Cards accepted at this property |
| Tiền mặt | Tiền mặt, Chỉ nhận tiền mặt | Cash, Cash only |
| Huỷ miễn phí | Miễn phí hủy | Free cancellation |
| Không hoàn tiền | Không hoàn tiền | Non-refundable |
