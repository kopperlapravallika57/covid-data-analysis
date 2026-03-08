# COVID-19 Data Analysis Project
import pandas as pd
import matplotlib.pyplot as plt
print("COVID Data Analysis Project Started")
# Sample data (temporary until we download real dataset)
data = {
    "Country": ["India", "USA", "Brazil", "UK"],
    "Total_Cases": [45000000, 103000000, 38000000, 24000000]
}
# Create DataFrame
df = pd.DataFrame(data)
# Display the data
print(df)
# Plot graph
plt.bar(df["Country"], df["Total_Cases"])
plt.title("COVID-19 Total Cases by Country")
plt.xlabel("Country")
plt.ylabel("Total Cases") 
plt.show()