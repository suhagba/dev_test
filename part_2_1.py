"""
Fix up this code so that it is well formatted (eg. PEP 8 and similar good practices).

answer:
    - using VS code set up the PEP8 code format either by using pip install pep8 
        or set up editor formating settings in the editor config file.
    - setting up max length to 72 characters 
        "python.formatting.autopep8Args": ["--max-line-length", "72", "--experimental"]
    - Same way we can set up tabs as well according to PEP8 standards.
    - lasty use the editor menu option to auto format the code to PEP8 standard (shift + Alt + F)
"""
import random


def print_average():
    """Prints the average of a random list 100 times
    """
    for i in range(100):
        values = [random.random() for item in range(20)]
        average = sum(values) / len(values)
        print(f"The average of the random list is {average}")


print_average()


