# Importing Necessary Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import joblib

# Variables and Data Types
number = 10          # Integer
pi = 3.14            # Float
message = "Hello"    # String
is_active = True     # Boolean

# Printing to the console
print("Number:", number)
print("Message:", message)

# Taking Input from the User
user_input = input("Enter a number: ")
print("You entered:", user_input)

# Functions
def add(a, b):
    """
    Returns the sum of a and b.
    """
    return a + b

result = add(5, 7)
print("Sum:", result)

# Conditional Statements
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Loops
# For Loop
for i in range(5):
    print("For Loop Iteration:", i)

# While Loop
count = 0
while count < 5:
    print("While Loop Count:", count)
    count += 1

# Data Structures
# List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Fruits:", fruits)

# Dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Person's Name:", person["name"])

# Tuple
colors = ("red", "green", "blue")
print("First Color:", colors[0])

# Set
unique_numbers = {1, 2, 3, 2, 1}
print("Unique Numbers:", unique_numbers)

# Exception Handling
try:
    division = number / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Classes and Objects
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Vehicle Brand: {self.brand}, Model: {self.model}")

car = Vehicle("Toyota", "Corolla")
car.info()

# Using NumPy for Numerical Computations
# Creating Arrays
array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", array)

# Performing Mathematical Operations
array_squared = array ** 2
print("Squared Array:", array_squared)

# Using Pandas for Data Manipulation
# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Accessing Data
print("Names:", df['Name'])

# Using Matplotlib for Data Visualization
# Plotting a Simple Line Graph
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Machine Learning with scikit-learn
# Sample Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3, 5, 7, 11])

# Splitting the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Creating and Training the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Making Predictions
predictions = model.predict(X_test)
print("Predictions:", predictions)

# Deep Learning with TensorFlow
# Defining a Simple Sequential Model
tf_model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

# Compiling the Model
tf_model.compile(optimizer='adam', loss='mean_squared_error')

# Training the Model
tf_model.fit(X_train, y_train, epochs=10)

# Making Predictions
tf_predictions = tf_model.predict(X_test)
print("TensorFlow Predictions:", tf_predictions)

# Data Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Scaled Features:", X_scaled)

# Saving and Loading Models
# Saving the scikit-learn Model
joblib.dump(model, 'linear_regression_model.pkl')

# Loading the Model
loaded_model = joblib.load('linear_regression_model.pkl')

# Evaluating the Model
score = loaded_model.score(X_test, y_test)
print("Model Score:", score)
