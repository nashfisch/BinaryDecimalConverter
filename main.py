import tkinter as tk

# Window setup
root = tk.Tk()
root.title('Binary Converter')
root.geometry('500x400')

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
entryPrompt = tk.Label(root, text = 'Enter a number: ')
entryPrompt.grid(column = 0, row = 1)
txt = tk.Entry(root, width = 10)
txt.grid(column = 1, row = 1)

arrow = tk.Label(root, text = '-->')
arrow.grid(column = 2, row = 1)
convert = tk.Button()


root.mainloop()