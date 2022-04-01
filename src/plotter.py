import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde


def make_line_plot(data: dict):
    """A line graph based histogram representation"""
    lists = sorted(data.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    plt.gca().xaxis.set_major_locator(MaxNLocator(prune="lower"))
    plt.gca().yaxis.set_major_locator(MaxNLocator(prune="lower"))

    plt.plot(x, y)
    plt.show()


def plot_kde_overlap(x, y, xlabel, ylabel):
    kde0 = gaussian_kde(x, bw_method=0.3)
    kde1 = gaussian_kde(y, bw_method=0.3)

    xmin = min(x.min(), y.min())
    xmax = max(x.max(), y.max())
    dx = 0.2 * (xmax - xmin)  # add a 20% margin, as the kde is wider than the data
    xmin -= dx
    xmax += dx

    x = np.linspace(xmin, xmax, 500)
    kde0_x = kde0(x)
    kde1_x = kde1(x)
    inters_x = np.minimum(kde0_x, kde1_x)

    plt.plot(x, kde0_x, color="b", label=xlabel)
    plt.fill_between(x, kde0_x, 0, color="b", alpha=0.2)
    plt.plot(x, kde1_x, color="orange", label=ylabel)
    plt.fill_between(x, kde1_x, 0, color="orange", alpha=0.2)
    plt.plot(x, inters_x, color="r")
    plt.fill_between(
        x,
        inters_x,
        0,
        facecolor="none",
        edgecolor="r",
        hatch="xx",
        label="intersection",
    )
    area_inters_x = np.trapz(inters_x, x)

    handles, labels = plt.gca().get_legend_handles_labels()
    labels[2] += f": {area_inters_x * 100:.1f} %"
    plt.legend(handles, labels, title="Survived?")
    plt.title("Fare vs Survived")
    plt.tight_layout()
    plt.show()


def calculate_kde_overlap(x, y):
    kde0 = gaussian_kde(x, bw_method=0.3)
    kde1 = gaussian_kde(y, bw_method=0.3)

    xmin = min(x.min(), y.min())
    xmax = max(x.max(), y.max())
    dx = 0.2 * (xmax - xmin)  # add a 20% margin, as the kde is wider than the data
    xmin -= dx
    xmax += dx

    x = np.linspace(xmin, xmax, 500)
    kde0_x = kde0(x)
    kde1_x = kde1(x)
    inters_x = np.minimum(kde0_x, kde1_x)
    return inters_x
