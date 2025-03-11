import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



df = pd.read_csv("/Users/devinreed/Downloads/INST414 - Python/Module 1/medianSalesPrice_All.csv")

#Isolating sales only in the borough of Manhattan
df_filtered = df[df['Borough'] == 'Manhattan']
#Cleaning the dataset by removing null values
#df_filtered = df_filtered.dropna()

#Filter to only include dates from 2019 to 2024
df_filtered = pd.concat([df_filtered.iloc[:, :3], 
                         df_filtered.loc[:, '2019-01':'2024-01']], axis=1)
df_filtered.to_csv("Manhattan_Covid.csv", index=False)


#Creating a Line graph that shows the price trends over time in main Manhatten submarkets
file_path = "/Users/devinreed/Downloads/INST414 - Python/Manhattan_Covid.csv"
df = pd.read_csv(file_path)

trend_data = df.iloc[:5, 3:].T  
trend_data.columns = df.iloc[:5, 0]  
trend_data.index = pd.to_datetime(trend_data.index, format='%Y-%m')  

plt.figure(figsize=(12, 6))
for column in trend_data.columns:
    plt.plot(trend_data.index, trend_data[column], label=column)

plt.title("Median Housing Prices in Manhatten Submarkets Through Covid-19")
plt.xlabel("Date")
plt.ylabel("Median Housing Price (in millions)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

submarket_df = df[df['areaType'] == 'submarket']

price_increase = submarket_df.iloc[:, -1] - submarket_df.iloc[:, 3]
max_submarket_index = price_increase.idxmax()
max_submarket_area = submarket_df.iloc[max_submarket_index, 0]
max_submarket_value = price_increase[max_submarket_index]

# Print the results
print(f"The submarket with the highest price increase over the time period is '{max_submarket_area}', "
      f"with an increase of ${max_submarket_value:,.2f}.")







