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
    global entryPrompt
    newEntry = entryPrompt.get()
    return newEntry

# Function to switch a decimal number into binary
def decToBin(num):
    binRep = 0
    base = 1

    while num > 0:
        rem = num % 2
        binRep += rem * base
        num //= 2
        base *= 10

    return binRep
    


# Entry field
entryPrompt = tk.Label(root, text = 'Enter a decimal number: ')
entryPrompt.grid(column = 0, row = 1)
txt = tk.Entry(root, width = 10)
txt.grid(column = 1, row = 1)



arrow = tk.Label(root, text = '-->')
arrow.grid(column = 2, row = 1)


convert = tk.Button(root, text = 'Convert', bg = 'lime')
convert.grid(column = 1, row = 2)

switch = tk.Button(root, text = 'Switch', command = switchRep, bg = 'red')
switch.grid(column = 2, row = 2)



root.mainloop()