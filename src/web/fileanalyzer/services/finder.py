from datetime import datetime
from os import listdir
from os.path import getatime, getmtime, getsize
from pathlib import Path

import polars as pl

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class Finder:
    """
    A class to find and retrieve information about files and folders.
    """

    def __init__(self) -> None:
        """
        Initializes the Finder object.

        Args:
            path (str): The path to the directory or file.
        """

    def get_results(self, path: str) -> None:
        """
        Creates a DataFrame of file and folder information.

        Args:
            path (str): The path to the directory.

        Raises:
            Exception: If the directory is empty.
        """

        path = Path(path)
        if path.is_dir():
            if listdir(path) == []:
                raise Exception("Directory is empty")
            else:
                elements_info = []
                for element in path.iterdir():
                    if element.is_file() and not element.name.startswith("."):
                        element_type = "File"
                    elif element.is_dir():
                        element_type = "Folder"
                    else:
                        element_type = "Unknown"

                    element_size = getsize(element)
                    element_access_time = datetime.fromtimestamp(
                        getatime(element)
                    ).strftime(DATETIME_FORMAT)
                    element_modification_time = datetime.fromtimestamp(
                        getmtime(element)
                    ).strftime(DATETIME_FORMAT)

                    elements_info.append(
                        {
                            "name": element.name,
                            "type": element_type,
                            "size": element_size,
                            "path": str(element),
                            "extension": element.suffix.lower()
                            if len(element.suffix) > 0
                            else "-",
                            "last_access": element_access_time,
                            "last_modified": element_modification_time,
                        }
                    )
        else:
            raise Exception("Path is not a directory")

        return elements_info

    def filter_elements(self, filter_by: str, value: str) -> dict:
        """
        Filters the results by the specified column and value.

        Args:
            filter_by (str): The column to filter by.
            value (str): The value to filter by.

        Returns:
            dict: A dictionary of filtered file and folder information.
        """
        result = self.results_table.filter(pl.col(filter_by) == value).to_dict(
            as_series=False
        )
        return result

    def save_to_csv(self, path) -> None:
        """
        Saves the results to a CSV file at the specified path.

        Args:
            path (str): The path where the CSV file will be saved.
        """
        self.results_table.write_csv(path)
