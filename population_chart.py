import matplotlib.pyplot as plt
import numpy as np

# Example dataset
ages = [23, 25, 31, 45, 22, 36, 41, 52, 33, 27, 29, 30, 35, 40, 50, 60, 21, 22, 23, 24]
genders = ["Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female",
           "Male", "Male", "Female", "Female", "Male", "Male", "Female", "Male",
           "Female", "Male", "Female", "Male"]

# Histogram for ages
plt.figure(figsize=(8, 5))
plt.hist(ages, bins=8, edgecolor='black')
plt.title('Age Distribution in Population')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Bar chart for gender distribution
plt.figure(figsize=(6, 4))
unique_genders, counts = np.unique(genders, return_counts=True)
plt.bar(unique_genders, counts, color=['blue', 'pink'])
plt.title('Gender Distribution in Population')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
