#!/usr/bin/env python3

import argparse

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.robust.scale as scale
import wquantiles


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", type=str, default="state.csv")

	return parser.parse_args()


if __name__ == "__main__":
	args = get_args()
	data = pd.read_csv(args.file)

	avg_population = data["Population"].mean()

	# Median and trimmed mean are robust measures of location
	median_population = data["Population"].median()
	trimmed_avg_population = stats.trim_mean(data["Population"], 0.1)  # Removes the top and bottom 10% of records from the data set
	
	avg_murder_rate = data["Murder.Rate"].mean()
	median_murder_rate = data["Murder.Rate"].median()
	weighted_avg_murder_rate = np.average(data["Murder.Rate"], weights=data["Population"])
	weighted_median_murder_rate = wquantiles.median(data["Murder.Rate"], weights=data["Population"])

	# Both variance and standard deviation are sensitive to outliers. IQR (or any comparison based on percentiles) and MAD are more robust measurements.
	variance_population = data["Population"].var()  # Sum of squared deviations divided by n - 1
	standard_deviation_population = data["Population"].std()  # Square root of variance
	iqr_population = data["Population"].quantile(0.75) - data["Population"].quantile(0.25)  # Difference between 75th and 25th percentile (25th percentile = 0.25 quantile)
	mad_population = scale.mad(data["Population"])  # Median absolute deviation from the median

	print(f"Average population: {avg_population}")
	print(f"Median population: {median_population}")
	print(f"Trimmed average population: {trimmed_avg_population}")
	print("----------------------------------------------------------------------")
	print(f"Average murder rate per 100k people: {avg_murder_rate}")
	print(f"Median murder rate per 100k people: {median_murder_rate}")
	print(f"Average murder rate weighted by population: {weighted_avg_murder_rate}")
	print(f"Median murder rate weighted by population: {weighted_median_murder_rate}")
	print("----------------------------------------------------------------------")
	print(f"Variance for population: {variance_population}")
	print(f"Standard deviation for population: {standard_deviation_population}")
	print(f"Population IQR: {iqr_population}")
	print(f"Median absolute deviation from the median: {mad_population}")

	quantiles = data["Murder.Rate"].quantile([0.05, 0.25, 0.5, 0.75, 0.95])

	print(f"Murder rate quantiles:")
	print(quantiles)

	# The whiskers on a box plot generally do not go past 1.5 x IQR (this is true for both the R and matplotlib implementations).
	ax = (data["Population"] / 1_000_000).plot.box(vert=False)
	ax.set_ylabel("Population (millions)")
	plt.show()
	

