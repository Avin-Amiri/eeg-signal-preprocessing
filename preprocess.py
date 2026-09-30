import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, iirnotch

def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    """
    Applies a 4th-order Butterworth bandpass filter.
    
    Parameters:
    data (array): Input signal time-series.
    lowcut (float): Lower cutoff frequency.
    highcut (float): Upper cutoff frequency.
    fs (float): Sampling frequency.
    order (int): Filter order.
    
    Returns:
    array: Filtered signal.
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

def notch_filter(data, notch_freq, fs, quality_factor=30.0):
    """
    Applies an IIR notch filter to remove specific frequency interference (e.g., 50Hz power line).
    
    Parameters:
    data (array): Input signal.
    notch_freq (float): Frequency to remove.
    fs (float): Sampling frequency.
    quality_factor (float): Quality factor.
    
    Returns:
    array: Filtered signal.
    """
    nyq = 0.5 * fs
    freq = notch_freq / nyq
    b, a = iirnotch(freq, quality_factor)
    return filtfilt(b, a, data)

def main():
    # Sampling frequency (Hz)
    fs = 250.0  
    t = np.arange(0, 2.0, 1.0 / fs)
    
    # Simulate synthetic EEG: Alpha wave (10Hz) + Power line noise (50Hz) + Random noise
    alpha_wave = np.sin(2 * np.pi * 10 * t)
    noise_50hz = 0.5 * np.sin(2 * np.pi * 50 * t)
    random_noise = 0.2 * np.random.normal(size=t.shape)
    raw_signal = alpha_wave + noise_50hz + random_noise

    # Pipeline execution
    # Apply bandpass filter (0.5 - 45 Hz) and notch filter (50 Hz)
    filtered = butter_bandpass_filter(raw_signal, 0.5, 45.0, fs)
    cleaned_signal = notch_filter(filtered, 50.0, fs)

    # Plotting and saving
    plt.figure(figsize=(10, 4))
    plt.plot(t, raw_signal, label='Raw EEG (with 50Hz noise)', alpha=0.6)
    plt.plot(t, cleaned_signal, label='Cleaned EEG', color='red', linewidth=1.5)
    plt.title('EEG Baseline Preprocessing Pipeline')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (uV)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('eeg_filtered_sample.png')
    print("Pipeline executed successfully. Plot saved as eeg_filtered_sample.png")

if __name__ == '__main__':
    main()
