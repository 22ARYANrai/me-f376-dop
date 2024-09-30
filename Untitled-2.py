import numpy as np

# Generate example time data (in seconds)
time = np.arange(0, 10, 0.5)  # Time from 0 to 10 seconds with a step of 0.5 seconds

# Example acceleration function: acc = 9.8 * cos(0.5 * time)
acc = 9.8 * np.cos(0.5 * time)

# Create a DataFrame with the generated data
data = {
    "time": time,
    "acc": acc
}

df = pd.DataFrame(data)

# Save the DataFrame to an Excel file without headers
file_path = '/mnt/data/generated_time_acc_data.xlsx'
df.to_excel(file_path, header=False, index=False)

file_path
