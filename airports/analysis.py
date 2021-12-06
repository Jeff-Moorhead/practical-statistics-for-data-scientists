#!/usr/bin/env python3

import argparse

import matplotlib.pyplot as plt
import pandas as pd


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", default="dfw_airline.csv")

	return parser.parse_args()


if __name__ == "__main__":
	args = get_args()

	airline_stats = pd.read_csv(args.file)
	print("Airline Stats")
	print("-------------")
	print(airline_stats)
	print()

	print("Percentage of Delays by Cause")
	print("-----------------------------")
	print(airline_stats * 100 / airline_stats.values.sum())
	print()

	"""
	# If x is not specified to plot.bar(), the index of the dataframe is used.
	# To get our data into the index instead of as columns, we transpose the dataframe (swap rows for columns).
	ax = airline_stats.T.plot.bar(legend=False)
	ax.set_xlabel("Cause of Delay")
	ax.set_ylabel("Count")
	plt.show()
	"""

	# Expected value is a type of weighted mean in which each possible value is multiplied by its probability of occurring. The divisor is always 1 since
	# the probability of at least one of the events occurring is always 1 (i.e. the probability of all events must always add to 1).
	# Note that expected value does not work for airline delay cause because the data is not on the same scale (there are no comparible units based purely
	# on cause of delay). If the data instead reflected the number of minutes delayed in buckets (e.g. ten, twenty, and thirty minutes), then we could
	# calculate expected value. It doesn't make sense to say "the expected value of flight delay is 0.23 * 'Carrier' + 0.3 * 'ATC'...".
	probabilities = airline_stats / airline_stats.values.sum()
	
	print("Probability of Each Delay Cause Occurring")
	print("-----------------------------------------")
	print(probabilities)
	print()

	# Note: for the purposes of exploratory data analysis, the probablility of an event occurring is simply the proportion of occurrences of that event
	# in an experiment repeated an infinite number of times. For example, for our purposes, the probability of flipping heads on a coin is 50%.

