import csv


def get_csv_data_by_file(file_handle) -> list:
    """
    Returns CSV data for input file handle
    :param file_handle: argparse.FileType("r")
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
    Returns CSV data for input file name
    :param file_name:
    :return:
    """
    with open(file_name, "r") as file:
        reader = csv.DictReader(file, quoting=csv.QUOTE_NONNUMERIC)
        dict_list = []
        for line in reader:
            dict_list.append(line)

    return dict_list
