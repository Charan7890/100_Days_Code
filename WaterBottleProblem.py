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
    
