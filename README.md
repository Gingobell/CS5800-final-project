# 🎵 Smart Playlist Generator – Balancing Mood and Energy through Algorithms
### *“Let algorithms tune your mood.”*

---

## 🧠 Question and Problem Definition
We aim to answer the question:

> **How can we use algorithms to automatically generate a playlist that maintains balanced mood transitions and smooth energy flow, while avoiding repetition or abrupt shifts?**

Our goal is to create a **Smart Playlist Generator** that organizes a set of songs based on **energy (tempo)** and **emotion (mood score)**.  
The algorithm should produce a sequence that feels **natural**, **gradually evolving in energy**, and **avoids abrupt jumps or repetitive transitions**.

---

## 📘 Scope

### ✅ **In Scope**
- **Dataset:**  
  A small synthetic or automatically generated CSV dataset of songs with attributes:  
  `tempo`, `mood`, and `duration`.

- **Core Algorithms:**  
  1. **Sorting Algorithm** – orders songs by energy or mood intensity.  
  2. **Greedy Algorithm** – iteratively selects the next song that best balances similarity and contrast.

- **Python Audio Analysis:**  
  Use libraries such as **librosa** or **Essentia** to automatically calculate:
  - Tempo (beats per minute)  
  - Energy (RMS loudness)  
  - Mood score (interpretable combination of tempo + loudness)

- **Frontend Implementation (Local HTML5 Audio Player):**
  - A lightweight web interface built with **HTML, CSS, and JavaScript**.  
  - Users upload local MP3 files.  
  - The app analyzes metadata and applies **sorting + greedy** algorithms to determine playback order.  
  - Songs play directly from local URLs using the HTML `<audio>` element (no Internet or APIs).  
  - The interface displays:
    - Playlist order  
    - Energy / Mood metrics  
    - Visualization of the playlist flow

- **Evaluation Metrics:**
  - Smoothness of transitions  
  - Playlist diversity  
  - Total playlist duration

### 🚫 **Out of Scope**
- External APIs (e.g., Spotify, YouTube Music)
- Machine-learning or AI-based recommendation models
- Cloud services or database integration

---

## 📅 Five-Week Plan

| **Week** | **Goal** | **Deliverables** |
|-----------|-----------|------------------|
| 1 | Define data model and implement Python audio feature extraction (tempo, mood, duration). | Dataset CSV, Scoring script |
| 2 | Implement and test sorting algorithm for baseline ordering. | Ordered playlist output |
| 3 | Implement greedy algorithm for smooth mood/energy transitions. | Smart sequencing prototype |
| 4 | Build and integrate Local HTML5 Audio Player frontend with backend algorithms; add visualization. | Fully functional interactive web app |
| 5 | Evaluate results, prepare report, and finalize presentation. | Final demo, graphs, and slides |

---

## 📚 Relation to Algorithms Textbook

This project directly applies **fundamental algorithmic concepts** discussed in class:

- **Sorting Algorithms:**  
  Used to order songs by numerical features like tempo or mood intensity.  
  ⏱️ *Time complexity: O(n log n)*

- **Greedy Algorithm:**  
  Iteratively selects the next song that minimizes abrupt transitions while maximizing diversity.  
  ⏱️ *Time complexity: O(n)*

- **Complexity Analysis:**  
  Evaluates the trade-off between computational simplicity and playlist quality.

> By grounding an interactive music system in core algorithmic principles,  
> this project demonstrates how textbook theory can enhance real-world user experiences.

---

## 🎯 Expected Outcomes

By the end of the project, we expect to deliver:

- 🐍 A **Python-based backend** that automatically extracts tempo, energy, and mood from MP3 files.  
- 💻 An **interactive HTML5 frontend** that visualizes playlist flow and plays music in smart order.  
- 📊 **Comparative analysis** between random playlists and algorithm-optimized sequences.  
- 🧩 A **final presentation** explaining how simple algorithms can emulate human-like playlist curation.

---

## 💡 Summary

The **Smart Playlist Generator** bridges **algorithmic reasoning** and **user experience design**.  
By combining **Sorting**, **Greedy selection**, and an **interactive HTML5 audio interface**,  
our system demonstrates how fundamental algorithms can create playlists that **feel human**,  
**sound natural**, and **flow emotionally** — all completely **offline**.

---

## 🛠️ Technologies Used
- **Python 3** – for backend feature extraction and playlist logic  
- **Librosa / NumPy / Pandas** – for audio analysis and data processing  
- **HTML5 + JavaScript** – for frontend audio playback and visualization  
- **Matplotlib (optional)** – for plotting energy/mood curves

---

## 🚀 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Smart-Playlist-Generator.git
   cd Smart-Playlist-Generator
