import json
import random
with open('datas.json','r') as file :
    content=file.read()

data=json.loads(content)
# Select a random question
random_ques = random.choice(data[0])  # Fixed key name

# Print the question and options
print("Question:", random_ques["question"])
for i, option in enumerate(random_ques["options"], 1):
    print(f"{i}. {option}")
# score=0
# for quest in data:
#     print(quest['question'])
#     for option in quest['options']:
#         print(option)
#     user_choice=(input("Enter the answer : "))
#     quest["user_choice"]=user_choice
#     if quest["user_choice"] == quest["correct_answer"] :
#         score=score+1
#         print("correct/.....")
#     else :
#         print(f"wrong ,the answer is { quest["correct_answer"]}")


# print(f"The total score is {score} / {len(data)}")
