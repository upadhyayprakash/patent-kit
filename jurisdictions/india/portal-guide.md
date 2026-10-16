# India: filing the provisional on the IP India portal, field by field

Written from a real self-filing in October 2026. Screens change; when one looks different, ask Claude with a screenshot (hide personal numbers).

## Phase 4: accounts (any time before filing)

1. **eSign.** On the provider's site (for example eMudhra), choose an individual eSign plan (a one-year plan with about 100 signatures is plenty), verify with Aadhaar e-KYC and the OTP on your Aadhaar-linked mobile, and pay (about Rs 250 plus platform charges). Note the **name** as it appears on the certificate (your Aadhaar name) and the **expiry date**; put both in the tracker.
2. **Portal account.** Open the portal, choose new user registration, pick eSign as the signature type, and register with that exact name, your email and mobile. Check the **profile address** now: it is copied into Form 1 and may not be editable there.
3. **Email.** Verify your email when asked; uploads stay locked until you do.

## Before you start

- **Signing:** an **eSign** bought with Aadhaar e-KYC (for example eMudhra, about Rs 250 for a year of signatures) or a Class 3 DSC. eSign works on any OS and browser.
- **Name:** use your name **exactly** as on the ID behind your eSign (Aadhaar or PAN) on Form 1, Form 2, the drawings and Form 3. If the portal pre-fills a longer name than you used, regenerate your PDFs with it.
- **Portal:** `https://ipronline.ipindia.gov.in/epatentfiling/goForLogin/doLogin` (linked from ipindia.gov.in, Filing Process). Register a user with the eSign, then log in with user ID and password.
- **Pop-ups:** allow pop-ups for ipronline.ipindia.gov.in. Some buttons open new windows and do nothing when blocked.
- **Your profile address** is copied into the applicant row and may not be editable later. Check it in the profile before starting Form 1.
- **Files ready:** Form 2 PDF, drawings PDF, Form 3 PDF (optional now), plain-text copies of the abstract and description for the text boxes. `scripts/pagecount.py` gives the page counts.

## Form 1 (New Application)

| Field | Value |
|---|---|
| Jurisdiction | Your branch by state: see "Which patent office" in `rules.md` (for example Karnataka files with **Chennai**, Maharashtra with **Mumbai**) |
| Type of Application | **ORDINARY APPLICATION** (a first filing in India; it still allows a PCT filing within 12 months) |
| Type of Specification | **PROVISIONAL** |
| Description, no. of pages | specification pages minus the abstract page |
| Claims, pages and number | **0** and **0** |
| Abstract, no. of pages | **1** |
| Drawings, pages and number | one per sheet |
| Sequence listing | 0 |
| Priorities | 0; do not click Add Priorities |
| Title | exactly as in Form 2 |
| Address for service (India) | your postal address |
| Abstract, Description boxes | paste the plain text (used only for publication) |
| Claims box (mandatory) | `Nil. This is a provisional specification; claims will be filed with the complete specification.` (or `NA` if rejected) |
| Applicants | yourself, natural person (NP) |
| Inventors | tick **"Inventor(s) is/are same as Applicant(s)"** |

**Declarations:** keep only "The Provisional specification ... is filed with this application" plus the two the portal ticks itself (in possession of the invention; no lawful ground of objection). Leave biological material, assignee, convention, priority, PCT, divisional and addition unticked.

**Bundled forms:** none. Form 9 needs a complete specification; Form 18 comes later; Form 28 is for small entities and startups.

Tick the "true to my best knowledge" box and click **Save**. The draft gets a temporary number such as `TEMP/E-1/123456/2026-MUM` (the last part is the office). **Drafts are deleted after 30 days**, so finish within that time.

## Email verification

After Save, the portal emails a verification link. **Upload stays disabled until you click it** (check spam).

## Upload

Form History > Drafted Forms > select your row > **Upload**. The row also shows the **fee** (Rs 1,600 for an individual within 30 pages): check it before going on. Upload each file with its type:

| Document type | File |
|---|---|
| PROVISIONAL SPECIFICATION | Form 2 PDF |
| DRAWINGS | drawings PDF |
| STATEMENT OF UNDERTAKING (FORM 3) | Form 3 PDF (optional now; due within 6 months; adds no fee) |
| FORM 1 | the portal's own Form 1: Drafted Forms > **Preview**, then Print > Save as PDF (A4) |

The portal refuses to sign until Form 1 itself is uploaded. Documents must be under 20 MB, not password protected, and must not include PAN, Aadhaar or passport copies.

## Sign

Before you sign, check once more (nothing can be edited afterwards):
- Each uploaded file opens with **View Content** and is the right document.
- Name identical on Form 1, Form 2, drawings and Form 3, and as on your eSign.
- Title identical in Form 1 and Form 2.
- Page counts on Form 1 match `pagecount.py`; jurisdiction and fee are right.
- Only the provisional-specification declaration (plus the two automatic ones) is ticked.


**Proceed to Sign Documents** > eSign > OTP on the mobile linked to your Aadhaar. All uploaded documents are signed together. **After signing nothing can be edited**: check everything first.

## Pay

**Payments/Submission** > select the application > pay (Rs 1,600 for a natural person, online, up to 30 pages). The filing date is the date of the successful payment.

If the bank page returns a failure or a pending status:

- **Do not pay again straight away.** Open **Pending CBR** and use **Check payment status** after 60 minutes.
- Check your bank: if nothing was debited, retry; if it was debited, wait for the status to settle. A failure page **after** a debit often turns into a success at the status check, with the receipt.
- If money left your account and the status stays failed, write to **ipo-helpdesk@nic.in** with the temporary application number, every transaction ID, amount, time and the bank reference. Failed gateway debits are normally refunded within 5 to 7 working days.

## The receipt

Open the receipt from Pending CBR or Payments and save it with the browser's Print > Save as PDF (it may download as a generic name such as `PATENT eFiling.pdf`). The CBR receipt shows the **application number** (12 digits, starting with the year), the CBR number and the date and time. Save it next to the filed PDFs and run `/patent-kit:track` with it.
