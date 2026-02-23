import random

#returns a list of the given index value from a list of tuples
def split_index_from_table(table, index):
    split_table = []
    for tup in table:
        split_table.append(tup[index])
    return split_table

def a_or_an(str):
    vowels = ['a','e','o','i','u']
    if str[0] in vowels:
        return "an"
    return "a"

def get_table_category(table):
    
    chosen_category = random.choices(
        population=split_index_from_table(table, 0),
        weights=split_index_from_table(table, 1)
    )
    
    return chosen_category[0]
