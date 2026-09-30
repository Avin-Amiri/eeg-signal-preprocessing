# EEG Signal Preprocessing Pipeline

A clean, modular Python pipeline designed for baseline preprocessing of Electroencephalography (EEG) signals. This repository serves as a lightweight demonstration of signal filtering techniques commonly used in **Affective Computing**, **Brain-Computer Interfaces (BCI)**, and cognitive neuroscience research.

---

**No dataset is required for this pipeline.** 
To keep the repository self-contained, lightweight, and runnable instantly on any machine without downloading heavy external files (like DEAP, SEED, or PhysioNet), this script **synthesizes a realistic baseline EEG signal mathematically**:
1. **Physiological Signal:** Simulates an Alpha wave ($\approx 10\text{ Hz}$), which is a primary brain rhythm associated with relaxed wakefulness.
2. **Artifacts & Noise:** Artificially injects power-line interference ($50\text{ Hz}$ noise common in standard electrical grids) and Gaussian random noise.
3. **Validation:** The script then applies the filtering pipeline to successfully strip out the noise, proving that the signal processing steps work correctly.

---

## What is the purpose of this pipeline? What does it solve?

Raw EEG signals recorded from electrodes are notoriously noisy and unreliable on their own. Before feeding EEG data into Machine Learning models or deep learning networks for emotion recognition or classification, researchers must clean the signal. 

This pipeline addresses two primary noise sources:
1. **Bandpass Filtering (0.5 – 45 Hz):** Uses a 4th-order Butterworth filter to isolate relevant neurological brain bands (Delta, Theta, Alpha, Beta) while removing slow baseline drifts and high-frequency muscle/environmental artifacts.
2. **Notch Filtering (50 Hz):** Implements an IIR notch filter to specifically target and eliminate electrical power-line hum without distorting adjacent frequency bands.

---

## Features
- **Modular Design:** Cleanly separated functions for bandpass and notch filtering with academic docstrings.
- **Visualization:** Automatically generates and saves a time-series comparative plot (`eeg_filtered_sample.png`) showing raw vs. cleaned signals.
- **Zero-Dependency Bloat:** Relies strictly on standard, optimized scientific Python libraries (`numpy`, `scipy`, `matplotlib`).

---

## Quickstart

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/eeg-signal-preprocessing.git
   cd eeg-signal-preprocessing
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**
   ```bash
   python preprocess.py
   ```

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
