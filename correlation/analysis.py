#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import statsmodels.robust.scale as scale

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30]
y = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 50]

df = pd.DataFrame({"x": x, "y": y})
mean = df.mean()
median = df.median()
trimmed_mean = stats.trim_mean(df, 0.1)

print("Mean")
print("------------------------------------------")
print(mean)
print()

print("Median")
print("------------------------------------------")
print(median)
print()

print("Trimmed Mean")
print("------------------------------------------")
print(trimmed_mean)
print()

std = df.std()
iqr = df.quantile(0.75) - df.quantile(0.25)
mad = scale.mad(df)

quantiles = [0.1, 0.25, 0.5, 0.75, 0.9]
quantiles = df.quantile(quantiles)


print("Standard Deviation")
print("------------------------------------------")
print(std)
print()

print("IQR")
print("------------------------------------------")
print(iqr)
print()

print("MAD")
print("------------------------------------------")
print(mad)
print()

print("Quantiles")
print("------------------------------------------")
print(quantiles)
print()

df.plot(kind="box")
plt.show()

df["x"].plot.hist(figsize=(10, 10), bins=3)
plt.show()

df["y"].plot.hist(figsize=(10, 10), bins=3)
plt.show()
