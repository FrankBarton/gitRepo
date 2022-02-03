import pyttsx3
if __name__ == '__main__':
    teacher = pyttsx3.init()
    teacher.say("你好！")
    teacher.runAndWait()
    teacher.stop()