def isAnagram(str1:str, str2:str)->bool:
    if len(str1) != len(str2):
        return False
    count = {}
    for char in str1:
        count[char] = count.get(char, 0) + 1
    for char in str2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return all(value == 0 for value in count.values())

if __name__ == "__main__":
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    if isAnagram(str1, str2):
        print(f'"{str1}" and "{str2}" are anagrams.')
    else:
        print(f'"{str1}" and "{str2}" are not anagrams.')