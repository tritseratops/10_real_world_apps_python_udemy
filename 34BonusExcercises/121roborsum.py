import re

class Robot:

    def __init__(self):
        pass

    def speak(self, query):
        num1, num2 = re.finditer(r"\d+", query)
        num1 = int(str(num1.group(0)))
        num2 = int(str(num2.group(0)))
        return num1+num2

robot = Robot()
print(robot.speak("What is the sum of 1 and 2"))
print(robot.speak("What is the sum of 8 and 10"))