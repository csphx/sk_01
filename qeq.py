#!/usr/bin/env python3

'''
    https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-formula-a1/a/discriminant-review

    https://www.codewithrepl.it/01-introduction-to-the-repl-it-ide.html

    quadratic equation solver

    Edit_By ...... Stanley C. Kitching
    Edit_Date .... 2020-08-22

    Edit_Date .... 2024-02-29

      moved solver code into the function named solve_it

      use random integers for coefficients
      to be used to test the solver 
'''

from qeq_solver import solve_quadratic

from random import randint

from math import isnan


def solve_it( x , y , z ) : 

    answer  = solve_quadratic( x , y , z )

    x1 , x2 = answer

    print( f'\n    coefficients .... a = {x}   b = {y}   c = {z} ' )

    print( f'\n       solution ....  x1 :  {x1:.4f}   x2 :  {x2:.4f} ' )

    # print( f'\n     x2 :  {x2:.4f} '  )

    if isnan( x1 )  and  isnan( x2 ) : 

        print( '\n    discriminant  d = ( b ** 2 )  - 4 * a*c  <  0 ' )

        print( '\n      no real solutions ' )    



def test_01() : 

    print( '\n  solving quadratic equations of the form ' )

    print( '\n   ax² + bx + c = 0 ' )

    for n in range( 3 ) : 

        i = randint( 1 ,  5 ) 

        j = randint( 1 , 10 ) 

        k = randint( 1 ,  3 )

        solve_it( i , j , k )

        print( '\n  --------------------------------------------------- ' )


if __name__ == '__main__' : 

    test_01()


