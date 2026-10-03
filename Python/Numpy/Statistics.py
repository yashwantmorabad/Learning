import numpy as np

# A sample array of data (e.g., ages of people)
ages = np.array([22, 25, 30, 35, 40, 22, 28])

print("Sum:", np.sum(ages))           # Adds everything together
print("Mean:", np.mean(ages))         # The average
print("Median:", np.median(ages))     # The middle value when sorted
print("Min / Max:", np.min(ages), "/", np.max(ages))
print("Standard Dev:", np.std(ages))  # How spread out the data is
print("Variance:", np.var(ages))      # The square of the standard deviation


import numpy as np

# Imagine 3 students (rows) and their scores on 4 tests (columns)
scores = np.array([
    [80, 85, 90, 95], # Student 1
    [70, 75, 80, 85], # Student 2
    [90, 95, 100, 90] # Student 3
])

# Global Mean (Average of all tests by all students)
print("Global Mean:", np.mean(scores)) 
# Output: 85.41

# Axis=0 (Average score for EACH TEST)
print("Test Averages (axis=0):", np.mean(scores, axis=0)) 
# Output: [80.  85.  90.  90.]

# Axis=1 (Average score for EACH STUDENT)
print("Student Averages (axis=1):", np.mean(scores, axis=1)) 
# Output: [87.5 77.5 93.75]