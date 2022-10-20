import gtts
from playsound import playsound
said_the_right_thing = False
while not said_the_right_thing:
    question = input("Won't you take me with you")
    good_answers = ["yes", "ok", "yeah" "yup", "ok", "fine", "sure"]
    if question.lower() in good_answers:
        said_the_right_thing = True

