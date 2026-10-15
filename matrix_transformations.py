import matplotlib.pyplot as graph
from math import sin, cos, radians, isclose
from typing import List

class Matrix:
    """
    A class representing a 2D matrix to support algebraic operations 
    and geometric transformations.
    """
 
    def __init__(self, rows: List[List[float]]) -> None:
        """
        Initializes the Matrix object with a 2D list of numerical rows.
        Calculates and stores its dimensions as [m, n].
        """
        self.dimensions: List[int] = [len(rows), len(rows[0])]
        self.rows: List[List[float]] = rows

    def is_2d(self):
        return self.dimensions[0] == 2

    def is_multiplicable(self, m2: 'Matrix') -> bool:
        """
        Checks if this matrix can be multiplied by another matrix (self * m2).
        
        Args:
            m2 (Matrix): The second matrix to check multiplication compatibility with.
            
        Returns:
            bool: True if self*m2 can be computed.
        """
        return self.dimensions[1] == m2.dimensions[0]
    
    def multiply(self, m2: 'Matrix') -> 'Matrix':
        """
        Multiplies this matrix by another matrix in the order (self * m2).
        
        Args:
            m2 (Matrix): The matrix to multiply by.
            
        Returns:
            Matrix: A new Matrix representing the product.
        """
        resultant_matrix = Matrix([[0 for _ in range(m2.dimensions[1])] for _ in range(self.dimensions[0])])
        for x in range(self.dimensions[0]):
            for i in range(m2.dimensions[1]):
                new_element = sum(self.rows[x][n] * m2.rows[n][i] for n in range(m2.dimensions[0]))
                if isclose(new_element, round(new_element)):
                    new_element = round(new_element)
                resultant_matrix.rows[x][i] = new_element

        return resultant_matrix

    def scale_factor_2d(self) -> 'Matrix':
        """
        Applies a 2D scaling transformation from the origin.
        
        Args:
            scale_factor_x (float): Scaling factor along the x-axis.
            scale_factor_y (float): Scaling factor along the y-axis.
            
        Returns:
            Matrix: A new transformed Matrix.
        """

        if self.is_2d():
            while True:
                try:
                    scale_factor_x = float(input("Enter the x enlargement scale factor: "))
                    scale_factor_y = float(input("Enter the y enlargement scale factor: "))
                    break
                except ValueError:
                    print("Please enter a valid scale factor")
            sf_matrix = Matrix([[scale_factor_x, 0], [0, scale_factor_y]])
            return sf_matrix.multiply(self)
        print("This matrix is not 2d and therefore cannot be transformed this way\n")
    

    def rotation_2d(self) -> 'Matrix':
        """
        Applies a 2D rotation transformation around the origin anticlockwise.
        
        Args:
            theta (float): Angle of rotation in degrees.
            
        Returns:
            Matrix: A new transformed Matrix.
        """

        if self.is_2d():
            while True:
                try:
                    theta = float(input("Enter angle in degrees to rotate the matrix anticlockwise by: "))
                    break
                except ValueError:
                    print("Please enter a valid angle")
            theta_rad = radians(theta)
            rotation_matrix = Matrix([[cos(theta_rad), -sin(theta_rad)], [sin(theta_rad), cos(theta_rad)]])
            return rotation_matrix.multiply(self)
        print("This matrix is not 2d and therefore cannot be transformed this way\n")

def enter_matrix() -> Matrix:
    """
    prompts the user to input dimensions and elements for a new matrix
    with error handling for invalid inputs and accidental spaces inbetween inputs.
    
    Returns:
        Matrix: The constructed Matrix object.
    """
    # Validate row and column dimensions
    while True:
        try:
            rows = int(input('Number of rows: '))
            columns = int(input('Number of columns: '))
            if rows > 0 and columns > 0:
                break
            print("Dimensions must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    matrix: List[List[float]] = [[] for _ in range(rows)] 
    
    for i in range(rows):
        while True:
            try:
                elements = input(f"Enter all elements for row {i+1} separated by commas: ")
                elements = [float(x.strip()) for x in elements.split(",")]
                
                if len(elements) != columns:
                    print(f"Row must contain exactly {columns} elements.")
                else:
                    matrix[i] = elements
                    break
            except ValueError:
                print("Invalid input. Please ensure all elements are numbers separated by commas.")
                
    print('\n')
    return Matrix(matrix)

def show_matrix(matrix: Matrix) -> None:
    """
    Plots a 2D matrix's coordinates graphically using matplotlib.
    Only works for 2D matrices; assumes the input matrix is valid.
    
    Args:
        matrix (Matrix): The Matrix object to visualize.
    """
    co_ordinates = ['' for _ in range(len(matrix.rows[0]))]
    for i in range(len(matrix.rows[0])):
        co_ordinates[i] = [matrix.rows[k][i] for k in range(len(matrix.rows))]
    l1 = [co_ordinates[i][0] for i in range(len(co_ordinates))]
    l2 = [co_ordinates[i][1] for i in range(len(co_ordinates))]

    graph.plot(l1, l2, 'o')
    graph.show()

def transformation_options(m1: Matrix) -> Matrix:
    """
    Shows a menu of transformation options to the user and applies the selected one.
    
    Args:
        m1 (Matrix): The current matrix to transform.
        
    Returns:
        Matrix: The transformed Matrix object.
    """

    transformations = ['R for rotation around origin anticlockwise theta degrees', 'S for enlargement from origin']
    t_m1 = m1
    while True:
        for transformation in transformations:
            print(transformation)
        print('\n')
        choice = input('Enter transformation option: ')
        if choice == 'S':
            t_m1 = m1.scale_factor_2d()
            break
        elif choice == 'R':
            t_m1 = m1.rotation_2d()
            break
        else:
            print("Not a valid transformation\n")

    return t_m1

def main_loop() -> None:
    """
    Runs the main loop allowing users to create,
    view, transform, and plot matrices.
    """
    print("Please enter an initial matrix: ")
    m1 = enter_matrix()
    running_loop = True
    options = [
        'E to enter new matrix', 
        'V to view current matrix', 
        'T to choose transformation of current matrix (only works for 2d matrices!)', 
        'S to show current matrix graphically', 
        'Q to quit'
    ]
    while running_loop:
        for option in options:
            print(f"{option}")
        choice = input('\nEnter option: ')
        if choice == 'Q':
            running_loop = False
        elif choice == 'E':
            m1 = enter_matrix()
        elif choice == 'T':
            m1 = transformation_options(m1)
        elif choice == 'S':
            show_matrix(m1)
        elif choice == 'V':
            for row in m1.rows:
                print(row)
            print('\n')

if __name__ == '__main__': 
    main_loop()