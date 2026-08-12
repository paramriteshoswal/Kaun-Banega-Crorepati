print("lets start kaun banega crorepati!!")
sum=0
questions= ["What is the capital of France?",
            "Who wrote \"Hamlet\"?",
            "What is the chemical symbol for water?",
            "Which planet is known as the Red Planet?",
            "What is 2 + 2?",
            "What color do you get by mixing red and white?",
            "What is the largest mammal?",
            "What is the freezing point of water in Celsius?",
            "What word is spelled incorrectly in every dictionary?",
            "What goes up but never comes down?"]
options=[["A. London","B. Paris","C. Berlin","D. Madrid"],
         ["A. Charles Dickens","B. William Shakespeare","C. Jane Austen","D. Mark Twain"],
         ["A. H2O","B. CO2","C. O2","D. H2SO4"],
         ["A. Venus","B. Mars","C. Jupiter","D. Saturn"],
         ["A. 3","B. 4","C. 5","D. 6"],
         ["A. Green","B. Pink","C. Orange","D. Blue"],
         ["A. Elephant","B. Blue Whale","C. Giraffe","D. Polar Bear"],
         ["A. 0°C","B. 100°C","C. -40°C","D. 32°C"],
         ["A. Incorrectly","B. Correctly","C. Dictionary","D. None of the above"],
         ["A. Age","B. Height","C. Money","D. Time"]]
correct_answers=["B","B","A","B","B","B","B","A","A","A"]
import random
numbers=[ i for i in range(0,10)]
random.shuffle(numbers)
prize= [100000,200000,300000,500000,1000000,2000000,4000000,8000000,10000000,70000000]
ordinals=["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"]
def prefix(prize):
            if prize<10000000:
                  return f"{prize / 100000:g} Lakh Rupees"
            else:
                  return f"{prize / 10000000:g} Crore Rupees"
c=0
for i in numbers:
      print("Your ",ordinals[c]," question is on screen for ",prize[c])
      print(questions[numbers[i]])
      print(options[numbers[i]])
      answer=input("Enter A/B/C/D:").capitalize().strip()
      if answer==correct_answers[numbers[i]]:
              print("Congratulations! You have won",prefix(prize[c]))
              sum=prize[c]
              if i==9:
                        print("Congratulations! You have won the game and",prefix(prize[c]))
      else:
             print("Sorry, that's incorrect. The correct answer is", correct_answers[numbers[i]])
             print("You have won",prefix(sum))
             break      
      c+=1        
           
