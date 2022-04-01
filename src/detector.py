import os
import matplotlib.pyplot as plt

from kit import get_KIT_features_F1_from_file
from util import pretty_print, list_avg
import seaborn as sns
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
    # TODO: Try using scipy gaussian_kde() instead of seaborn. Refrence: https://stackoverflow.com/questions/62375034/find-non-overlapping-area-between-two-kde-plots-in-python
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
    plt.legend(labels=["105", "106"])
    plt.show()
