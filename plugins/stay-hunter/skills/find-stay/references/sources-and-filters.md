# Search sources and where to check each requirement

The link templates below open result pages quickly. Booking sites change their parameters — **always check that the page shows the right dates, guests and rooms**; if not, type into the search form instead.

Conventions: dates as `YYYY-MM-DD`; place names URL-encoded (space → `+` or `%20`). Verified November 2026.

---

## Booking.com (worldwide)

**Search link:**
```
https://www.booking.com/searchresults.en-gb.html?ss={DESTINATION}&checkin={CHECKIN}&checkout={CHECKOUT}&group_adults={ADULTS}&no_rooms={ROOMS}&group_children={CHILDREN}&order=price&selected_currency={CURRENCY}
```
- With children: add `&age={AGE}` per child (e.g. two children aged 6 and 9: `&group_children=2&age=6&age=9`).
- `order=price` = lowest price first. If it doesn't apply, choose "Sort by: Price (lowest first)".
- `selected_currency=USD` (or any ISO code) sets the currency.

**Filters — put them straight into the link with `&nflt=` (faster and more reliable than clicking):**
| Filter | Code |
|---|---|
| 24-hour front desk | `hotelfacility=8` |
| No prepayment needed | `fc=5` |
| Free cancellation | `fc=2` |
| Within 1 / 3 / 5 km (of the place in `ss`) | `distance=1000` / `3000` / `5000` |
| Parking | `hotelfacility=2` |
| Free WiFi | `hotelfacility=107` |
| Swimming pool | `hotelfacility=433` |
| Breakfast included | `mealplan=1` |
| Self-catering (kitchen) | `mealplan=999` |
| Private bathroom | `roomfacility=38` |
| Elevator | `accessible_room_facilities=132` |

Join several codes with `;` and URL-encode, e.g. `&nflt=hotelfacility%3D8%3Bfc%3D5`. If a code stops working, run JavaScript on the results page to list every `input[type=checkbox]` (`name`/`value` + `aria-label`) and read the new codes.

**Search near a landmark:** set `ss={LANDMARK}, {CITY}` (e.g. `ss=Ben Thanh Market, Ho Chi Minh City`). Each result card then shows "X km from {landmark}"; without it, cards show the distance from the center.

**Read the result list fast with JavaScript:** each property is `[data-testid="property-card"]`; name `[data-testid="title"]`; link `a[data-testid="title-link"]`; suggested rooms `[data-testid="recommended-units"]`; the total is the line containing "Total" (or "Tổng cộng" on the Vietnamese site) — it includes taxes and fees, for the whole stay and all rooms.

**Watch capacity:** the cheapest results are often dorm beds / bunk beds, or a single "Quadruple Room" — these fail when the user needs a specific number of rooms. Check the "2 × …" line in the suggested rooms.

**On the detail page:**
- Total: room table → price column for the stay, "Includes taxes and charges" / "+ taxes and charges".
- 24-hour front desk: "Facilities" → "Front desk services".
- Prepay / pay at property: each rate says "No prepayment needed" or "Prepayment".
- Cards / cash: "House rules" / "The fine print" → "Cards accepted at this property", "Cash only".
- Cancellation: each rate says "Free cancellation before {date}".

---

## Airbnb (homes, apartments, private rooms)

**Search link (accepts a place name directly):**
```
https://www.airbnb.com/s/{DESTINATION}/homes?checkin={CHECKIN}&checkout={CHECKOUT}&adults={ADULTS}&children={CHILDREN}&min_bedrooms={ROOMS}&currency={CURRENCY}
```
- No sort-by-price option → read every card on the page (~18) and pick the cheapest yourself.
- Read with `read_page` (filter all): each listing is a `group` block with a `/rooms/{ID}` link, the listing type ("Apartment in …"), bedrooms, beds, rating (out of 5), **"X for N nights" = the all-in total for the stay**, and "Free cancellation" when offered. `get_page_text` only returns the heading here.
- Listing pages `/rooms/{ID}` don't load their content while the browser pane is hidden.
- Fixed rules: always paid online through Airbnb (card / wallet) → fails "pay at property" and "cash"; meets "prepay" and "credit card". No front desk, usually self check-in → mark 24-hour front desk as ❓.

---

## Agoda (strong in Asia) — best used as a price check

**Find a city or property id without clicking (suggest API, returns JSON readable with `get_page_text`):**
```
https://www.agoda.com/api/cronos/search/GetUnifiedSuggestResult/3/24/24/0/vi-vn/?searchText={NAME}&origin=VN&cid=-1&pageTypeId=1
```
(Tested with the `vi-vn` locale shown above; the JSON fields are the same whatever the display language.) In `ViewModelList`: a city has `ObjectTypeId: 1` and `CityId`; a property has `IsHotel: true` and `ObjectId` = propertyId.

**Property page:**
```
https://www.agoda.com/en-us/accom/property?propertyId={ID}&finalPriceView=1&adults={ADULTS}&children={CHILDREN}&rooms={ROOMS}&checkIn={CHECKIN}&los={NIGHTS}&currencyCode={CURRENCY}
```
After ~5–10 seconds the "from X … View prices" button (find it with `find`) gives the lowest price per room per night, **before taxes and fees**.

**City search (needs `city=`; a link with only `textToSearch` redirects to the home page):**
```
https://www.agoda.com/en-us/search?city={CITY_ID}&checkIn={CHECKIN}&checkOut={CHECKOUT}&los={NIGHTS}&rooms={ROOMS}&adults={ADULTS}&children={CHILDREN}&currency={CURRENCY}&sort=priceLowToHigh
```
Filters: pay at property `paymentOptions=56649`, 24-hour front desk `hotelFacility=116`. Known city id: Da Lat `15932`.

**Limits:** Agoda list prices are **per room per night, before taxes and fees** → total ≈ price × rooms × nights + taxes/fees (often ~8–15%). Very low prices are often a single dorm bed. The results list and room tables only load while the browser pane is on screen; when hidden, only the first ~3 results have prices and `scroll_to` doesn't trigger loading. That's why the dashboard uses Agoda only to price-check the Booking shortlist.

---

## Traveloka (Southeast Asia)

Link parameters are unstable → open `https://www.traveloka.com/en-en/hotel` and type destination, dates, guests and rooms. Then "Sort" → "Lowest price". Filters: "Pay at hotel", "Free cancellation", "24-hour front desk". Check the detail page's "Facilities" and "Policies".

---

## Tried, not usable
- **Google Hotels** (`google.com/travel/search?...&checkin=&checkout=`): ignores dates passed in the link and shows "No results".
- **Expedia** (`expedia.com/Hotel-Search?...`): returns a bot-block page (HTTP 429, "Are you a human?"). Do not try to get past it.

---

## Keyword cheat sheet

| Requirement | English | Vietnamese (if the site shows Vietnamese) |
|---|---|---|
| 24-hour front desk | 24-hour front desk | Lễ tân 24 giờ |
| Pay at property | No prepayment needed, Pay at the property | Không cần thanh toán trước, Thanh toán tại chỗ nghỉ |
| Prepay | Prepayment, Pay now | Thanh toán trước |
| Credit card | Cards accepted at this property | Thẻ được chấp nhận |
| Cash | Cash, Cash only | Tiền mặt, Chỉ thanh toán bằng tiền mặt |
| Free cancellation | Free cancellation | Miễn phí hủy |
| Non-refundable | Non-refundable | Không hoàn tiền |
| Total price | Total, includes taxes and charges | Tổng cộng, đã bao gồm thuế và phí |
