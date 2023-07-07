import tkinter as tk
from tkinter import scrolledtext
from itertools import product


class PromptGenerator:
    def __init__(self, root):
        self.root = root
        self.entries = []

        self.add_fixed_button = tk.Button(self.root, text="Add Fixed Part", command=self.add_fixed)
        self.add_fixed_button.pack(fill=tk.X)

        self.add_variable_button = tk.Button(self.root, text="Add Variable Part", command=self.add_variable)
        self.add_variable_button.pack(fill=tk.X)

        self.generate_button = tk.Button(self.root, text="Generate Prompts", command=self.generate_prompts)
        self.generate_button.pack(fill=tk.X)

        self.result_text = scrolledtext.ScrolledText(self.root, width=70, height=10)
        self.result_text.pack(fill=tk.BOTH, expand=True)

    def add_fixed(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X)
        label = tk.Label(frame, text="Fixed part:")
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame, width=50)
        entry.pack(side=tk.LEFT)
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(frame, text="Add comma", variable=var)
        checkbox.pack(side=tk.LEFT)
        delete_button = tk.Button(frame, text="Delete", command=lambda: self.delete_part(frame))
        delete_button.pack(side=tk.LEFT)
        self.entries.append(("fixed", entry, var, frame))

    def add_variable(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X)
        label = tk.Label(frame, text="Variable part:")
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame, width=50)
        entry.pack(side=tk.LEFT)
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(frame, text="Add comma", variable=var)
        checkbox.pack(side=tk.LEFT)
        delete_button = tk.Button(frame, text="Delete", command=lambda: self.delete_part(frame))
        delete_button.pack(side=tk.LEFT)
        self.entries.append(("variable", entry, var, frame))

    def delete_part(self, frame):
        self.entries = [entry for entry in self.entries if entry[3] != frame]
        frame.destroy()

    def generate_prompts(self):
        self.result_text.delete('1.0', tk.END)
        prompts = []
        variable_parts = [entry[1].get().split(', ') if entry[0] == "variable" else [entry[1].get()] for entry in self.entries]
        variable_combinations = list(product(*variable_parts))
        for variable_combination in variable_combinations:
            prompt_parts = []
            for i, part in enumerate(variable_combination):
                prompt_parts.append(part)
                if self.entries[i][2].get():
                    prompt_parts.append(',')
            prompts.append(' '.join(prompt_parts))
        for prompt in prompts:
            self.result_text.insert(tk.END, prompt + '\n')


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prompt Generator")

    prompt_generator = PromptGenerator(root)

    root.mainloop()
