from pyscript import display, document


def periodic_table(e):
    document.getElementById('result').innerHTML = ' '
    elements = document.getElementById('list').value.lower().strip()

    reactive_nonmetals = {
    'a': ['Hydrogen', 1, 1.008]
    'b': ['Phosphorus', 15, 30.974]
    'c': ['Bromine', 35, 79.960]
    'd': ['Carbon', 6, 12.011]
    'e': ['Nitrogen', 7, 14.007]
    'f': ['Sulfur', 16, 32.065]
    }