<!-- ========================================================= -->
<!--                    AIR WRITING SYSTEM                     -->
<!-- ========================================================= -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:141E30,50:243B55,100:0F2027&height=220&section=header&text=Air%20Writing%20System&fontSize=45&fontColor=ffffff&animation=fadeIn&fontAlignY=38"/>

<br>

<img src="https://readme-typing-svg.herokuapp.com?color=5E60CE&center=true&vCenter=true&width=600&lines=Real-Time+Hand+Gesture+Drawing;Computer+Vision+Based+Interaction;MediaPipe+%2B+OpenCV+Integration;Human-Computer+Interaction+System" />

<br><br>

<strong>Real-Time Hand Gesture Based Virtual Drawing using Computer Vision</strong>

<br><br>

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv"/>
<img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Working-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Build-Stable-brightgreen?style=for-the-badge"/>

</div>

---

# Project Overview

Air Writing System is a real-time computer vision application that enables users to draw in the air using hand gestures captured through a webcam.

The system detects hand landmarks using **MediaPipe** and maps the index finger tip movement onto a virtual canvas using **OpenCV**.

It demonstrates practical implementation of:

- Real-time vision processing  
- Gesture-based interaction  
- Human-Computer Interaction (HCI)  
- AI-based motion tracking  

---

# Technical Details

### Core Concepts Implemented

- Real-time video frame capture  
- 21-point hand landmark detection  
- Gesture-based event triggering  
- Finger coordinate mapping to 2D canvas  
- Object-Oriented Python design  

---

# Key Features

- Real-time hand tracking  
- Index finger drawing mechanism  
- Clear screen functionality  
- Smooth stroke rendering  
- Low latency processing  
- Lightweight architecture  

---

# System Architecture

```mermaid
flowchart LR
    A[Webcam Input] --> B[OpenCV Frame Capture]
    B --> C[MediaPipe Hand Detection]
    C --> D[Landmark Extraction]
    D --> E[Index Finger Tracking]
    E --> F[Coordinate Mapping]
    F --> G[Virtual Canvas Rendering]
```

---

# Workflow

```mermaid
flowchart TD
    A[Start Application] --> B[Activate Webcam]
    B --> C[Detect Hand]
    C --> D{Index Finger Up?}
    D -- Yes --> E[Track Movement]
    E --> F[Draw on Canvas]
    D -- No --> G[Wait for Gesture]
```

---

# Technology Stack

| Technology | Purpose |
|------------|----------|
| Python 3.11 | Core language |
| OpenCV | Video capture & drawing engine |
| MediaPipe 0.10.9 | Hand tracking & landmark detection |
| NumPy | Numerical operations |

---

# Project Structure

```
air-writing-system/
│
├── main.py
├── hand_tracking.py
├── ui_utils.py
└── README.md
```

---

# Installation Guide

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

---

# Run the Application

```
python main.py
```

Ensure your webcam is enabled.

---

# Future Enhancements

- Save drawing as image  
- Add color selection gestures  
- Implement eraser mode  
- Improve gesture classification  
- Integrate handwriting recognition model  
- Multi-hand support  

---

# Commit Guide

To maintain a clean and professional repository, this project follows the Conventional Commits standard.

This ensures:
- Clear version history
- Structured commit tracking
- Professional collaboration
- Improved readability

---

## Commit Message Format

```
<type>: <short description>

[optional body]

[optional footer]
```

---

## Commit Types

| Type     | Purpose |
|----------|----------|
| feat     | New feature |
| fix      | Bug fix |
| docs     | Documentation updates |
| style    | Code formatting (no logic change) |
| refactor | Code restructuring without changing functionality |
| perf     | Performance improvements |
| test     | Adding or updating tests |
| chore    | Maintenance tasks |
| build    | Dependency or build system changes |
| ci       | CI/CD configuration changes |

---

## Examples

### Adding a new feature
```
feat: add multi-hand tracking support
```

### Fixing a bug
```
fix: resolve index finger tracking lag
```

### Updating documentation
```
docs: update installation instructions
```

### Refactoring code
```
refactor: optimize landmark detection pipeline
```

---

## Branch Naming Convention

```
feature/hand-gesture-improvement
fix/canvas-render-issue
docs/readme-update
refactor/performance-enhancement
```

---

## Contribution Workflow

```mermaid
flowchart LR
    A[Fork Repository] --> B[Create Feature Branch]
    B --> C[Make Changes]
    C --> D[Commit with Proper Message]
    D --> E[Push to GitHub]
    E --> F[Create Pull Request]
    F --> G[Code Review]
    G --> H[Merge]
```

---

## Pull Request Guidelines

- Keep pull requests focused on a single feature or fix
- Follow the commit message format
- Ensure the project runs without errors
- Update documentation if required
- Maintain clean and readable code

---

## Versioning Strategy

This project follows Semantic Versioning (SemVer):

```
MAJOR.MINOR.PATCH
```

| Version Part | Meaning |
|--------------|----------|
| MAJOR | Breaking changes |
| MINOR | New features |
| PATCH | Bug fixes |

Example:
```
v1.2.3
```

---

## Best Practices

- Write meaningful commit messages
- Avoid large unrelated commits
- Test before pushing
- Use descriptive branch names
- Keep commits atomic and focused

---

# Author

Iqra Fatima  
Computer Science Student  
Specialisation in Artificial Intelligence  

Artificial Intelligence • Computer Vision • Real-Time Vision Systems  

---

# License

This project is open-source and available under the MIT License.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:243B55,100:141E30&height=120&section=footer"/>

</div>
