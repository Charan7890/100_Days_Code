Problem Statement:

Given a string containing letters followed by numbers, your task is to repeat each letter based on the number immediately following it. The number can be of any length (i.e., it can be more than one digit).

For example, if the input string is "a4b12c6", you need to repeat 'a' four times, 'b' twelve times, and 'c' six times, and concatenate these repetitions to form the final output.

Write a function repeat_characters(s) that takes such a string s as input and returns the expanded string with repeated characters.

Example:

Input:
"a4b12c6"

Output:
"aaaabbbbbbbbbbbbcccccc"
_----------+------------------------------------------------------------------------------------------------666
inp: list = list(input().strip())



alphabet: str = ""

num: int = 0

flag: bool = False # True/False/False

if inp[0].isnumeric():

  print("Invalid input")

   

else:

  # running loop all over the elements

  for val in range(len(inp)):

    # if a new alphabet encounters then flag will turned to Turned which helps in printing the letters.

    if flag==True:

      for x in range(num):

        print(alphabet,end=" ")

        # If for condition fails it runs else block.

      else:

        print()

        num = 0

        flag = False

        alphabet = ""

         

    # condition to check for an alpha in a list

    if inp[val].isalpha():

      alphabet = inp[val]  

    # condition to check for a number in a list

    if inp[val].isnumeric():    

      num = num*10 + int(inp[val]) 

    # Handling index out of range exception.

    try:

      if inp[val+1].isalpha():

        flag=True

    except:

      pass

      #print("Index out of range, known error")



  # Additional loop to print the missed element.

  for x in range(num):

        print(alphabet,end=" ")

