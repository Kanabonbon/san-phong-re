# Stay Hunter

An assistant that finds the **hotel, guesthouse or homestay with the lowest total cost** for your exact group, rooms, dates and requirements — running inside Claude.

- Searches **Booking.com** and **Airbnb**, with an **Agoda** price check
- Checks every stay: enough rooms for the whole group, total price including taxes and fees, 24-hour front desk, prepay or pay at property, cash or card, free cancellation
- Filters by **location** (near a landmark, within 1/3/5 km) and **amenities** (parking, breakfast, kitchen, elevator…)
- Prices in **10 currencies** (USD by default), sortable by price, distance or rating
- If a source is blocked it switches to another one and says so in the report
- **Never books**: the agent only searches and compares; you follow the link to book

> Vietnamese version: install the `san-phong-re` plugin from the same marketplace.

## Requirements

- A **Claude** account (a plan that includes Claude Code)
- The **Claude desktop app** (macOS / Windows) — the agent uses the app's built-in browser to read booking sites
- Each search uses your own Claude usage and takes about 1–3 minutes

## Install

Run these two commands in a terminal (Claude Code must be installed):

```bash
claude plugin marketplace add Kanabonbon/san-phong-re
```

```bash
claude plugin install stay-hunter@san-phong-re
```

Restart the Claude desktop app so the plugin loads.

## Use

**Option 1 — Dashboard (recommended):** in the Claude desktop app, **Code** tab, type:

> Open the Stay Hunter dashboard

Claude creates your own dashboard page. Pin it; from then on, open the page, fill in the form, press **Find cheapest stay** and confirm your criteria. The first time, choose **Allow** when the app asks to let the page use the browser and ask Claude.

**Option 2 — Chat:** describe what you need, for example:

> /find-stay Bangkok, Dec 20–22, 4 adults, 2 rooms, 24-hour front desk, pay at the property in cash

## Update

```bash
claude plugin marketplace update san-phong-re
```

```bash
claude plugin update stay-hunter@san-phong-re
```

Then in the Claude app type "Update the Stay Hunter dashboard" so your dashboard gets the new version (same link).

## Uninstall

```bash
claude plugin uninstall stay-hunter@san-phong-re
```

## Limitations

- The agent reads websites the way a person does, so it can break when sites change their layout, and it can be blocked if it searches too much.
- Agoda is used only as a price check (lowest price per room per night, before taxes and fees).
- Airbnb is always paid online, so it is skipped automatically when you need pay-at-property or cash.
- The dashboard reads the Vietnamese-language versions of the booking sites internally (that path is the tested one) and shows everything in English; its "View & book" links open the English sites.
- Prices change constantly — always check again on the booking site before you book.

## Disclaimer

For **personal use at low volume**. Booking.com, Airbnb and Agoda restrict automated access in their terms; you are responsible for complying with those terms. The tool never books, never signs in and never enters payment details. Results are for reference only; the author is not responsible for prices, availability or booking decisions.

Not affiliated with Booking.com, Airbnb, Agoda or Anthropic.

## License

[MIT](LICENSE)
