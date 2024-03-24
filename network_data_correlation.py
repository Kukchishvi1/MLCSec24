import pandas as pd
import numpy as np

df = pd.read_csv('network_data.csv', header=None, names = ["Packet Size (bytes)", "Session Duration (minutes)", "Number of Errors", "Protocol (TCP-1, UDP-2, ICMP-3)"])

print(df)


# Compute Pearson correlation coefficient
pearson_corr = df.corr(method='pearson')

# Display the correlation matrix
print(pearson_corr)
