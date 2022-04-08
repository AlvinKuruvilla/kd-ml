import os
import matplotlib.pyplot as plt

from kit import get_KIT_features_F1_from_file
from util import pretty_print, list_avg
from plotter import *
import numpy as np

if __name__ == "__main__":
    dir_name = "data"
    dir_path = os.path.join(os.getcwd(), dir_name)
    selected_profile_path = os.path.join(dir_path, "Desktop/", "User105.csv")
    alternative_profile_path = os.path.join(dir_path, "Desktop/", "User106.csv")

    # The KIT version
    selected_profile_KIT_dictionary = get_KIT_features_F1_from_file(
        selected_profile_path
    )
    alt_profile_KIT_dictionary = get_KIT_features_F1_from_file(alternative_profile_path)
    selected_profile_data = list(selected_profile_KIT_dictionary.values())
    alt_profile_data = list(alt_profile_KIT_dictionary.values())
    processed_selected_profile_data = []
    processed_alt_data = []
    for dataset in selected_profile_data:
        processed_selected_profile_data.append(list_avg(dataset))
    for alt_dataset in alt_profile_data:
        processed_alt_data.append(list_avg(alt_dataset))

    # plot_kde_overlap(
    #     np.array(processed_alt_data),
    #     np.array(processed_selected_profile_data),
    #     "105",
    #     "106",
    # )
    # plot_Epanechnikov(np.array(processed_selected_profile_data))
    # plot_Epanechnikov(np.array(processed_alt_data))
    # FIXME: All the other plots except gaussian so far look the same
    plot_Biweight_equation_overlap(
        np.array(processed_selected_profile_data),
        np.array(processed_alt_data),
        "105",
        "106",
    )
