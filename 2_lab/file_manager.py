import os
import shutil
import sys

def mkfold(folder_name):
    try:
        os.mkdir(folder_name)
    except:
        pass

def rmfold(folder_name):
    try:
        shutil.rmtree(folder_name)
    except:
        pass
def cf(path):

    OS = sys.platform
    if OS == 'darwin':
        symbol = '/'

    elif OS == 'cygwin' or OS == 'win32' :
        symbol = "\\"

    else:
        symbol = "/"

    if path == "-":

        p = str(os.getcwd())
        p = p.split(symbol)
        p[0] = ""
        p[-1] = ""

        if len(p)-1 > tr_len:

            sum = ""
            for i in range(len(p)):
                sum = sum + symbol + p[i]
            sum = sum[1::]

            os.chdir(sum)
        else:
            print('Дальше нельзя')

    elif  "."+symbol in path:
        p = str(os.getcwd())+symbol+path[2::]
        os.chdir(p)


    else:
        os.chdir(path)

def ls():
    return str((os.listdir()))

def create(file_name):
    file = open(file_name, "w+")
    file.close()

def rmv(file_name):
    os.remove(file_name)

def rewrite(file_name, content):
    try:
        file = open(file_name, "w")
        file.write(content)
    except:
        print('Что-то пошло не так')

def add(file_name, content):
    file = open(file_name, "a")
    file.write(content)
    file.close()

def rename(first_name, second_name):
    try:
        os.rename(first_name,second_name)
    except:
        print('Что-то пошло не так')

def copy(first_name, second_name):
    try:
        shutil.copy(first_name,second_name)
    except:
        print('Что-то пошло не так')

def move(first_name, second_name):
    try:
        shutil.move(first_name,second_name)
    except:
        print('Что-то пошло не так')