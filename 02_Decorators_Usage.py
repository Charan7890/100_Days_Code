from typing import Callable as c

# Decorators

def decor(norm: c[[int,int], int]) -> c[[int,int], int]:

  def wrapper(*args):

    x : int = len(args)

    sum : int = norm(*args)

    print(f"{norm.__name__} has {x} arguments. And the sum is: {sum}")

  return wrapper


@decor

def func(a : int,b : int) -> int:

  return a+b


def main() -> None:

  #print("hello")

  a : int = int(input())

  b : int = int(input())

   

  func(a,b)

if __name__ == "__main__":

  main()

   
