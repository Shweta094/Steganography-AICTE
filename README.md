Here's a **human-friendly** README file for your repository. It explains the project, its purpose, and how to use it in a simple and engaging way. 🚀  

---

# 🕵️‍♂️ Steganography GUI – Hide & Reveal Secrets in Images!  

Welcome to the **Steganography GUI** project! This tool allows you to **hide secret messages inside images** and later retrieve them, all with a simple and interactive graphical interface.  

##  What's Inside?  

Here's what you'll find in this repository:  

| File Name               | Description |
|-------------------------|-------------|
| `steganography_code.py` | The Python script containing the GUI and encoding/decoding logic. |
| `sampleImage.png`       | A normal image (used as an example before encoding). |
| `EncryptedImage.png`    | An image that contains a hidden secret message. |

## Features  
✅ **User-Friendly GUI** – No need for command-line input! Everything works via an easy-to-use interface.  
✅ **Encode Messages** – Hide any text inside an image without changing how it looks.  
✅ **Decode Messages** – Extract hidden text from an encoded image.  
✅ **Cyberpunk VFX** – The GUI has a "hacker-style" aesthetic for extra fun.  

## How to Use It  

### 🔹 Step 1: Install Dependencies  
Make sure you have **Python** installed. Then, install the required libraries:  
```sh
pip install tkinter pillow stegano
```

### Step 2: Run the Script  
Launch the GUI by running:  
```sh
python steganography_code.py
```

### Step 3: Hide a Secret Message  
1. Click **Load Image** and select `sampleImage.png` (or any other image).  
2. Enter a **secret message** in the text box.  
3. Click **Encode Text**, then **save** the new encrypted image (e.g., `EncryptedImage.png`).  

### Step 4: Reveal a Hidden Message  
1. Click **Load Image** and select `EncryptedImage.png`.  
2. Click **Decode Text** – the hidden message will appear!  
3. A pop-up will say **"Hacker Mode Activated"** (because why not? 😎).  

## Example  
🖼 **Before Encoding:** `sampleImage.png` – A normal image.  
🖼 **After Encoding:** `EncryptedImage.png` – Looks the same, but secretly contains a message!  

## ⚠️ Notes  
- This tool uses **LSB steganography** (Least Significant Bit), meaning the image remains visually unchanged.  
- Only **.png and .bmp** formats are supported for encoding.  
- If decoding fails, make sure you're using an image that actually contains a hidden message.  

---

### 🎉 Enjoy hiding secrets like a true hacker! 😎  
For any issues, feel free to open an **Issue** or contribute to the project! 🚀  

---
