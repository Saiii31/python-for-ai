# Using external packages
# After installation, import and use:

# Web requests
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data)

# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)