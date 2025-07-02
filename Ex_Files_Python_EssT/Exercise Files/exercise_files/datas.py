# import sys
# print("Python executable:", sys.executable)
# import numpy as np
# array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(array.shape)
# print(array.ndim)
# print(array)

# import pandas as pd
# objects = pd.Series([1, 2, 3])
# print(objects)

words_list = ["apple", "banana", "cherry", "grape", "kiwi", "mango"]

# Define function
def filter_words(words, letters={'a', 'e'}):
    return [word for word in words if any(letter in word for letter in letters)]

# Calling function multiple times
print(filter_words(words_list))  # First usage
print(filter_words(["orange", "blueberry", "watermelon"]))  # Second usage
