# India: rules that shape a provisional filing

Compiled October 2026 from the IP India site, the Patents Act 1970 and the Patents Rules 2003. Fees and some procedures change: check every amount on ipindia.gov.in on the day you file.

## What a provisional does

- It fixes your **priority date** for everything it describes. Anything not described gets no date from it.
- It needs **no claims**. It must describe the invention well enough for a skilled person to build it (enablement), with the variations you may want to claim later.
- Within **12 months** (no extension) you file the **complete specification** with claims and Form 5, or the provisional is abandoned.
- India is first to file and has **no general grace period**. Any public disclosure before the filing date can destroy novelty, including your own post, video, demo, talk or pushed repository.

## Who files

- The applicant can be you as a natural person. You pay the lowest official fees (the same as startups). Startup benefits need DPIIT recognition, which needs a company, LLP or registered partnership.
- **Only humans are inventors.** Name yourself; never name a tool or company as inventor, and do not credit an AI system in the filing.
- **File your own invention.** Acting for someone else before the Patent Office is reserved for registered patent agents. patent-kit is for inventors filing their own applications.
- Section 39: if you live in India, file in India first and wait **six weeks** before filing anywhere else (or get Form 25 permission).

## Which patent office

File with the branch for where the applicant lives, has a place of business, or where the invention originated (Patents Rules, rule 4). Choose it in the Jurisdiction field of Form 1.

| Office | States and union territories |
|---|---|
| **Mumbai** | Maharashtra, Gujarat, Madhya Pradesh, Goa, Chhattisgarh, Dadra and Nagar Haveli and Daman and Diu |
| **Delhi** | Delhi, Haryana, Punjab, Himachal Pradesh, Jammu and Kashmir, Ladakh, Rajasthan, Uttar Pradesh, Uttarakhand, Chandigarh |
| **Chennai** | Tamil Nadu, Karnataka, Kerala, Andhra Pradesh, Telangana, Puducherry, Lakshadweep |
| **Kolkata** | West Bengal, Bihar, Jharkhand, Odisha, Sikkim, Assam, Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Tripura, Andaman and Nicobar Islands |

## Patent or design?

A patent protects how something **works**; a design registration (Designs Act, 2000) protects how it **looks**. If the inventor describes appearance (material, texture, colour, styling, "premium", "sleek"), separate it: the provisional describes the mechanism, function and technical effect; appearance may deserve a separate design registration, which is outside this kit. Say this plainly at the start, before the interview.

## Format (Form 2 and drawings)

- A4, margins **4 cm top and left, 3 cm bottom and right**, numbered pages, readable font (12 pt, 1.5 spacing is safe).
- **Title:** at most **15 words**, plain, no trade marks, no fancy words.
- **Abstract:** at most **150 words**, starting with the title; on its own page. Optional with a provisional, but prepare it.
- **Drawings** (rule 15): separate A4 sheets, same margins, black lines, no colour, no dimensions, no descriptive text except labels and flowchart text, letters at least 0.32 cm high. Applicant's name **top left**, "Sheet N of M" **top right**, signature **bottom right**.
- Reference numerals in the drawings must match the description.
- The base fee covers **30 pages** (description + abstract + drawings) and 10 claims. Extra pages cost more.

## Software inventions: sections 3(k) and 3(n)

Section 3(k) excludes "a computer programme per se" and 3(n) "a presentation of information". A software invention is not excluded when it shows a **technical effect** or technical contribution (Ferid Allani v. Union of India, 2019; the CRI Guidelines). So:

- Claim and describe the **mechanism**, not the look or the business idea.
- State the **technical problem** and the **technical effects** plainly: less computation, lower latency, fewer errors, deterministic correctness, no reflow, less bandwidth, and so on.
- Expect the objection in examination; answer it by substance.

## Words and things to avoid

- Claims of benefit to a group of people without data.
- Trade marks used as names of techniques.
- Attribution of the idea to anyone other than the inventor.
- Anything you want to keep out (for example a separate invention you plan to file on its own): describe it only as context, or not at all.

## Fees (natural person, online; verify)

| Item | Fee |
|---|---|
| Form 1 with provisional specification, up to 30 pages and 10 claims | Rs 1,600 |
| Form 18, request for examination (within 31 months) | Rs 4,000 |
| Form 18A, expedited examination (eligible categories only) | Rs 8,000 |
| Form 9, early publication | Rs 2,500 |
| eSign (Aadhaar e-KYC with a provider such as eMudhra) | about Rs 250 a year |

## Deadlines

Run `python3 scripts/deadlines.py YYYY-MM-DD --esign-expiry YYYY-MM-DD` on the filing date and paste the table into the tracker.
