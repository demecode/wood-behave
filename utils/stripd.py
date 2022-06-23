import re


def only_numbers(value=None):

    return re.sub('[^0-9]', '', value)
