# Convert a NumPy array to 0 or 1 based on threshold in Python

import numpy as np

arr = np.array([0.2, 0.1, 0.4, 0.7, 0.3, 0.9])

new_arr = np.where(arr > 0.5, 1, 0)
print(new_arr)  # 👉️ [0 0 0 1 0 1]