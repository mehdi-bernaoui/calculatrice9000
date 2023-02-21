from tkinter import *

# Fonction pour effectuer les calculs
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Fonction pour ajouter un chiffre ou un symbole à l'expression
def add_to_expression(char):
    current_expression = entry.get()
    entry.delete(0, END)
    entry.insert(0, current_expression + str(char))

# Fonction pour effacer le dernier caractère entré
def delete_last_char():
    current_expression = entry.get()[:-1]
    entry.delete(0, END)
    entry.insert(0, current_expression)

# Création de la fenêtre
root = Tk()
root.title("Calculatrice")
root.configure(background="#9ACD32")

# Entrée pour afficher l'expression et le résultat
entry = Entry(root, width=30, borderwidth=5, font=('Arial', 18, 'bold'))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Boutons pour les chiffres
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: add_to_expression(1), bg="#FFFFFF", font=('Arial', 16, 'bold'))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: add_to_expression(2), bg="#FFFFFF", font=('Arial', 16, 'bold'))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: add_to_expression(3), bg="#FFFFFF", font=('Arial', 16, 'bold'))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: add_to_expression(4), bg="#FFFFFF", font=('Arial', 16, 'bold'))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: add_to_expression(5), bg="#FFFFFF", font=('Arial', 16, 'bold'))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: add_to_expression(6), bg="#FFFFFF", font=('Arial', 16, 'bold'))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: add_to_expression(7), bg="#FFFFFF", font=('Arial', 16, 'bold'))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: add_to_expression(8), bg="#FFFFFF", font=('Arial', 16, 'bold'))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: add_to_expression(9), bg="#FFFFFF", font=('Arial', 16, 'bold'))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: add_to_expression(0), bg="#FFFFFF", font=('Arial', 16, 'bold'))


# Boutons pour les opérations
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: add_to_expression("+"), bg="#E6E6FA", font=('Arial', 16, 'bold'))
button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: add_to_expression("-"), bg="#E6E6FA", font=('Arial', 16, 'bold'))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: add_to_expression("*"), bg="#E6E6FA", font=('Arial', 16, 'bold'))
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: add_to_expression("/"), bg="#E6E6FA", font=('Arial', 16, 'bold'))
button_equal = Button(root, text="=", padx=91, pady=20, command=calculate, bg="#E6E6FA", font=('Arial', 16, 'bold'))
button_clear = Button(root, text="Effacer", padx=70, pady=20, command=lambda: entry.delete(0, END), bg="#FFA07A", font=('Arial', 16, 'bold'))
button_delete = Button(root, text="Effacer\nDernier", padx=50, pady=20, command=delete_last_char, bg="#FFA07A", font=('Arial', 16, 'bold'))

# Placement des boutons sur la fenêtre
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_delete.grid(row=5, column=0)
button_add.grid(row=5, column=1)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_equal.grid(row=5, column=2, columnspan=2)

# Boucle principale
root.mainloop()
