import tkinter as tk

# Window setup
root = tk.Tk()
root.title('Binary Converter')
root.geometry('500x400')

binary = False

def switchRep():
    global entryPrompt
    global binary
    if binary == False:
        binary = True
        entryPrompt.config(text = 'Enter a binary number: ')
    elif binary == True:
        binary = False
        entryPrompt.config(text = 'Enter a decimal number: ')

def getEntry():
    return field.get()

# Function to switch a decimal number into binary
def conversion(num):
    if binary == False:
        binRep = 0
        base = 1

        while int(num) > 0:
            rem = num % 2
            binRep += rem * base
            num //= 2
            base *= 10

        answer.config(text = binRep)

    elif binary == True:
        bit = 0
        decRep = 0
        i = 0
        while int(num) > 0:
            bit = num % 10
            if bit == 1 or bit == 0:
                decRep += bit * 2 ** i
                num //= 10
                i += 1
        answer.config(text = decRep)




# Entry field
entryPrompt = tk.Label(root, text = 'Enter a decimal number: ')
entryPrompt.grid(column = 0, row = 1)

answer = tk.Label(root)
answer.grid(column = 3, row = 1)

field = tk.Entry(root, width = 10)
field.grid(column = 1, row = 1)


arrow = tk.Label(root, text = '-->')
arrow.grid(column = 2, row = 1)


convert = tk.Button(root, text = 'Convert', bg = 'lime', command = lambda: conversion(getEntry()))
convert.grid(column = 1, row = 2)

switch = tk.Button(root, text = 'Switch', bg = 'red', command = switchRep)
switch.grid(column = 2, row = 2)



root.mainloop()