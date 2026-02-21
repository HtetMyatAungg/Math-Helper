from stat_helper import mean, std_dev, binomial, median,mode
from stat_helper.utils import load_data
import matplotlib.pyplot as plt
import pandas as pd

#from mathamatic structure review question
data = load_data("data.txt")

#Fair Coin 
n = 5
p = 0.5
k_values = list(range(n + 1))
probabilities = [binomial(n, p, k) for k in k_values]
print(f"mean: {mean(data)}")
print(f"probabilities: {probabilities}")
print(f"standard deviation: {std_dev(data)}")
print(f"median: {median(data)}")

result = []

result.append([mean(data), std_dev(data), median(data), mode(data)])


table = pd.DataFrame(result, columns=["Mean", "Standard Deviation", "Median", "Mode"])
print("Table")
print(table)

plt.bar(k_values, probabilities, color='skyblue', edgecolor='black')
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.xlabel('Number of Successes (k)')
plt.ylabel('Probability P(X=k)')
plt.xticks(k_values)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

table.to_csv("test.csv", index=False)