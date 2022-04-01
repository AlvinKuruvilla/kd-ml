import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import scipy.stats as stats
import pandas as pd


def make_line_plot(data: dict):
    """A line graph based histogram representation"""
    lists = sorted(data.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    plt.gca().xaxis.set_major_locator(MaxNLocator(prune="lower"))
    plt.gca().yaxis.set_major_locator(MaxNLocator(prune="lower"))

    plt.plot(x, y)
    plt.show()
