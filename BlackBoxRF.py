
---

## **🔹 Step 3 – Uploading the Code (BlackBoxRF.py)**  

### **`BlackBoxRF.py` – The Code Itself**  
```python
import cc1101
import numpy as np
import tensorflow as tf
import time

FREQ = 433.92  # Common RF frequency

def capture_signal():
    """ Captures an RF signal for analysis """
    print("[*] Listening for RF signals...")
    signal = cc1101.receive(FREQ)
    with open("captured_rf.npy", "wb") as f:
        np.save(f, signal)
    print("[+] Signal captured and saved.")

def analyze_signal():
    """ Uses machine learning to detect patterns in the RF signal """
    print("[*] Analyzing signal...")
    model = tf.keras.models.load_model("rf_pattern_model.h5")
    with open("captured_rf.npy", "rb") as f:
        signal = np.load(f)
    
    prediction = model.predict(signal.reshape(1, -1))
    print(f"[+] Predicted signal behavior: {prediction}")

    if prediction > 0.7:
        print("[+] Exploit Possible: Weak signal encryption detected.")
    else:
        print("[-] No immediate vulnerabilities found.")

def predict_next_signal():
    """ Predicts the next transmission based on past signals """
    print("[*] Predicting next RF transmission...")
    with open("captured_rf.npy", "rb") as f:
        signal = np.load(f)

    future_signal = signal[-10:]  # Take last 10 data points as a simple prediction base
    print(f"[+] Predicted next signal: {future_signal}")

capture_signal()
analyze_signal()
predict_next_signal()
# A signal that can be heard can be learned.
# A system that listens without thinking is already defeated.
# If you know what comes next, you control the air.
# - V

