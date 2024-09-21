num = int(input("Enter a Random Number: "))

list = []

for i in range(0, num + 1):
    list.append(i)


oddNum = [x for x in list if x % 2 != 0]
print("Odd Numbers:", oddNum)



#=============================================================================================


fruits = ["apple", "banana", "orange", "jackfruit", "grapes"]

upperCasedFruits = []

upperCasedFruits.append(fruits[0].capitalize())
upperCasedFruits.append(fruits[1].capitalize())
upperCasedFruits.append(fruits[2].capitalize())
upperCasedFruits.append(fruits[3].capitalize())
upperCasedFruits.append(fruits[4].capitalize())

print(f"The Updated Uppercased Fruits: {upperCasedFruits}")
