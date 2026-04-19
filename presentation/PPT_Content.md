# AI CrowdSense - Hackathon Pitch Deck

This document outlines the ideal sequence and talking points for your 5-minute hackathon presentation.

## Slide 1: The Title Slide
**Visual:** 
- Large **AI CrowdSense** logo.
- Subtitle: "Smart Event Experience Platform."
- Your Team Name.

**Talking Point:** 
> "Hello judges! We are presenting AI CrowdSense, a platform designed to end the chaos of massive crowds at large events."

---

## Slide 2: The Problem
**Visual:** 
- Bullet points fading in:
  - 🚶 Crowd movement chaos & bottlenecks.
  - ⏳ 30+ minute waiting times for food and washrooms.
  - 😵 Poor overall attendee experience.
- Image of a crowded, confusing stadium corridor.

**Talking Point:** 
> "At large sporting events or concerts, attendees waste huge amounts of time in queues and struggle to find the fastest routes. This leads to frustrated fans and unequal distribution of crowds for vendors."

---

## Slide 3: Our Solution
**Visual:** 
- 3 bold icons representing: 
  1. Smart Navigation 
  2. Queue Prediction
  3. AI Assistant
- A screenshot of our sleek, dark-mode web application.

**Talking Point:** 
> "Our solution is AI CrowdSense. It gives users real-time queue predictions, intelligent route navigation, and an AI assistant that dynamically balances crowds out across the venue."

---

## Slide 4: Key Feature - Bias-Aware Routing (The "Wow" Factor)
**Visual:** 
- Diagram showing 100 people. 
  - Standard App: Sends all 100 to Stall A because it's closest (creates a new bottleneck).
  - AI CrowdSense: Sends 50 to Stall A, 50 to Stall B.

**Talking Point:** 
> "What makes our tool different is our Bias-Aware Recommendation engine. By utilizing Google Gemini, we don't just send everyone to the shortest queue. We intelligently balance recommendations to ensure smooth crowd flow across *all* stalls."

---

## Slide 5: Tech Stack & Architecture
**Visual:** 
- Simple Architecture Flowchart:
  - Frontend: HTML/CSS/JS (Glassmorphism UI)
  - Backend API: Python FastAPI
  - AI Engine: Google Gemini 2.5 Flash
  - Cloud: Deployed via Docker on Google Cloud Run

**Talking Point:** 
> "We built this with a lightweight Vanilla JS frontend communicating with a Python FastAPI backend. The core logic is powered by Google Gemini via prompt-engineering. And it’s completely containerized and deployed live on Google Cloud Run."

---

## Slide 6: LIVE DEMO
**Visual:** 
- Switch to the LIVE browser.

**Execution:** 
1. Show the Live Queue times updating to prove the data is "live".
2. Select a destination (e.g., "Food Stall A") and hit "Get Route". Point out why the AI suggested what it did.
3. Type a custom question into the AI Assistant like: "Where is the best place to get food right now?" Wait for Gemini's intelligent response.

---

## Slide 7: Future Scope & Conclusion
**Visual:** 
- Bullet points:
  - Integrate real IoT cameras for actual crowd counting.
  - Monetization via vendor partnerships.
  - Mobile App release.

**Talking Point:** 
> "In the future, we can upgrade our simulated data engine to use live IoT cameras. AI CrowdSense is the modern standard for event management. Thank you!"
