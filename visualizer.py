from tkinter import *
from tkinter import ttk
from dijkstra import Algorithme_de_dijkstra
import json


def visualisation(dictionnaire):
    def insert_data(tree, steps, columns):
        for step, values in steps.items():
            choix_str = f"{values['choix'][0]}({values['choix'][1]})"
            if len(values['choix']) == 3:
                choix_str += f"{values['choix'][2]}"
            row = [values.get(col, '') for col in columns[0:-1]] + [choix_str]
            tree.insert('', 'end', values=row)

    def update_window(event):
        if len(tree_root.winfo_children()) == 2:
            tree_root.winfo_children()[-1].destroy()

        algo = Algorithme_de_dijkstra(dictionnaire, lettre_arrive=start_point.get(), lettre_depart=end_point.get())

        best_chemin_str = f"{algo.meilleur_chemin}"
        best_chemin_label.configure(text=best_chemin_str)

        columns = []
        for i in algo.steps["step 0"].keys():
            columns.append(i)

        tree = ttk.Treeview(tree_root, show="headings", columns=columns)
        tree.pack(expand=YES)

        for i in columns:
            tree.heading(i, text=f"{i}")
            tree.column(i, width=100, anchor="center")

        insert_data(tree=tree, steps=algo.steps, columns=columns)

    root.quit()
    root.destroy()

    chemin_root = Tk()

    tree_root = Tk()

    points = []
    for i in dictionnaire:
        points.append(i)

    end_point = StringVar()
    end_point.set(points[0])
    OptionMenu(chemin_root, end_point, *points, command=update_window).pack(side="left")

    Label(chemin_root, text='to').pack(side="left")

    start_point = StringVar()
    start_point.set(points[-1])
    OptionMenu(chemin_root, start_point, *points, command=update_window).pack(side="left")

    best_chemin_label = Label(tree_root, text="", font=("", 25))
    best_chemin_label.pack()

    update_window(None)

    while True:
        tree_root.update()
        chemin_root.update()


def str_to_dict():
    # Supprimer les espaces blancs autour des clés et valeurs pour avoir une chaîne JSON valide
    str_dict = str(entry.get()).replace("'", "\"")

    visualisation(json.loads(str_dict))

root = Tk()

Label(root, text="Entrez la route :", font=("", 20)).pack()

entry = Entry(root)
entry.pack()

Button(root, text="VISUALISATION", command=str_to_dict).pack(pady=10)

root.mainloop()
