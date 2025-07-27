import tkinter as tk
from tkinter import messagebox

# دالة تنفيذ المعادلة
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# دالة حذف آخر رقم
def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# دالة لحذف كل شيء
def clear():
    display.delete(0, tk.END)

# دالة لإضافة رقم أو عملية
def add_to_display(value):
    display.insert(tk.END, value)

# دالة للخروج
def turn_off():
    root.destroy()

# واجهة البرنامج
root = tk.Tk()
root.title("Egyptian Calculator")
root.geometry("350x450")
root.configure(bg="black")

# شاشة العرض
display = tk.Entry(root, font=("Orbitron", 24), borderwidth=5, relief="ridge", justify="right", bg="black", fg="lime")
display.pack(pady=20, padx=10, fill="x")

# الأزرار
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for row in buttons:
    frame = tk.Frame(root, bg="black")
    frame.pack(pady=5)
    for btn in row:
        action = (
            calculate if btn == '=' else
            backspace if btn == '⌫' else
            lambda b=btn: add_to_display(b)
        )
        tk.Button(frame, text=btn, width=6, height=2, font=("Orbitron", 14),
                  command=action, bg="#333", fg="white").pack(side="left", padx=5)

# صف الأوامر (Clear + Back + Off)
bottom = tk.Frame(root, bg="black")
bottom.pack(pady=10)

tk.Button(bottom, text="C", width=10, height=2, font=("Orbitron", 12), command=clear,
          bg="red", fg="white").pack(side="left", padx=5)

tk.Button(bottom, text="⌫", width=10, height=2, font=("Orbitron", 12), command=backspace,
          bg="orange", fg="white").pack(side="left", padx=5)

tk.Button(bottom, text="OFF", width=10, height=2, font=("Orbitron", 12), command=turn_off,
          bg="black", fg="red", borderwidth=2).pack(side="left", padx=5)

root.mainloop()
