
# TODO: Step 1 - return shape from user input (it can't be blank and must be a valid shape!)
def get_shape():
    valid_shapes = ['triangle', 'square', 'pyramid']
    while True:
        shape_input = input('Enter shape: ').strip().lower()
        if shape_input == '':
            continue

        if shape_input in valid_shapes:
            return shape_input


# TODO: Step 2 - return height from user input (it must be int!)
#       The maximum possible height must be 80
def get_height():
    height_input = input('Enter height: ')
    while True:
        if not height_input and not height_input.isdigit():
            continue

        return int(height_input)


# TODO: Step 3 Complete the required shapes below
#       with reference to the unittests
def draw_square(height):
    if height and isinstance(height, int):
        for i in range(height):
            for j in range(height):
                print('*', end='')
            print()


def draw_triangle_reversed(height):
    if height and isinstance(height, int):
        for i, val in enumerate(range(height, 0, -1)):
            for _ in range(val):
                print(i+1, end=' ')
            print()


def draw_triangle(height):
    '''1 
1 2 
1 2 3 '''
    if height and isinstance(height, int):
        for i in range(height):
            for k in range(i+1):
                print(k+1, end='')
            print('')


def draw_triangle_multiplication(height):
    pass


def draw_pyramid(height):
    pass


def draw_triangle_prime(height):
    """ 
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    In Python, prime numbers are essential in various mathematical and computational applications. They play a
    fundamental role in number theory, cryptography, and data security.

    Prime numbers are characterized by the following properties:
    1. They are integers greater than 1.
    2. They have exactly two positive divisors: 1 and the number itself.
    3. They cannot be divided evenly by any other positive integer except 1 and itself.

    For example, some prime numbers are 2, 3, 5, 7, 11, 13, 17, and so on. Non-prime numbers are called composite
    numbers and have more than two positive divisors.

"""
    pass


# TODO: Step 4 - add support for other shapes
def draw(shape, height):
    if shape == "pyramid":
        draw_pyramid(height)


# TODO: Step 5 (standalone function) - Solve The Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    return ""


if __name__ == "__main__":
    # shape_param = get_shape()
    # height_param = get_height()
    # draw(shape_param, height_param)
    draw_triangle(4)
