"""
412. Fizz Buzz
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""

"""
def fizzBuzz(n):

    re = []
    for i in range(n):
        value = i+1
        if value%5==0 and value%3==0:
            re.append('FizzBuzz')
            continue
        if value%5 == 0:
            re.append('Buzz')
            continue
        if value%3 == 0:
            re.append('Fizz')
            continue
        re.append(str(value))

    return (re)
"""

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    re = list(range(1,n+1))
    re = [str(i) for i in re]

    i = 2
    while i < n:
        re[i] = 'Fizz'
        i+=3

    i = 4
    while i < n:
        re[i] = 'Buzz'
        i+=5

    i = 14
    while i < n:
        re[i] = 'FizzBuzz'
        i+=15


    return (re)

print(fizzBuzz(15))