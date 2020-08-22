'''
    https://www.codewithrepl.it/01-introduction-to-the-repl-it-ide.html

    quadratic equation solver
    
    Edit_By ...... Stanley C. Kitching
    Edit_Date .... 2020-08-22
'''

import math

def solve_quadratic( a , b , c ) :

    d = ( b ** 2 )  - 4 * a * c

    s1 = (- b + math.sqrt( d ) ) / ( 2 * a )

    s2 = (- b - math.sqrt( d ) ) / (2 * a)

    return s1, s2

