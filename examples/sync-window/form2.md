<!-- Example only: fictional inventor and invention. -->

# FORM 2

**THE PATENTS ACT, 1970**
(39 of 1970)
&
**THE PATENTS RULES, 2003**

**PROVISIONAL SPECIFICATION**
(See section 10 and rule 13)

**1. TITLE OF THE INVENTION**

SCHEDULING BACKGROUND DATA SYNCHRONISATION OF MOBILE APPLICATIONS INTO SHARED RADIO ACTIVITY WINDOWS

**2. APPLICANT**

(a) Name: ASHA EXAMPLE
(b) Nationality: Indian
(c) Address: Flat 1, Sample Residency, Example Road, Pune, Maharashtra - 411000

**3. PREAMBLE TO THE DESCRIPTION**

PROVISIONAL

The following specification describes the invention.

---

## FIELD OF THE INVENTION

[0001] The present invention relates to mobile operating systems and applications that synchronise data in the background. More particularly, it relates to scheduling such synchronisations so that they share periods in which the device's radio is already active.

## BACKGROUND OF THE INVENTION

[0002] Mobile applications synchronise data in the background: mail, messages, feeds, backups and analytics. Each synchronisation wakes the cellular or Wi-Fi radio. After a transfer ends, the radio stays in a high-power state for several seconds before returning to idle (the "tail"). When many applications synchronise small amounts of data at different moments, the device pays many tails, and the energy spent is far larger than the data requires.

[0003] Operating-system job schedulers can defer background jobs until the device is charging or on an unmetered network. Push messaging wakes an application only when its server has data. Individual applications may batch their own requests.

[0004] None of these solves the following technical problem: deferrable synchronisations of different applications still start at different moments, each turning the radio on and each paying its own tail.

## OBJECTS OF THE INVENTION

[0005] An object of the invention is to reduce the number of radio high-power tails needed to perform the background synchronisations of several applications.

[0006] Another object is to do so without changing application logic beyond declaring a deadline for each synchronisation.

## SUMMARY OF THE INVENTION

[0007] According to the invention, a scheduler on the device keeps a registry of pending deferrable synchronisations, each with a deadline and an estimated size. When the radio becomes active for any reason (a user action, a push message, or a synchronisation whose deadline has arrived), the scheduler selects the pending synchronisations that fit in the expected active window of the radio and starts them during that window, so that they share one tail.

[0008] In embodiments the expected window is learned per network from observed tails, and a wearable device routes its synchronisations through the active window of a paired phone.

## BRIEF DESCRIPTION OF THE DRAWINGS

[0009] Figure 1 shows the architecture of a device with a synchronisation scheduler according to an embodiment.

[0010] Figure 2 is a flowchart of the window planner.

## DETAILED DESCRIPTION OF THE INVENTION

[0011] The following description sets out embodiments in detail. They are examples; the invention is not limited to them, and features described for one embodiment may be combined with features of other embodiments.

### Architecture (Figure 1)

[0012] Referring to Figure 1, a mobile device 100 comprises a synchronisation scheduler service 110 with a registry 112 of pending synchronisations, a radio state monitor 114, a window planner 116 and a dispatcher 118. Applications 120 register synchronisations through an interface 122, each with the application identifier, an estimated number of bytes, a deadline and a priority. The radio 130 reports its power state to the monitor 114.

### Window planner (Figure 2)

[0013] Referring to Figure 2, when the monitor reports that the radio has become active (step 202), the planner estimates the remaining active window (step 204), sorts the pending synchronisations by deadline and priority (step 206), selects those whose estimated transfer time fits in the window (step 208), and the dispatcher starts them (step 210). The registry is updated (step 212). Synchronisations whose deadline arrives with the radio idle are started on their own and open a window for others (step 214).

### Other embodiments

[0014] The expected window length is learned per network and per radio technology from the observed duration of past tails.

[0015] A wearable device paired with a phone registers its synchronisations with the phone's scheduler, which performs them during the phone's active windows.

[0016] A user setting selects between freshness and battery, which scales the deadlines.

## TECHNICAL EFFECTS AND ADVANTAGES

[0017] Fewer radio high-power tails are needed for the same amount of synchronised data, reducing energy per synchronised byte.

[0018] Applications need only declare a deadline; the scheduling is performed by the device for all applications together.

## INDUSTRIAL APPLICABILITY

[0019] The invention can be used in mobile phones, tablets, wearables and other battery-powered connected devices.

[0020] The foregoing describes embodiments of the invention. Modifications and variations that do not depart from the scope of the invention will be apparent to persons skilled in the art.

---

Dated this 2nd day of November, 2026

Signature:

Name: ASHA EXAMPLE
Applicant

---

## ABSTRACT

SCHEDULING BACKGROUND DATA SYNCHRONISATION OF MOBILE APPLICATIONS INTO SHARED RADIO ACTIVITY WINDOWS

A scheduler on a mobile device keeps pending deferrable synchronisations of several applications, each with a deadline and estimated size. When the radio becomes active for any reason, the scheduler starts the pending synchronisations that fit in the expected active window, so that they share one high-power tail instead of each waking the radio. The window length may be learned per network, and wearables may route synchronisations through a paired phone's windows. Energy per synchronised byte falls while applications only declare deadlines. (Figure 2)
