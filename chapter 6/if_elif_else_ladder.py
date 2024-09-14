a = int(input("Enter your age: "))

if(a>=18):
    print("You r above the age of consent.")
    print("Good for you.")


elif(a<0):
    print("You are not born yet.")

elif(a==0):
    print("You are a new born baby.")

else:
    print("You are a minor.")

print("Thank you for using the program.")