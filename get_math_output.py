from subprocess import *
def math(number):
#    rezults = check_output(["C:\Users\Shakirov Farit\Desktop\math_function.exe", number]).split('\r\n')
#    rezults.pop()
    rezults = []
    for i in range(0,5):
        rezults.append('Hello, %s'%number)
    return rezults

rezult = math("-4.8")
print rezult

