from tqdm import tqdm
import os
import sys
import matplotlib.pyplot as plt

from kht import get_all_users_features_KHT, get_all_users_features_KHT_from_file
from kit import get_all_users_features_KIT
from util import count_matches, pretty_print, list_avg
from plotter import make_line_graph, make_kde
import seaborn as sns
import numpy as np

if __name__ == "__main__":
    dir_name = "data"
    dir_path = os.path.join(os.getcwd(), dir_name)
    selected_profile_path = os.path.join(dir_path, "Desktop/", "User105.csv")
    # The KHT version

    # selected_profile_KHT_dictionary = get_all_users_features_KHT_from_file(
    #     selected_profile_path
    # )
    user_files = os.listdir(os.path.join(dir_path, "Desktop/"))
    # # pretty_print(get_all_users_features_KHT(user_files))
    # # pretty_print(get_all_users_features_KIT(user_files)[0])
    for i in tqdm(range(len(user_files))):
        user_file = user_files[i]
        # current_KHT_dict = get_all_users_features_KHT_from_file(
        #     os.path.join(dir_path, "Desktop/", user_files[i])
        # )
        #     print("Running against profile: %s" % user_file)
        # k, v = count_matches(selected_profile_KHT_dictionary, current_KHT_dict)
        #     print("Found", k, "key matches")
        #     print("Found", v, "value matches")
        # make_histogram(current_KHT_dict)
    # The KIT version
    profiles = get_all_users_features_KIT(
        os.path.join(dir_path, "Desktop/"), selected_profile_path
    )
    processed_KIT = {}
    current_KIT = profiles[0]
    KIT_values = list(current_KIT.values())
    KIT_keys = list(current_KIT.keys())
    for i in KIT_values:
        vals = dict(i)
        for k, v in vals.items():
            processed_KIT[k] = list_avg(v)
    # for i in range(len(KIT_keys)):
    #     processed_KIT[KIT_keys[i]] = list_avg(KIT_values[i])
    pretty_print(processed_KIT)
    # make_line_graph(processed_KIT)
    data = list(processed_KIT.values())
    sns.set_style("whitegrid")
    plot = sns.kdeplot(np.array(data), bw=0.5)
    plt.show()
