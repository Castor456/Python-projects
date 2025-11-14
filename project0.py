import tkinter as tk
from tkinter import simpledialog, scrolledtext

# ---------------------------------------
# THEME DEFINITIONS
# ---------------------------------------

LIGHT_THEME = {
    "BG": "#f0f0f0",
    "FG": "#000000",
    "BTN_BG": "#e0e0e0",
    "BTN_FG": "#000000",
    "TEXT_BG": "#ffffff",
    "TEXT_FG": "#000000",
    "HIGHLIGHT": "#d0d0d0"
}

DARK_THEME = {
    "BG": "#1e1e1e",
    "FG": "#ffffff",
    "BTN_BG": "#2d2d2d",
    "BTN_FG": "#ffffff",
    "TEXT_BG": "#252526",
    "TEXT_FG": "#d4d4d4",
    "HIGHLIGHT": "#3c3c3c"
}

current_theme = DARK_THEME  # start in dark mode


# ---------------------------------------
# LOGIC / FUNCTIONS
# ---------------------------------------

def apply_theme(theme):
    """Apply theme colors to the entire GUI."""
    root.config(bg=theme["BG"])
    title.config(bg=theme["BG"], fg=theme["FG"])
    toggle_btn.config(bg=theme["BTN_BG"], fg=theme["BTN_FG"],
                      activebackground=theme["HIGHLIGHT"])

    for btn in buttons:
        btn.config(bg=theme["BTN_BG"], fg=theme["BTN_FG"],
                   activebackground=theme["HIGHLIGHT"])

    result_box.config(bg=theme["TEXT_BG"], fg=theme["TEXT_FG"])


def toggle_theme():
    global current_theme
    current_theme = LIGHT_THEME if current_theme == DARK_THEME else DARK_THEME
    toggle_btn.config(text="Dark Mode" if current_theme == LIGHT_THEME else "Light Mode")
    apply_theme(current_theme)


# ---------------------------------------
# BASIC PROBLEM FUNCTIONS
# ---------------------------------------

def output(text):
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, text)
    result_box.config(state=tk.DISABLED)


def reverse_string():
    s = simpledialog.askstring("Input", "Enter a string:")
    if s:
        output(f"Reversed: {s[::-1]}")


def check_palindrome():
    s = simpledialog.askstring("Input", "Enter a string:")
    if s:
        output("Palindrome" if s == s[::-1] else "Not Palindrome")


def count_vowels():
    s = simpledialog.askstring("Input", "Enter a string:")
    if s:
        cnt = sum(1 for c in s.lower() if c in "aeiou")
        output(f"Vowel count: {cnt}")


def find_max():
    nums = simpledialog.askstring("Input", "Enter numbers:")
    if nums:
        arr = list(map(int, nums.split()))
        output(f"Max: {max(arr)}")


def sum_of_list():
    nums = simpledialog.askstring("Input", "Enter numbers:")
    if nums:
        arr = list(map(int, nums.split()))
        output(f"Sum: {sum(arr)}")


def find_duplicates():
    nums = simpledialog.askstring("Input", "Enter numbers:")
    if nums:
        arr = list(map(int, nums.split()))
        seen = set()
        dups = []
        for n in arr:
            if n in seen:
                dups.append(n)
            seen.add(n)
        output(f"Duplicates: {dups if dups else 'None'}")


def fibonacci():
    n = simpledialog.askinteger("Input", "How many numbers?")
    if n:
        a, b = 0, 1
        seq = []
        for _ in range(n):
            seq.append(str(a))
            a, b = b, a + b
        output(", ".join(seq))


def factorial():
    n = simpledialog.askinteger("Input", "Enter a number:")
    if n is not None:
        f = 1
        for i in range(1, n + 1):
            f *= i
        output(f"Factorial: {f}")


def prime_check():
    num = simpledialog.askinteger("Input", "Enter number:")
    if num is not None:
        if num <= 1:
            output("Not Prime")
            return
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                output("Not Prime")
                return
        output("Prime")


def sort_list():
    nums = simpledialog.askstring("Input", "Enter numbers:")
    if nums:
        arr = list(map(int, nums.split()))
        output(f"Sorted: {sorted(arr)}")


def frequency_count():
    nums = simpledialog.askstring("Input", "Enter numbers:")
    if nums:
        arr = list(map(int, nums.split()))
        freq = {}
        for n in arr:
            freq[n] = freq.get(n, 0) + 1
        output(str(freq))


def remove_duplicates():
    nums = simpledialog.askstring("Input", "Enter numbers:")
    if nums:
        arr = list(map(int, nums.split()))
        output(f"Unique: {list(set(arr))}")


def second_largest():
    nums = simpledialog.askstring("Input", "Enter numbers:")
    if nums:
        arr = sorted(list(set(map(int, nums.split()))))
        output("Not enough numbers" if len(arr) < 2 else f"Second largest: {arr[-2]}")


def word_count():
    s = simpledialog.askstring("Input", "Enter sentence:")
    if s:
        output(f"Word count: {len(s.split())}")


def armstrong_check():
    num = simpledialog.askinteger("Input", "Enter number:")
    if num is not None:
        total = sum(int(d) ** len(str(num)) for d in str(num))
        output("Armstrong" if total == num else "Not Armstrong")


# ---------------------------------------
# GUI LAYOUT / RESPONSIVE SETUP
# ---------------------------------------

root = tk.Tk()
root.title("Python Practice Problems (Dark/Light Mode)")
root.geometry("900x600")
root.minsize(700, 450)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Title bar
title_frame = tk.Frame(root)
title_frame.grid(row=0, column=0, sticky="nsew")
title_frame.columnconfigure(0, weight=1)

title = tk.Label(title_frame, text="Select a Problem", font=("Arial", 18, "bold"))
title.grid(row=0, column=0, pady=10, sticky="w", padx=10)

toggle_btn = tk.Button(title_frame, text="Light Mode", command=toggle_theme)
toggle_btn.grid(row=0, column=1, padx=10, sticky="e")

# Buttons grid
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, sticky="nsew", padx=10)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

problems = [
    ("Reverse String", reverse_string),
    ("Palindrome Check", check_palindrome),
    ("Count Vowels", count_vowels),
    ("Find Max", find_max),
    ("Sum of List", sum_of_list),
    ("Find Duplicates", find_duplicates),
    ("Fibonacci", fibonacci),
    ("Factorial", factorial),
    ("Prime Check", prime_check),
    ("Sort List", sort_list),
    ("Frequency Count", frequency_count),
    ("Remove Duplicates", remove_duplicates),
    ("Second Largest", second_largest),
    ("Word Count", word_count),
    ("Armstrong Check", armstrong_check)
]

buttons = []
row = 0
for text, cmd in problems:
    btn = tk.Button(button_frame, text=text, command=cmd, height=2)
    btn.grid(row=row // 2, column=row % 2, sticky="nsew", padx=5, pady=5)
    buttons.append(btn)
    row += 1

for r in range((len(problems) // 2) + 2):
    button_frame.rowconfigure(r, weight=1)

# Output area
result_box = scrolledtext.ScrolledText(root, font=("Courier", 12), state=tk.DISABLED)
result_box.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

# Apply starting theme
apply_theme(current_theme)

root.mainloop()