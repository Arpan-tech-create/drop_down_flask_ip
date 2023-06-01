import pandas as pd

# Sample data
data = {
    'IP': ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5'],
    'MESSAGE': ['Message 1', 'Message 2', 'Message 3', 'Message 4', 'Message 5'],
    'ID': [1, 2, 3, 4, 5],
    'RESPONSE': ['Response 1', 'Response 2', 'Response 3', 'Response 4', 'Response 5']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)
df.to_csv('sample.csv')
