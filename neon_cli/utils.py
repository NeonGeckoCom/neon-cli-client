import re


def remove_ssml(text):
    return re.sub('<[^>]*>', '', text).replace('  ', ' ')

