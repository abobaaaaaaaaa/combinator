import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=70, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    'Перестановка', 'Сочетания', 'Размещения', 'МАКСИМ НЕ ТРОГАЙ ГИТХАБ',
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0', 'C', '='
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10, bg='white', fg='black', font='white')
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
