from tqdm import tqdm
import os

from kht import get_all_users_features_KHT, get_all_users_features_KHT_from_file
from kit import get_all_users_features_KIT
from util import count_matches, pretty_print, list_avg

if __name__ == "__main__":
    dir_name = "data"
    dir_path = os.path.join(os.getcwd(), dir_name)
    selected_profile_path = os.path.join(dir_path, "Desktop/", "User105.csv")
    selected_profile_KHT_dictionary = get_all_users_features_KHT_from_file(
        selected_profile_path
    )
    user_files = os.listdir(os.path.join(dir_path, "Desktop/"))
    # pretty_print(get_all_users_features_KHT(user_files))
    # pretty_print(get_all_users_features_KIT(user_files)[0])
    for i in tqdm(range(len(user_files))):
        user_file = user_files[i]
        current_KHT_dict = get_all_users_features_KHT_from_file(
            os.path.join(dir_path, "Desktop/", user_files[i])
        )
        print("Running against profile: %s" % user_file)
        k, v = count_matches(selected_profile_KHT_dictionary, current_KHT_dict)
        print("Found", k, "key matches")
        print("Found", v, "value matches")
