################################################################################
# Name        : string_utilities
# Description : Includes a few useful functions for making string prettier.
# Version     : 0.0.0
# Created On  : 2019-01-10
# Modified On : 2019-01-10
# Author      : Hamid R. Darabi, Ph.D.
################################################################################

import numpy as np
import pandas as pd
import locale
import string

locale.setlocale(locale.LC_ALL, 'en_US')


def get_formatted(input_number):
    """
    Adds commas for every three 0s
    :param input_number: input number
    :return: string
    """
    string_with_commas = locale.format_string("%d", input_number, grouping = True)
    return string_with_commas


def get_data_frame_count(data_frame):
    # ToDo: It's not a string utility. Refactor to aws utilities.
    """
    Prints the value counts for each column of a data frame.
    :param data_frame: input data frame
    :return: prints the value counts for each column
    """
    for NextColumn in data_frame.columns:
        print(data_frame.loc[:, NextColumn].value_counts().apply(get_formatted))
        print("\n")


def find_nth_index(in_this_string, find_this_string, nth_index):
    """
    finds the nth occurrence of an string in another one
    :param in_this_string: the source string to be searched
    :param find_this_string: the string to search for
    :param nth_index: the n number
    :return:
    """
    start = in_this_string.find(find_this_string)
    while start >= 0 and nth_index > 1:
        start = in_this_string.find(find_this_string, start + 1)
        nth_index -= 1
    return start


def get_s3_bucket_key(s3_path_without_file):
    """
    Generates bucket name and key name from a S3 string
    :param s3_path_without_file: the raw s3 string
    :return: bucket, and key
    """
    # ToDO: This one can be refactored to AWS utility if necessary.
    _path = str(s3_path_without_file).lower()
    second_slash = find_nth_index(_path, "/", 2)
    third_slash = find_nth_index(_path, "/", 3)
    _bucket = s3_path_without_file[(second_slash + 1): third_slash]
    _key = s3_path_without_file[(third_slash + 1):]

    return _bucket, _key


def rand_str(string_length):
    """
    generates a random string of lower cases of specified length
    :param string_length: length of the string
    :return: string of length n
    """
    return ''.join([np.random.choice([c for c in string.ascii_lowercase])
                    for i in range(string_length)])


if __name__ == "__main__":
    print("please import this script in my_shared_library")
