# Image Processing Tasks

This repository showcases two essential image processing techniques:

1. **Image Interpolation**: Examining the effects of scaling factors and interpolation methods (Nearest, Linear, Cubic, Lanczos) on the quality of resized images.
2. **Histogram Equalization**: Analyzing the contrast enhancement of underexposed, overexposed, and frequency-filtered images.

---

## Project Structure

- `src/`: Contains the Python scripts for the tasks.
- `images/`: Includes the input image (`Lenna.png`).
- `README.md`: Explains the project.
- `AiCV_Report.pdf`: Detailed report of the tasks.

---

## Tasks Overview

### Task 1: Image Interpolation

- Resize the `Lenna.png` image using scaling factors (0.5, 0.25, 0.1).
- Apply four interpolation methods:
  - **Nearest-Neighbor**
  - **Linear**
  - **Cubic**
  - **Lanczos**
- Compare the visual results of downscaled and restored images.

### Task 2: Histogram Equalization

- Enhance the contrast of grayscale images:
  - Original, underexposed, and overexposed.
  - Low-frequency and high-frequency filtered images.
- Display the results with and without equalization.

---

## How to Run the Code

### Prerequisites

- Python 3.x
- Required Libraries: `cv2`, `numpy`, `matplotlib`
- Install dependencies using:
  ```bash
  pip install opencv-python-headless matplotlib numpy
