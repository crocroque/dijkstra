import pygame
from tkinter import *
import clipboard

colors = {
    "Red": (255, 0, 0),
    "Blue": (0, 0, 255),
    "Green": (0, 255, 0),
    "Yellow": (255, 255, 0),
    "Orange": (255, 165, 0),
    "Purple": (128, 0, 128),
    "Pink": (255, 192, 203),
    "Brown": (165, 42, 42),
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Gray": (128, 128, 128),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "Lime": (0, 255, 0),
    "Maroon": (128, 0, 0),
    "Navy": (0, 0, 128),
    "Olive": (128, 128, 0),
    "Teal": (0, 128, 128),
    "Silver": (192, 192, 192),
    "Gold": (255, 215, 0)
}


def end_connection_root():
    for i in label_entry_choix:
        if i[1].get().isdigit():
            point_connecte = i[0]['text']

            points[point_selectionne[0]]["Chemin"][point_connecte] = {"distance": int(i[1].get())}
            points[point_connecte]["Chemin"][point_selectionne[0]] = {"distance": int(i[1].get())}


    connection_root.quit()
    connection_root.destroy()


def end_lines_root(point_a_suppr=None):
    if point_a_suppr is not None:
        del points[point_selectionne[0]]['Chemin'][point_a_suppr]
        del points[point_a_suppr]['Chemin'][point_selectionne[0]]

    remove_lines_root.quit()
    remove_lines_root.destroy()


def generate_route():
    route = {}
    for key in points:
        route[key] = {"Chemin" : points[key]['Chemin']}


    generate_route_text.delete("1.0", "end")
    generate_route_text.insert(END, route)


def copy_route():
    clipboard.copy(generate_route_text.get('1.0', "end"))


def set_type_of_points(type_of_points):
    global nom_itineraire_type


    if type_of_points == "Numbers":
        nom_itineraire_type = int

    elif type_of_points == 'Letters':
        global noms_points
        nom_itineraire_type = list

        noms_points = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    type_of_points_choix_root.quit()
    type_of_points_choix_root.destroy()

type_of_points_choix_root = Tk()

Label(type_of_points_choix_root, text="points type : ").pack()

for i in ["Numbers", "Letters"]:
    Button(type_of_points_choix_root, text=i, command=lambda i=i: set_type_of_points(i)).pack()

type_of_points_choix_root.mainloop()
pygame.init()

background_color = (255, 255, 255)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

running = True

fps = pygame.time.Clock()

mouse = pygame.mouse

pressed = None

txt_color = (0, 0, 0)
font = pygame.font.SysFont(None, 30)

iterateur_point = -1
iterateur_point_liste = 0

points = {}

lines = []

tools_root = Tk()
tools_root.geometry("400x400")
is_place = IntVar()

scale = Scale(tools_root, from_=0, to=3, showvalue=False, orient=HORIZONTAL, variable=is_place, width=15, length=250)
scale.pack()
Label(tools_root, text="PLACE (A)               MOVE(Z)      REMOVE (E)          SELECT (R)", font=("courrier", 10)).pack(fill="both")

generate_route_button = Button(tools_root, text="generate", command=generate_route)
generate_route_button.pack(pady=15)

generate_route_text = Text(tools_root, height=2, width=45)
generate_route_text.pack()

copy_route_btn = Button(tools_root, text="copy", command=copy_route)
copy_route_btn.pack()

Label(tools_root, text='--- Background Color ---').pack(pady=15)
selected_colors_bg = StringVar()
selected_colors_bg.set(list(colors)[0])
OptionMenu(tools_root, selected_colors_bg, *list(colors)).pack()

Label(tools_root, text='--- Text Color ---').pack(pady=15)
selected_colors_txt = StringVar()
selected_colors_txt.set(list(colors)[0])
OptionMenu(tools_root, selected_colors_txt, *list(colors)).pack()


