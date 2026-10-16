# Invention disclosure

> Example only: a fictional inventor and invention, to show the format.

| | |
|---|---|
| Working title | Scheduling background data synchronisation of mobile applications into shared radio activity windows |
| Short name | Sync Window |
| Inventor and applicant | Asha Example |
| Date of conception | 20 Oct 2026 |
| Built or tested so far | Android prototype; battery measurement on two phones |
| Public disclosure so far | None |

## 1. Field

Mobile operating systems and applications that synchronise data in the background over cellular or Wi-Fi radios.

## 2. Background and the problem

Each application wakes the radio on its own schedule. Every wake-up keeps the radio in a high-power state for several seconds after the transfer ends (the tail), so many small syncs cost far more energy than their data.

Known approaches:

1. Operating-system job schedulers that defer jobs until charging or unmetered network.
2. Push messaging that wakes an app only when the server has data.

The problem these do not solve: deferrable syncs from different apps still start at different moments, each paying its own radio tail.

## 3. Summary of the invention

A scheduler on the device keeps a list of pending deferrable syncs, each with a deadline. When any transfer turns the radio on (a user action, a push message or a sync whose deadline has come), the scheduler starts every pending sync that fits in the same radio activity window, so they share one tail.

## 4. Detailed description (one embodiment, as built)

### 4.1 Architecture

Sync scheduler service (110) with a registry of pending syncs (112), a radio state monitor (114), a window planner (116) and a dispatcher (118); applications (120) register syncs through an interface (122).

### 4.2 Data model

Pending sync: app, estimated bytes, deadline, priority.

### 4.3 Flow

Radio becomes active, planner selects syncs by deadline and size that fit the expected window, dispatcher starts them, registry updated, radio returns to idle.

## 5. Variations and other embodiments

1. The window length learned per network from past tails.
2. Wearables that route syncs through the phone's active window.
3. A user setting trading freshness for battery.

Ranking by commercial importance: 1, 2, 3.

## 6. Technical effects

1. Fewer radio high-power tails for the same data, so less energy per synchronised byte.
2. No change to application code beyond registering the sync with a deadline.

## 7. Claim sketch

1. A method in a mobile device comprising: keeping pending deferrable synchronisations each with a deadline; detecting a transition of a radio to an active state; selecting pending synchronisations that fit an expected active window; and starting them during that window.

## 8. Figures to draw

1. Architecture.
2. Flowchart of the window planner.

## 9. Evidence that it works

Prototype measurement: 31% less radio-on time over 24 hours on two test phones (example figures).

## 10. Open points for the inventor

- None.
