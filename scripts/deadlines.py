#!/usr/bin/env python3
"""Deadlines for an Indian provisional application, from its filing date.

Usage: python3 deadlines.py YYYY-MM-DD [--esign-expiry YYYY-MM-DD] [--form3-filed] [--ics FILE.ics] [--title TEXT]

Prints a Markdown table to paste into the tracker. With --ics, also writes a calendar file (all-day events,
each with a reminder two weeks before) that imports into Google Calendar, Apple Calendar or Outlook. Verify every date against the current Patents Rules
on ipindia.gov.in; the 31-month examination rule applies to applications filed on or after 15 Mar 2024.
"""
import calendar, datetime as dt, sys


def add_months(d, n):
    m = d.month - 1 + n
    y, m = d.year + m // 12, m % 12 + 1
    return dt.date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    filed = dt.date.fromisoformat(args[0])
    opt = lambda k: args[args.index(k) + 1] if k in args else None
    esign = dt.date.fromisoformat(opt("--esign-expiry")) if opt("--esign-expiry") else None
    form3 = "--form3-filed" in args
    title = opt("--title") or "patent application"
    f = lambda d: d.strftime("%d %b %Y")
    rows = [
        (filed + dt.timedelta(weeks=6), "Earliest date to file abroad without Form 25 permission (Section 39)"),
        (add_months(filed, 6), "Form 3: filed with the application" if form3 else "**Form 3 due** (statement and undertaking)"),
        (add_months(filed, 11), "Target: file the complete specification (a month of margin before the hard deadline)"),
        (add_months(filed, 10), "Decide on foreign protection (PCT)"),
        (add_months(filed, 12), "**Complete specification with claims + Form 5 (no extension); PCT application if wanted**"),
        (add_months(filed, 18), "Application published, unless Form 9 asks for earlier"),
        (add_months(filed, 31), "**Form 18, request for examination**, unless filed earlier"),
    ]
    if esign:
        rows.append((esign, "eSign or signing certificate expires: renew before any signing after this"))
    rows.sort()
    print(f"Deadlines for a provisional filed on {f(filed)}\n")
    print("| Date | What |\n|---|---|")
    for d, what in rows:
        print(f"| {f(d)} | {what} |")
    if esign and esign < add_months(filed, 12):
        print("\nNote: the signing certificate expires before the complete specification is due. Renew it in time.")
    if opt("--ics"):
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        ev = []
        for i, (d, what) in enumerate(rows):
            if "filed with the application" in what:
                continue
            text = what.replace("**", "").replace(",", "\\,").replace(";", "\\;")
            ev += ["BEGIN:VEVENT", f"UID:patent-kit-{filed:%Y%m%d}-{i}@patent-kit", f"DTSTAMP:{stamp}",
                   f"DTSTART;VALUE=DATE:{d:%Y%m%d}", f"DTEND;VALUE=DATE:{d + dt.timedelta(days=1):%Y%m%d}",
                   f"SUMMARY:Patent: {text}", f"DESCRIPTION:{title} (filed {f(filed)})",
                   "BEGIN:VALARM", "TRIGGER:-P14D", "ACTION:DISPLAY", f"DESCRIPTION:Patent: {text}", "END:VALARM",
                   "END:VEVENT"]
        ics = "\r\n".join(["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//patent-kit//deadlines//EN", *ev, "END:VCALENDAR"]) + "\r\n"
        open(opt("--ics"), "w", newline="").write(ics)
        print(f"\nwrote {opt('--ics')} ({len(ev) // 13} events, reminders two weeks before)")


if __name__ == "__main__":
    main()
