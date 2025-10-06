def are_anagrams(str1, str2):
    """
    Check if two strings are anagrams.
    """
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    if are_anagrams(str1, str2):
        print(f'"{str1}" and "{str2}" are anagrams.')
    else:
        print(f'"{str1}" and "{str2}" are not anagrams.')