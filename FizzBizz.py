# -*- coding: utf-8 -*-

def fizzbizz(num):
    
    if num % 3 == 0 and num % 5 == 0 and num !=0:
        return 'FizzBizz'
    
    elif num % 3 == 0 and num != 0:
        return 'Fizz'

    elif num % 5 ==0 and num != 0:
        return 'Bizz'

    elif num == 0 :
        return 'ValueError'

    else :
        return num

