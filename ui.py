import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from main import persons, price, theme_anime, theme_games, theme_kids, theme_fruits, theme_Normal, flavor, occasions
from main import genetic_algorithm


def run_genetic_algorithm():
    try:
        client = [int(combo_persons.get()), int(combo_price.get()), combo_theme.get(), combo_flavor.get()]
        population_f, history_f, fss_best, best_ind, count, worst = genetic_algorithm(client, int(size.get()),
                                                                               int(size_of_population.get()),
                                                                               float(num_gen.get()),
                                                                               float(num_ind.get()),
                                                                               float(epochs.get()))
        messagebox.showinfo("Result",
                            f"Best Fitness Scores: {fss_best}\nBest Individuals: {best_ind[0]}\n{best_ind[1]}\n{best_ind[2]}")
        plt.plot(history_f)
        plt.plot(worst)
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.grid()
        plt.ylim(0, 1)
        plt.title('Fitness over Generations')
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Please select valid values.")


root = tk.Tk()

tk.Label(root, text="Persons").grid(row=0)
tk.Label(root, text="Price").grid(row=1)
tk.Label(root, text="Design").grid(row=2)
tk.Label(root, text="Flavor").grid(row=3)
tk.Label(root, text="Size of Population").grid(row=5)
tk.Label(root, text="Size of first gen").grid(row=6)
tk.Label(root, text="% of mutate genes").grid(row=7)
tk.Label(root, text="% of mutate individuals").grid(row=8)
tk.Label(root, text="% aprovate").grid(row=9)

combo_persons = ttk.Combobox(root, values=persons)
combo_price = ttk.Entry(root, width=23)
combo_theme = ttk.Combobox(root, values=occasions)
combo_flavor = ttk.Combobox(root, values=flavor)
size = ttk.Entry(root, width=23)
size_of_population = ttk.Entry(root, width=23)
num_gen = ttk.Entry(root, width=23)
num_ind = ttk.Entry(root, width=23)
epochs = ttk.Entry(root, width=23)

combo_persons.grid(row=0, column=1, pady=5, padx=5)
combo_price.grid(row=1, column=1, pady=5, padx=5)
combo_theme.grid(row=2, column=1, pady=5, padx=5)
combo_flavor.grid(row=3, column=1, pady=5, padx=5)
size.grid(row=5, column=1, pady=5, padx=5)
size_of_population.grid(row=6, column=1, pady=5, padx=5)
num_gen.grid(row=7, column=1, pady=5, padx=5)
num_ind.grid(row=8, column=1, pady=5, padx=5)
epochs.grid(row=9, column=1, pady=5, padx=5)

tk.Button(root, text='Run Genetic Algorithm', command=run_genetic_algorithm).grid(row=10, column=0, sticky=tk.W,
                                                                                  pady=20, padx=20)

root.mainloop()
