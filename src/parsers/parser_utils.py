import os

from log import Logger


def is_csv_file(path: str) -> bool:
    """
    Check if a provided path is to a CSV file.
    Parameters
    ----------
    path: str
          The path to be checked.
    Returns
    -------
    bool
    """
    log = Logger("is_csv_file")
    is_file = os.path.isfile(path)
    if is_file:
        # Now check that the extension is CSV
        if path.lower().endswith(".csv"):
            return True
        else:
            log.km_fatal(path + ", is not a csv file")
            return False
    else:
        log.km_fatal(path + " , is not a file")
        return False


class NotCSVFileError(Exception):
    """Exception raised if provided path is not a csv file.
    Attributes:
        path -- input path which caused the error
        message -- explanation of the error
    """

    def __init__(self, path, message):
        self.path = path
        self.message = message
        super().__init__(self.message)
