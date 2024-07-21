boy: list = list(input("Enter your name:").strip().lower())

girl: list = list(input("Enter your partner name:").strip().lower())



# Cancelling common characters among the names(one---one)

for i in range(len(boy)):
    for j in range(len(girl)):
        if boy[i]==girl[j]:
            boy[i],girl[j]='@','@'
            break
        elif boy[i]=='@':
            break

# print(boy, girl)
# Counting characters other than '@'
charCount: int = 0
for i in boy:
    if i!='@':
        charCount+=1

for i in girl:
    if i!='@':
        charCount+=1
# print(charCount)

flames: list = list("FLAMES")

# logic for cancelling the character based on charCount.
count: int = len(flames)
while len(flames)!=1:

    reminder: int = charCount%count

    if reminder==0:
        flames.pop()
    else:
        flames.pop(reminder-1)
        flames = flames[reminder-1:]+flames[:reminder-1]

    print(flames)

    count-=1

print(flames)




    








