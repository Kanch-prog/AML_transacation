import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil.parser
from sklearn.preprocessing import StandardScaler

# Load a sample of the data into a DataFrame
file_path = "LI-Small_Trans.csv\LI-Small_Trans.csv"
df = pd.read_csv(file_path, dtype={
    'Amount Received': 'float32',  
    'Timestamp': 'str' 
}, nrows=100000) 

# Convert 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

#Checking for Missing Values
print("Checking for Missing Values:")
print(df.isnull().sum())

#Basic Statistics
print("\nBasic Statistics of Amount Received:")
print(df['Amount Received'].describe())

# Analyzing Temporal Trends
print("\nAnalyzing Temporal Trends:")
df.set_index('Timestamp', inplace=True)
monthly_trend = df['Amount Received'].resample('M').sum()
print(monthly_trend)

# Plot histogram of transaction amounts
plt.figure(figsize=(14, 7))

# Plot histogram of transaction amounts
plt.subplot(1, 2, 1)
plt.hist(df['Amount Received'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Transaction Amount (USD)')
plt.ylabel('Frequency')

# Plot line plot of transaction amounts over time
plt.subplot(1, 2, 2)
plt.plot(df['Timestamp'], df['Amount Received'], marker='o', color='salmon')
plt.title('Transaction Amounts Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Transaction Amount (USD)')
plt.xticks(rotation=45, ha='right')

# Format the x-axis to show dates clearly
ax = plt.gca()
xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
plt.gcf().autofmt_xdate()  # Auto format the x-axis labels

plt.tight_layout()

# Anomaly detection using StandardScaler
scaler = StandardScaler()
df['Amount Received_scaled'] = scaler.fit_transform(df[['Amount Received']])

# Print the anomalies found in the dataset
print("Anomalies:")
print(df[df['Amount Received_scaled'] > 3])  # Adjust the threshold as needed

plt.show()
