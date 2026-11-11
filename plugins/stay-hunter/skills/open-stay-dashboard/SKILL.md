---
name: open-stay-dashboard
description: Open, create or update the "Stay Hunter" dashboard — a page with a form for destination, dates, guests, rooms, currency, location, amenities and payment requirements that searches Booking.com and Airbnb for the cheapest qualifying stay and price-checks Agoda. Use when the user says "open the Stay Hunter dashboard", "create a hotel search dashboard", "update the Stay Hunter dashboard", or wants to search with a form instead of chat.
---

# Open / update the Stay Hunter dashboard

The dashboard is an Artifact page on claude.ai. It drives the Claude desktop app's built-in browser and asks Claude to read and score each stay. For now only the page's **owner** can use the browser from the page, so every user needs **their own copy**. This skill publishes that copy.

The page source is `dashboard/index.html`, next to this SKILL.md (in the skill's base directory).

## Requirements

- The **Artifact** tool must be available (Claude desktop app, or Claude Code signed in to claude.ai). If this session has no Artifact tool, tell the user: "The dashboard has to be opened from the Claude desktop app (Code tab). You can still search by chat with /find-stay." and stop.
- The dashboard can only **search** when the user opens the page in the **Claude desktop app**. In a regular web browser it can only show past results.

## Steps

1. **Look for an existing copy (to keep its link):** call Artifact `action: "list"` and look for the user's artifact titled **"Stay Hunter"**.
   - Found → this is an update: call `action: "read"` on its `url` first, then publish to that `url` in step 4.
   - Not found → create a new one.
2. **Read the whole** `dashboard/index.html` from this skill (required before publishing a file you didn't write).
3. **Copy the file** into this session's scratchpad directory (or the working directory if there is no scratchpad), keeping the name `index.html`. Don't change its content.
4. **Publish** with Artifact (publish):
   - `file_path`: the copy you just made
   - `url`: the existing copy's link, if any (step 1)
   - `icon`: `"hotel"` (only when creating)
   - `description`: "Find the cheapest stay that fits your group, rooms and requirements on Booking.com and Airbnb, with an Agoda price check."
   - `capabilities` (required, exactly as written):
     ```json
     {"mcp": {"servers": [{"server": "host:claude_browser", "tools": ["preview_start", "navigate", "get_page_text", "find", "read_page"]}]}, "sample": {}}
     ```
5. **Tell the user**, briefly:
   - The page link, and suggest **pinning** it for quick access (pin only if they agree).
   - The first time they press **Search**, the app asks to let the page use the browser and ask Claude: choose **Allow**.
   - Each search takes about 1–3 minutes and uses their own Claude usage.
   - Prices default to **USD**; any of 10 currencies can be chosen in the search bar.
   - The agent only searches and compares; it **never books**.

## Notes

- Don't add, remove or change any capability beyond the list above.
- Don't share the page publicly on the user's behalf; sharing is theirs to do from the Share menu.
- If publishing reports a version conflict, read the current version and publish again to that `url`.
- The page reads the Vietnamese-language versions of the booking sites internally (the tested path) but shows everything in English and its "View & book" links open the English sites.
