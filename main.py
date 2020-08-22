'''
    https://www.codewithrepl.it/01-introduction-to-the-repl-it-ide.html

    Edit_By ...... Stanley C. Kitching
    Edit_Date .... 2020-08-22
'''

from solver import solve_quadratic

a = 20
b = 24
c = 4

answer = solve_quadratic( a , b , c )

print( '\n  quadratic solver ....' )

print( '\n     a = {0}   b = {1}   c = {2} '.format( a , b , c ) )

print( '\n  answer .... ' )

print( '\n    x1 ' , answer[ 0 ] )

print( '\n    x2 ' , answer[ 1 ] )

