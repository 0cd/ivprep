#!env python

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

--

Solution -
Create a generator that accepts a limit and yields the lower of the next multiple of 3 or 5.
Stops once the next value is no longer less than the limit.
'''

def createGeneratorForMultiplesOf3Or5(limit):
    m3 = m5 = 0
    while True:
        if (m3 == m5):
            m = m3
            m3, m5 = m3 + 3, m5 + 5
        elif (m3 < m5):
            m = m3
            m3 += 3
        else:
            m = m5
            m5 += 5
        if (m < limit):
            yield m
        else:
            break


if __name__ == "__main__":
    print("Sum of all multiples of 3 or 5 below 10   :", sum(createGeneratorForMultiplesOf3Or5(10)))
    print("Sum of all multiples of 3 or 5 below 1000 :", sum(createGeneratorForMultiplesOf3Or5(1000)))

'''Output
Sum of all multiples of 3 or 5 below 10   : 23
Sum of all multiples of 3 or 5 below 1000 : 233168
'''