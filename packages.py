#  Built in Packages -

import math
math.sqrt(16)

# ------------------------------------------------------------------------

from math import sqrt
result = sqrt(25)  # if added from math import sqrt then we can use sqrt() directly without math.sqrt()
print(result)

# --------------------------------------------------------------------
# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])
print("Random number:", number)
print("Random choice:", choice)

# --------------------------------------------------------------------
# Common built-in packages in Python

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

print(json_string)

# --------------------------------------------------------------------
# Different ways to import packages

# Import entire module
import math
result = math.sqrt(16)

# Import specific functions
from math import sqrt, pi
result = sqrt(16)
radius = 5
circle_area = pi * radius ** 2
print(circle_area)

# Import with alias

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

# Import everything (avoid this!)
from math import *