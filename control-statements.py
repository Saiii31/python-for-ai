age=17

if age >= 18:
    print("You are an adult.")
    if age==18:
        print("You are 18 years old.")
elif age < 18 and age >= 13:
    print("You are a teenager.")
    if age==16:
        print("You are in 10th std")
    elif age<16:
        print("You are below 10th std")
    else:
        print("You are in college")
else:
    print("You are a child.")
    
    
    
