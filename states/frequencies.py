#!/usr/bin/env python3

import argparse

import matplotlib.pyplot as plt
import pandas as pd


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", default="state.csv")

	return parser.parse_args()


if __name__ == "__main__":
	args = get_args()
	states = pd.read_csv(args.file)
	binned_by_population = pd.cut(states["Population"], 10)  # Creates ten equal-width bins based on population.
	binned_by_population.value_counts()  # Counts the number of states in each population bin.

	# Creates a histogram of population. Histograms are made of equal-width bins and no white space appears between bins unless a bin is empty.
	# This is different from a bar chart, which has empty space between categories. Histograms are useful for turning continuous data into
	# categorical data.
	ax = (states["Population"] / 1_000_000).plot.hist()
	ax.set_xlabel("Population (millions)")
	plt.show()

	# Creates a density plot. This can be thought of as a smoothed histogram. Usually computed directly from the data using a kernel density estimate.
	# The y-axis of a density plot is the kernel density estimate for the probability density function for the x-variable (in this case population).
	# To convert this to an actual probability of a given x-value appearing in a specified range is found by taking the integral of the PDF from X1
	# to X2 (this is equivalent to the area under the curve of the density plot. For example, the probability that a state has a population between
	# 3 and 5 million people is approximately 0.16 or 16% (2 * 0.08 +- some rounding error).
	ax = (states["Population"] / 1_000_000).plot.hist(density=True)

	# The `ax` parameter allows superposition of plots on top of each other.
	(states["Population"] / 1_000_000).plot.density(ax=ax, xlim=[0, 40])
	ax.set_xlabel("Population (millions)")
	plt.show()

	# Creates a density plot of murder rate
	ax = states["Murder.Rate"].plot.hist(density=True, xlim=[0, 12], bins=range(1, 12))
	states["Murder.Rate"].plot.density(ax=ax)
	ax.set_xlabel("Murder Rate (per 100,000)")
	plt.show()

