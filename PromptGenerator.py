import tkinter as tk
from tkinter import scrolledtext
from itertools import product

def add_fixed():
    frame = tk.Frame(root)
    frame.pack(fill=tk.X)
    label = tk.Label(frame, text="Fixed part:")
    label.pack(side=tk.LEFT)
    entry = tk.Entry(frame, width=50)
    entry.pack(side=tk.LEFT)
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(frame, text="Add comma", variable=var)
    checkbox.pack(side=tk.LEFT)
    delete_button = tk.Button(frame, text="Delete", command=lambda: delete_part(frame))
    delete_button.pack(side=tk.LEFT)
    entries.append(("fixed", entry, var, frame))

def add_variable():
    frame = tk.Frame(root)
    frame.pack(fill=tk.X)
    label = tk.Label(frame, text="Variable part:")
    label.pack(side=tk.LEFT)
    entry = tk.Entry(frame, width=50)
    entry.pack(side=tk.LEFT)
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(frame, text="Add comma", variable=var)
    checkbox.pack(side=tk.LEFT)
    delete_button = tk.Button(frame, text="Delete", command=lambda: delete_part(frame))
    delete_button.pack(side=tk.LEFT)
    entries.append(("variable", entry, var, frame))

def delete_part(frame):
    entries[:] = [entry for entry in entries if entry[3] != frame]
    frame.destroy()

def generate_prompts():
    result_text.delete('1.0', tk.END)
    prompts = []
    variable_parts = [entry[1].get().split(', ') if entry[0] == "variable" else [entry[1].get()] for entry in entries]
    variable_combinations = list(product(*variable_parts))
    for variable_combination in variable_combinations:
        prompt_parts = []
        for i, part in enumerate(variable_combination):
            prompt_parts.append(part)
            if entries[i][2].get():
                prompt_parts.append(',')
        prompts.append(' '.join(prompt_parts))
    for prompt in prompts:
        result_text.insert(tk.END, prompt + '\n')

root = tk.Tk()
root.title("Prompt Generator")

entries = []

add_fixed_button = tk.Button(root, text="Add Fixed Part", command=add_fixed)
add_fixed_button.pack(fill=tk.X)

add_variable_button = tk.Button(root, text="Add Variable Part", command=add_variable)
add_variable_button.pack(fill=tk.X)

generate_button = tk.Button(root, text="Generate Prompts", command=generate_prompts)
generate_button.pack(fill=tk.X)

result_text = scrolledtext.ScrolledText(root, width=70, height=10)
result_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
