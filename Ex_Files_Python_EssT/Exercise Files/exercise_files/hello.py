# n = int(input())
# if n % 2:
#     print("Weird")
# elif 2 <= n <= 5:
#     print("Not Weird")
# elif 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")
import os
import csv

# with open("C:\\Users\\kanza\\Downloads\\Ex_Files_Python_EssT\\Ex_Files_Python_EssT\\Exercise Files\\exercise_files\\titanic.csv", newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

def print_length(data):
    length = len(data)
    print(f"The length of the Titanic dataset is: {length}")

def print_keys(data):
    keys = data[:12]  # Assuming the first row contains the headers
    print(f"Keys: {keys}")

def print_values(data):
    values = data[:12]  # Exclude the header row
    for row in values:
        print(row)

def convert_to_list(data):
    data_list = list(data)
    half_length = len(data_list) // 10  # Calculate the halfway point
    first_half = data_list[:half_length]  # Slice the list to get the first half
    print(f"First half of the data as list: {first_half}")

# Main code
file_path = "C:\\Users\\kanza\\Downloads\\Ex_Files_Python_EssT\\Ex_Files_Python_EssT\\Exercise Files\\exercise_files\\titanic.csv"
data = read_csv(file_path)

# Call the functions as needed
#convert_to_list(data)
def add(a, b):
    return a + b

# Unit test
assert add(2, 3) == 5
assert add(-1, 1) == 0