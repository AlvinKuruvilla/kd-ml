import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
from enum import Enum
from scipy.stats import gaussian_kde
from KDEpy import FFTKDE
import seaborn as sns


class KDE_Type(Enum):
    Guassian = 1
    Epanechnikov = 2
    Unifrm = 3  # FIXME: Unimplemented
    Triangular = 4
    Biweight = 5
    Triweight = 6
    Cosine = 7
    Cosine2 = 8  # FIXME: Unimplemented
    Tricube = 9


def make_line_plot(data: dict):
    """A line graph based histogram representation"""
    lists = sorted(data.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    plt.gca().xaxis.set_major_locator(MaxNLocator(prune="lower"))
    plt.gca().yaxis.set_major_locator(MaxNLocator(prune="lower"))

    plt.plot(x, y)
    plt.show()


def basic_kde(processed_selected_profile_data, processed_alt_data):
    sns.set_style("whitegrid")
    sns.kdeplot(
        np.array(processed_alt_data), bw_method=0.5, fill=True, legend=True, shade=1
    )
    sns.kdeplot(
        np.array(processed_selected_profile_data),
        bw_method=0.5,
        fill=True,
        legend=True,
        shade=1,
    )


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


def plot_Epanechnikov(data):
    # FIXME: What does the parameter to the evaluate() function do?
    x, y = FFTKDE(bw=1, kernel="epa").fit(data, weights=None).evaluate(2**8)
    plt.plot(x, y)
    plt.tight_layout()
    plt.show()


def plot_Triangular(data):
    x, y = FFTKDE(bw=1, kernel="tri").fit(data, weights=None).evaluate(2**8)
    plt.plot(x, y)
    plt.tight_layout()
    plt.show()


def plot_Biweight(data):
    x, y = FFTKDE(bw=1, kernel="biweight").fit(data, weights=None).evaluate(2**8)
    plt.plot(x, y)
    plt.tight_layout()
    plt.show()


def plot_Tricube(data):
    x, y = FFTKDE(bw=1, kernel="tricube").fit(data, weights=None).evaluate(2**8)
    plt.plot(x, y)
    plt.tight_layout()
    plt.show()


def plot_Triweight(data):
    x, y = FFTKDE(bw=1, kernel="triweight").fit(data, weights=None).evaluate(2**8)
    plt.plot(x, y)
    plt.tight_layout()
    plt.show()


def plot_Cosine(data):
    x, y = FFTKDE(bw=1, kernel="cosine").fit(data, weights=None).evaluate(2**8)
    plt.plot(x, y)
    plt.tight_layout()
    plt.show()
