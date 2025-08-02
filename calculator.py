import tkinter as tk
import sys

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

def calculate(a, op, b):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        if b == 0:
            return "Divide by 0"
        return div(a, b)
    else:
        return "Invalid operator"

light_theme = {
    "bg": "#ffffff",
    "fg": "#000000",
    "btn_bg": "#e0e0e0",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

dark_theme = {
    "bg": "#2c2c2c",
    "fg": "#ffffff",
    "btn_bg": "#4a4a4a",
    "entry_bg": "#333333",
    "entry_fg": "#ffffff"
}

current_theme = light_theme 
def click(char):
    current = entry.get()
    if char == "=":
        try:
            for op in ['+', '-', '*', '/']:
                if op in current:
                    left, right = current.split(op)
                    a = float(left.strip())
                    b = float(right.strip())
                    result = calculate(a, op, b)
                    entry.delete(0, tk.END)
                    entry.insert(0, str(result))
                    return
            entry.delete(0, tk.END)
            entry.insert(0, "Invalid")
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(0, "Invalid")
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(0, "Divide by 0")
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif char == "C":
        entry.delete(0, tk.END)
    elif char == "⌫":
        entry.delete(len(current) - 1)
    else:
        entry.insert(tk.END, char)

def toggle_theme():
    global current_theme
    current_theme = dark_theme if current_theme == light_theme else light_theme
    apply_theme()

def apply_theme():
    root.configure(bg=current_theme["bg"])
    entry.configure(bg=current_theme["entry_bg"], fg=current_theme["entry_fg"])
    for btn in buttons_list:
        btn.configure(bg=current_theme["btn_bg"], fg=current_theme["fg"])
    theme_btn.configure(bg=current_theme["btn_bg"], fg=current_theme["fg"])

root = tk.Tk()
root.title("Python GUI Calculator")
root.resizable(False, False)

entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

layout = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C", "⌫", "Theme")
]

buttons_list = []
for r, row in enumerate(layout):
    for c, char in enumerate(row):
        if char == "Theme":
            theme_btn = tk.Button(root, text=char, width=11, height=2, font=("Arial", 14), command=toggle_theme)
            theme_btn.grid(row=r + 1, column=c, columnspan=2, padx=3, pady=3, sticky="we")
        else:
            btn = tk.Button(root, text=char, width=5, height=2, font=("Arial", 16),
                            command=lambda ch=char: click(ch))
            btn.grid(row=r + 1, column=c, padx=3, pady=3)
            buttons_list.append(btn)

apply_theme()

root.mainloop()
