import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = "C:/Users/caner/OneDrive/Desktop/Python/Lenna.png"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)
if image is None:
raise FileNotFoundError("Lenna image could not be loaded")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
scaling_factors = [0.5, 0.25, 0.1]
interpolations = {
"Nearest": cv2.INTER_NEAREST,
"Linear": cv2.INTER_LINEAR,
"Cubic": cv2.INTER_CUBIC,
"Lanczos": cv2.INTER_LANCZOS4
}
fig, axes = plt.subplots(len(scaling_factors), len(interpolations) + 1, figsize=(20, 15))
for i, scale in enumerate(scaling_factors):
for j, (method_name, method) in enumerate(interpolations.items()):
small = cv2.resize(image, None, fx=scale, fy=scale, interpolation=method)
restored = cv2.resize(small, (image.shape[1], image.shape[0]),
interpolation=method)
restored_rgb = cv2.cvtColor(restored, cv2.COLOR_BGR2RGB)
axes[i, j + 1].imshow(restored_rgb)
axes[i, j + 1].set_title(f"{method_name} (Factor {scale})", fontsize=10)
axes[i, j + 1].axis("off")
axes[i, 0].imshow(image_rgb)
axes[i, 0].set_title("Original", fontsize=10)
axes[i, 0].axis("off")
plt.tight_layout()
plt.subplots_adjust(top=0.9, hspace=0.3, wspace=0.3)
plt.show()
