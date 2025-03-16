for i in range(1,101):
    if i%3 == 0 and i%5 == 0: #It's imperative that this line of code comes first. Otherwise, it's only going to print Fizz or Buzz even for numbers divisible by both 3 and 5.
       print("FizzBuzz")
    
    if i%3 == 0:
        print("Fizz")

    elif i%5 == 0:
        print("Buzz")

    else:
        print(i)