while running:
    screen.fill(background_color)
    txt_color = selected_colors_txt.get()
    background_color = selected_colors_bg.get()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if mouse.get_pressed(3)[0] and is_place != 1:
        pressed = True

    if keys[pygame.K_a]:
        scale.set(0)
    elif keys[pygame.K_z]:
        scale.set(1)
    elif keys[pygame.K_e]:
        scale.set(2)
    elif keys[pygame.K_r]:
        scale.set(3)

    if is_place.get() == 1:
        if mouse.get_pressed(3)[0]:
            point_selectionne = None
            for i in points.items():
                if i[1]["rect"].collidepoint(mouse.get_pos()):
                    point_selectionne = i
                    break

            if point_selectionne is not None:
                point_selectionne[1]["rect"].center = mouse.get_pos()

    if pressed:
        if not mouse.get_pressed(3)[0]:
            pressed = False

            if is_place.get() == 0:
                iterateur_point += 1

                if nom_itineraire_type is int:
                    nom_point = iterateur_point

                elif nom_itineraire_type is list:
                    if len(noms_points) == iterateur_point:
                        iterateur_point = 0
                        iterateur_point_liste += 1

                    nom_point = noms_points[iterateur_point] + f"{iterateur_point_liste if iterateur_point_liste != 0 else ''}"

                text = f"{nom_point}"

                text_surface = font.render(text, True, txt_color)
                text_rect = text_surface.get_rect()

                text_rect.x, text_rect.y = mouse.get_pos()

                points[str(nom_point)] = {"surface": text_surface, "rect": text_rect, "Chemin": {}}

            elif is_place.get() == 2:
                point_selectionne = None
                for i in points.items():
                    if i[1]["rect"].collidepoint(mouse.get_pos()):
                        point_selectionne = i
                        break

                if point_selectionne is not None and point_selectionne[1]['Chemin'] != {}:
                    remove_lines_root = Tk()

                    entries_per_row = 5
                    for i, chemin in enumerate(point_selectionne[1]['Chemin']):
                        row = i // entries_per_row
                        column = i % entries_per_row # Multiplier par 2 pour laisser un espace pour les entrées

                        Button(remove_lines_root, text=f'remove {point_selectionne[0]} -> {chemin}', command=lambda chemin=chemin: end_lines_root(chemin)).grid(row=row, column=column)

                    Button(remove_lines_root, text="quit", command=end_lines_root).grid()

                    remove_lines_root.geometry(f"{entries_per_row * 75 + 100}x{(row + 1) * 55 + 10}")
                    remove_lines_root.mainloop()

            elif is_place.get() == 3:
                point_selectionne = None
                for i in points.items():
                    if i[1]["rect"].collidepoint(mouse.get_pos()):
                        point_selectionne = i
                        break

                if point_selectionne is not None:
                    points_dispo = []
                    for i in points:
                        if i != point_selectionne[0]:
                            points_dispo.append(i)



                    connection_root = Tk()


                    label_entry_choix = []

                    for i, m in enumerate(points_dispo):
                        label_entry_choix.append( (Label(connection_root, text=points_dispo[i]), Entry(connection_root, width=5) ))


                    entries_per_row = 10
                    for i, m in enumerate(label_entry_choix):
                        row = i // entries_per_row
                        column = i % entries_per_row * 2 # Multiplier par 2 pour laisser un espace pour les entrées

                        m[0].grid(row=row, column=column, padx=5, pady=5)
                        m[1].grid(row=row, column=column + 1, padx=5, pady=5)

                    choix_connection_btn = Button(connection_root, text="choisir", command=end_connection_root)
                    choix_connection_btn.grid()

                    connection_root.geometry(f"{entries_per_row * 75 + 30}x{(row + 1) * 55 + 10}+0+0")
                    connection_root.mainloop()

    for i in points.items():
        i[1]["surface"] = font.render(i[0], True, txt_color)
        screen.blit(i[1]["surface"], i[1]["rect"])

    lines = []
    for i in points.items():
        for m in i[1]['Chemin']:
            lines.append((screen, txt_color, i[1]['rect'].center, points[m]['rect'].center, i[1]["Chemin"][m]['distance']))


    for screen, color, pos1, pos2, distance in lines:
        pygame.draw.line(screen, color, pos1, pos2)

        text_surface = font.render(str(distance), True, txt_color)
        text_rect = text_surface.get_rect()

        text_rect.x = (pos1[0] + pos2[0]) / 2 #on fait la moyenne des pos pour trouver le millieu des droite
        text_rect.y = (pos1[1] + pos2[1]) / 2

        screen.blit(text_surface, text_rect)

    tools_root.update()
    pygame.display.flip()


pygame.quit()
tools_root.quit()
tools_root.destroy()
