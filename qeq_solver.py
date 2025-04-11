#!/usr/bin/env python3

'''
    https://www.codewithrepl.it/01-introduction-to-the-repl-it-ide.html

    quadratic equation solver

    Edit_By ...... Stanley C. Kitching
    Edit_Date .... 2020-08-22

    Edit_Date .... 2024-02-29

      included check for negative discriminant
      which indicates  no real solutions 
'''

import math

def solve_quadratic( a , b , c ) :

    d = ( b ** 2 )  - 4 * a * c

    if d < 0 : 

       return float( 'nan' ) , float( 'nan' ) 

    else : 

        s1 = (- b + math.sqrt( d ) ) / ( 2 * a )

        s2 = (- b - math.sqrt( d ) ) / ( 2 * a )

        return s1 , s2


