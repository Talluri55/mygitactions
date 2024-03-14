correct_number = 5
guessed_number = input("guess the number between 1 to 10 > ")
guessed_num_as_int = int(guessed_number)
correct_number_as_string = str(correct_number)
if(guessed_num_as_int == correct_number):
    print("congrats you did a great job")
elif(guessed_num_as_int + 1 == correct_number):
    print("you were close, the correct number is was " + str(correct_number))
else:
    print("aplogies, you guessed the wrong number. but you were very close")

