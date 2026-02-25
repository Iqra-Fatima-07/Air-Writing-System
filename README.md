# **Air Writing System**

<p align="center">
  <strong>Real-Time Hand Gesture Based Virtual Drawing using Computer Vision</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv"/>
  <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Working-success?style=for-the-badge"/>
</p>

---

## **Project Overview**

Air Writing System is a real-time computer vision application that enables users to draw in the air using hand gestures captured through a webcam.

The system detects hand landmarks using MediaPipe and maps the index finger tip movement onto a virtual canvas using OpenCV.

It demonstrates practical implementation of real-time vision-based human-computer interaction.

---

## **Technical Details**

<details>
<summary><strong>Core Concepts Implemented</strong></summary>

<br>

- Real-time video processing  
- 21-point hand landmark detection  
- Gesture-based interaction  
- Finger coordinate mapping  
- Object-oriented program structure  

</details>

---

## **Key Features**

<details>
<summary><strong>Click to Expand</strong></summary>

<br>

- Real-time hand tracking  
- Index finger drawing mechanism  
- Clear screen functionality  
- Smooth and responsive drawing  
- Lightweight and efficient performance  

</details>

---

## **Technology Stack**

<details>
<summary><strong>Tech Stack Breakdown</strong></summary>

<br>

| Technology | Purpose |
|------------|----------|
| Python 3.11 | Core programming language |
| OpenCV | Video capture and drawing |
| MediaPipe (0.10.9) | Hand tracking |
| NumPy | Numerical operations |

</details>

---

## **Project Structure**

<details>
<summary><strong>Folder Structure</strong></summary>

<br>

```
air-writing-system/
│
├── main.py
├── hand_tracking.py
├── ui_utils.py
└── README.md
```

</details>

---

## **Installation Guide**

<details>
<summary><strong>Setup Instructions</strong></summary>

<br>

### Clone Repository
```
git clone https://github.com/your-username/air-writing-system.git
cd air-writing-system
```

### Create Virtual Environment
```
python -m venv venv
```

### Activate Environment

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

### Install Dependencies
```
pip install opencv-python
pip install mediapipe==0.10.9
pip install numpy
```

</details>

---

## **Run the Application**

```
python main.py
```

Ensure your webcam is enabled.

---

## **How It Works**

<details>
<summary><strong>System Workflow</strong></summary>

<br>

1. Webcam captures live video frames  
2. MediaPipe detects 21 hand landmarks  
3. Index finger tip coordinates are extracted  
4. Movement is mapped to virtual canvas  
5. Specific gestures trigger actions  

</details>

---

## **Future Enhancements**

<details>
<summary><strong>Planned Improvements</strong></summary>

<br>

- Save drawing as image  
- Add color selection gestures  
- Implement eraser mode  
- Improve gesture accuracy  
- Integrate handwriting recognition  

</details>

---

## **Author**

<p align="center">

### **Iqra Fatima**  
Computer Science Student  
Specialisation in Artificial Intelligence  

Artificial Intelligence • Computer Vision • Real-Time Vision Systems  

</p>

---

## **License**

This project is open-source and available under the MIT License.

