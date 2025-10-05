'''Question: Water Bottle Exchange Problem

You are given a certain amount of money (in rupees) and the cost of exchanging empty bottles for a new full bottle. Each bottle costs 1 rupee, and after drinking, you can exchange a certain number of empty bottles (given as e) for one new full bottle. Write a program that calculates the maximum number of water bottles you can drink with the given amount of money and exchange rate. If the exchange rate is 1, the process would go into an infinite loop, so handle this as an exception.

Input: Two integers separated by a space: the amount of money (n) and the exchange rate (e).
Output: The maximum number of bottles that can be consumed.'''

def maxBottles(n:int, e:int) -> None:

    noOfBottles = n

    backupValue = n

    if e==1:

        print("It will enter to into an infinite loop so i am breaking it here(exception)")

    else:

        while n>=e:

            rem = n%e  # extra bottles

            newBottles = n//e # purchased bottles fater the exchange.

            noOfBottles += newBottles

            n = newBottles + rem
    
        print(f"Max no. of bottles can be purchased with {backupValue} is {noOfBottles}")


if __name__ == "__main__":

    n,e = list(map(int, input("Enter two values sepearing with space( first value: rupees(int); second value: exchange(int)):").split()))

    maxBottles(n,e)
    
