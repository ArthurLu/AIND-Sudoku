assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    result = []
    for box, val in zip(boxes, grid):
        if val == ".":
            result.append((box, cols))
        else:
            result.append((box, val))
    return dict(result)

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)

def eliminate(values):
    new_values = values.copy()
    for box in boxes:
        if len(values[box]) == 1:
            for peer in peers[box]:
                new_values[peer] = new_values[peer].replace(values[box], "")
    return new_values

def only_choice(values):
    new_values = values.copy()
    for unit in unitlist:
        for val in cols:
            candidates = [box for box in unit if val in values[box]]
            if len(candidates) == 1:
                new_values[candidates[0]] = val
    return new_values

def reduce_puzzle(values):
    pass

def search(values):
    pass

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    values = eliminate(values)
    return values



if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    boxes = cross(rows, cols)
    row_units = [cross(row, cols) for row in rows]
    col_units = [cross(rows, col) for col in cols]
    square_units = [cross(row, col) for row in ["ABC", "DEF", "GHI"] for col in ["123", "456", "789"]]
    unit_list = row_units + col_units + square_units
    units = dict((box, [unit for unit in unit_list if box in unit]) for box in boxes)
    peers = dict((box, set(sum(units[box],[]))-set([box])) for box in boxes)
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
