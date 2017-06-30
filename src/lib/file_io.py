import csv


def get_csv_data_by_file(file_handle) -> list:
    """

    :param file_handle:
    :return:
    """
    with file_handle as file:
        reader = csv.DictReader(file, quoting=csv.QUOTE_NONNUMERIC)
        dict_list = []
        for line in reader:
            dict_list.append(line)

    return dict_list


def get_csv_data_by_filename(file_name: str):
    """

    :param file_name:
    :return:
    """
    with open(file_name, "r") as file:
        reader = csv.DictReader(file, quoting=csv.QUOTE_NONNUMERIC)
        dict_list = []
        for line in reader:
            dict_list.append(line)

    return dict_list
