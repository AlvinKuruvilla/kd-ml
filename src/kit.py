import os
import numpy as np
import pandas as pd
from tqdm import tqdm

from util import count_matches

# get KIT feature based on current key and timing values
def get_timings_KIT(keys_in_pipeline, search_key, search_key_timing):
    mask = np.ones(len(keys_in_pipeline))
    keys_in_pipeline = np.asarray(keys_in_pipeline)
    for i, (key, timing) in enumerate(keys_in_pipeline):
        if search_key == key:
            mask[i] = 0
            non_zero_indices = np.nonzero(mask)

            if len(non_zero_indices) > 0:
                keys_in_pipeline = keys_in_pipeline[non_zero_indices]
            else:
                keys_in_pipeline = []

            return keys_in_pipeline, timing, search_key_timing
    return keys_in_pipeline, None, None


# function to get KIT data frame with key, press_time, release_time for a given user
def get_dataframe_KIT(data):
    """Input: data  Output: Dataframe with (key, press_time, release_time)"""
    keys_in_pipeline = []
    result_key = []
    press = []
    release = []
    for row_idx in range(len(data)):
        keys_in_pipeline = list(keys_in_pipeline)
        curr_key = data[row_idx][1]
        curr_direction = data[row_idx][2]
        curr_timing = data[row_idx][3]

        if curr_direction == 0:
            keys_in_pipeline.append([curr_key, curr_timing])

        if curr_direction == 1:
            keys_in_pipeline, curr_start, curr_end = get_timings_KIT(
                keys_in_pipeline, curr_key, curr_timing
            )
            if curr_start is None:
                continue
            else:
                result_key.append(curr_key)
                press.append(curr_start)
                release.append(curr_end)

    resultant_data_frame = pd.DataFrame(
        list(zip(result_key, press, release)),
        columns=["Key", "Press_Time", "Release_Time"],
    )
    return resultant_data_frame


# KIT feature (Digraph) extraction utilities

# function to get Flight1 KIT feature dictionary for a given user
def get_KIT_features_F1(data):
    """Input: keystroke data, Output: Dictionary of (next_key_press - current_key_release)"""
    feature_dictionary = {}

    for row_idx in range(0, len(data)):
        curr_key = data[row_idx][0]
        if row_idx + 1 >= len(data):
            break
        next_key = data[row_idx + 1][0]
        curr_timing = data[row_idx][2]
        next_timing = data[row_idx + 1][1]

        if str(curr_key) + str(next_key) in list(feature_dictionary.keys()):
            feature_dictionary[str(curr_key) + str(next_key)].append(
                int(float(next_timing)) - int(float(curr_timing))
            )
        else:
            feature_dictionary[str(curr_key) + str(next_key)] = []
            feature_dictionary[str(curr_key) + str(next_key)].append(
                int(float(next_timing)) - int(float(curr_timing))
            )

    return feature_dictionary


# function to get Flight2 KIT feature dictionary for a given user
def get_KIT_features_F2(data):
    """Input: keystroke data, Output: Dictionary of (next_key_press - current_key_press)"""
    feature_dictionary = {}

    for row_idx in range(0, len(data)):
        curr_key = data[row_idx][0]
        if row_idx + 1 >= len(data):
            break
        next_key = data[row_idx + 1][0]
        curr_timing = data[row_idx][1]
        next_timing = data[row_idx + 1][1]
        if str(curr_key) + str(next_key) in list(feature_dictionary.keys()):
            feature_dictionary[str(curr_key) + str(next_key)].append(
                int(float(next_timing)) - int(float(curr_timing))
            )
        else:
            feature_dictionary[str(curr_key) + str(next_key)] = []
            feature_dictionary[str(curr_key) + str(next_key)].append(
                int(float(next_timing)) - int(float(curr_timing))
            )

    return feature_dictionary


# function to get Flight3 KIT feature dictionary for a given user
def get_KIT_features_F3(data):
    """Input: keystroke data, Output: Dictionary of (next_key_release - current_key_release)"""
    feature_dictionary = {}

    for row_idx in range(0, len(data)):
        curr_key = data[row_idx][0]
        if row_idx + 1 >= len(data):
            break
        next_key = data[row_idx + 1][0]
        curr_timing = data[row_idx][2]
        next_timing = data[row_idx + 1][2]
        if str(curr_key) + str(next_key) in list(feature_dictionary.keys()):
            feature_dictionary[str(curr_key) + str(next_key)].append(
                int(float(next_timing)) - int(float(curr_timing))
            )
        else:
            feature_dictionary[str(curr_key) + str(next_key)] = []
            feature_dictionary[str(curr_key) + str(next_key)].append(
                int(float(next_timing)) - int(float(curr_timing))
            )

    return feature_dictionary


# function to get Flight4 KIT feature dictionary for a given user
def get_KIT_features_F4(data):
    """Input: keystroke data, Output: Dictionary of (next_key_release - current_key_press)"""
    feature_dictionary = {}

    for row_idx in range(0, len(data)):
        curr_key = data[row_idx][0]
        if row_idx + 1 >= len(data):
            break
        next_key = data[row_idx + 1][0]
        curr_timing = data[row_idx][1]
        next_timing = data[row_idx + 1][2]
        if str(curr_key) + str(next_key) in list(feature_dictionary.keys()):
            feature_dictionary[str(curr_key) + str(next_key)].append(
                int(float(next_timing)) - int(float(curr_timing))
            )
        else:
            feature_dictionary[str(curr_key) + str(next_key)] = []
            feature_dictionary[str(curr_key) + str(next_key)].append(
                int(float(next_timing)) - int(float(curr_timing))
            )

    return feature_dictionary


# TODO: We can further optimize the speed by using an enum to branch off which flight time calculations we wish to do


def get_all_users_features_KIT(directory, profile_path=None):
    users_feat_dict_f1 = {}
    users_feat_dict_f2 = {}
    users_feat_dict_f3 = {}
    users_feat_dict_f4 = {}
    user_files = os.listdir(directory)
    for i in tqdm(range(len(user_files))):
        user_file = user_files[i]
        data_frame = pd.read_csv(directory + user_file)
        data_frame = get_dataframe_KIT(data_frame.values)
        user_data = data_frame.values

        user_feat_dict_f1 = get_KIT_features_F1(user_data)
        if profile_path is not None:
            profile_df = pd.read_csv(profile_path)
            df = get_dataframe_KIT(profile_df.values)
            data = df.values
            features = get_KIT_features_F1(data)
            print("Running against profile: %s" % directory + user_file)
            kit_k, kit_v = count_matches(user_feat_dict_f1, features)
            print("Found", kit_k, "Flight 1 KIT key matches")
            print("Found", kit_v, "Flight 1 KIT value matches")

        users_feat_dict_f1[i + 1] = user_feat_dict_f1

        user_feat_dict_f2 = get_KIT_features_F2(user_data)
        users_feat_dict_f2[i + 1] = user_feat_dict_f2

        user_feat_dict_f3 = get_KIT_features_F3(user_data)
        users_feat_dict_f3[i + 1] = user_feat_dict_f3

        user_feat_dict_f4 = get_KIT_features_F4(user_data)
        users_feat_dict_f4[i + 1] = user_feat_dict_f4

    return (
        users_feat_dict_f1,
        users_feat_dict_f2,
        users_feat_dict_f3,
        users_feat_dict_f4,
    )
