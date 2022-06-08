#Manage data and implement persistent data storage

import re
import os

def loadWordsFromFile(fileName):
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()
    return re.split('\n', textData)

def mainMenu():

    file = loadWordsFromFile("PrimeMinisters.txt")

    print("""
    1. Display all of the data.
    2. Display some of the data.
    3. Select data to add to a favourites list.
    4. Remove last item from favourites list.
    5. Display favourites list.
    6. Quit.
    """)

    answer = int(input('Choose: '))

    if answer == 1:
        for i in range(28):
            name, term = file[i].split('+')[0], file[i].split('+')[1]
            print('Name: ' + name + ' | Term: ' + term)
        mainMenu()
    elif answer == 2:
        print('''
        1. Filter by year
        2. Filter by name
                 ''')
        answer2 = int(input("Choose: "))
        if answer2 == 1:
            year = input('Enter year: ')
            for i in range(28):
                term = file[i].split('+')[1]
                if "-" in term:
                    term = term.split("-")[0]
                if term == year:
                    name, term = file[i].split('+')[0], file[i].split('+')[1]
                    print('Name: ' + name + ' | Term: ' + term)
        elif answer2 == 2:
            name = input('Enter name: ')
            for i in range(28):
                title = file[i].split('+')[0]
                if title == name:
                    name, term = file[i].split('+')[0], file[i].split('+')[1]
                    print('Name: ' + name + ' | Term: ' + term)
        mainMenu()
    elif answer == 3:
        print('''
            1. Add by year (first year)
            2. Add by name (full name)
                    ''')
        answer2 = int(input("Choose: "))
        if answer2 == 1:
            year = input('Enter year: ')
            for i in range(28):
                term = file[i].split('+')[1]
                if "-" in term:
                    term = term.split("-")[0]
                if term == year:
                    file_object = open(username + '.txt', 'a')
                    file_object.write('\n' + file[i])
                    file_object.close()
                    print('Data added!')
        elif answer2 == 2:
            name = input('Enter name: ')
            for i in range(28):
                title = file[i].split('+')[0]
                if title == name:
                    file_object = open(username + '.txt', 'a')
                    file_object.write('\n' + file[i])
                    file_object.close()
                    print('Data added!')
        mainMenu()
    elif answer == 4:
        a_file = open(username + ".txt", "r")
        lines = a_file.readlines()
        a_file.close()
        del lines[len(lines)-1]
        new_file = open(username + ".txt", "w+")
        for line in lines:
            new_file.write(line)
        new_file.close()
        mainMenu()
        #On school computer this makes the line go blank
        #On mac, this completely deletes the line
    elif answer == 5:
        account_file = loadWordsFromFile(username + ".txt")
        for i in range(len(account_file)):
            print(account_file[i])
        mainMenu()
    elif answer == 6:
        exit()


print("""
    1. LOGIN
    2. REGISTER
        """)
response = int(input('Enter choice: '))
file = loadWordsFromFile("logins.txt")
username = ''
password = ''
LOGIN = False
if response == 1:
    username = input('Enter username: ')
    password = input('Enter password: ')
    for i in range(len(file)):
        if username == file[i].split('-')[0] and password == file[i].split('-')[1]:
            LOGIN = True
    if LOGIN == True:
        print('LOGIN success')
        mainMenu()
    else:
        print('LOGIN failure. Quitting program')
elif response == 2:
    username = input('Create username: ')
    password = input('Create password: ')
    for i in range(len(file)):
        if username == file[i].split('-')[0]:
            LOGIN = False
        else:
            LOGIN = True
    if LOGIN == True:
        file_object = open('logins.txt', 'a')
        file_object.write('\n' + username + '-' + password)
        file_object.close()
        with open(username + '.txt', 'x') as f:
            f.write(username + "'s account")
        print('Account Created!')
        mainMenu()
    else:
        print('LOGIN info already exists. Please restart this program and login.')
        exit()


