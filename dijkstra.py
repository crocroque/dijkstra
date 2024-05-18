
    def __init__(self, route, lettre_depart: str, lettre_arrive: str):
    lettre_choisi = []
    tableau_dijkstra = {}
    etapes_dict = {}
    etape_nbr = 0

    for i in route.keys():
        tableau_dijkstra[i] = "-" if i != lettre_depart else 0

    while True:
        etapes_dict[f"step {etape_nbr}"] = tableau_dijkstra.copy()

        # on cherche le choix
        choix_potentielle = []
        for i in etapes_dict[f"step {etape_nbr}"].items():
            if type(i[1]) is int:
                choix_potentielle.append(i)

        choix = min(choix_potentielle, key=lambda x: x[1]) # key=lambda x: x[1] car on donne un tuple et ca bug ducoup on prend seuleument la 2eme valeur


        position = choix[0]
        distance = choix[1]
        lettre_choisi.append(position)

        etapes_dict[f"step {etape_nbr}"]["choix"] = choix  # on met une virgule aprés position pour montrer qu'on ajoute un tuple

        # on complète le tableau de djikstra à l'etape suivante
        etape_nbr += 1
        if etape_nbr == len(route):
            break

        for i in route.keys():
            if i in lettre_choisi:
                tableau_dijkstra[i] = "|"

            elif i in route[position]["Chemin"].keys():
                precedent_contenu = etapes_dict[f"step {etape_nbr - 1}"][i]
                if type(precedent_contenu) is int and precedent_contenu < distance + route[position]["Chemin"][i]["distance"]:
                    tableau_dijkstra[i] = precedent_contenu
                    continue
                tableau_dijkstra[i] = distance + route[position]["Chemin"][i]["distance"]

    lettre_historique = {}

    for i in etapes_dict.values():
        for m in i.items():
            if m[0] == "choix":
                continue
            try:
                lettre_historique[m[0]].append(m[1])
            except:
                lettre_historique[m[0]] = [m[1]]


    lettre_index = {}

    for i in lettre_historique.items():
        mini = min(x for x in i[1] if isinstance(x, int))
        lettre_index[i[0]] = i[1].index(mini)

    list_lettre_origine = []

    for i in etapes_dict.values():
        nom_lettre = i['choix'][0]
        try:
            list_lettre_origine.append(etapes_dict[f"step {lettre_index[nom_lettre] - 1}"]["choix"][0])
        except:
            pass


    for i in range(1, len(etapes_dict)):
        etapes_dict[f"step {i}"]["choix"] += (list_lettre_origine[i - 1],)

    chemin = []
    prochaine_lettre = lettre_arrive
    for i in reversed(etapes_dict.values()):
        if i["choix"][0] == prochaine_lettre:
            chemin.append(i["choix"][0])
            if i["choix"][0] == lettre_depart:
                break
            prochaine_lettre = i["choix"][2]

    chemin.reverse()
    return {"meilleur chemin": chemin, "distance": distance, "tableau": etapes_dict}


def afficher_tableau(tableau: dict):
    x = tableau["step 0"]

    for i in x:

        print(f"   {i}  ▕", end="")

    print()

    for n in tableau.values():
        for m in n.values():
            if type(m) is tuple:
                if len(m) == 2:
                    print(f" {m[0]}({m[1]})", end="")
                else:
                    print(f" {m[0]}({m[1]}) {m[2]}", end="")
                continue
            print(f'  {str(m):4}▕', end="")
        print()

if __name__ == '__main__':
    route_wikipedia = {
        "A": {"Chemin": {"B": {"distance": 85}, "C": {"distance": 217}, "E": {"distance": 173}}},
        "B": {"Chemin": {"A": {"distance": 85}, "F": {"distance": 80}}},
        "C": {"Chemin": {"A": {"distance": 217}, "G": {"distance": 186}, "H": {"distance": 103}}},
        "D": {"Chemin": {"H": {"distance": 183}}},
        "E": {"Chemin": {"A": {"distance": 173}, "J": {"distance": 502}}},
        "F": {"Chemin": {"B": {"distance": 80}, "I": {"distance": 250}}},
        "G": {"Chemin": {"C": {"distance": 186}}},
        "H": {"Chemin": {"C": {"distance": 103}, "D": {"distance": 183}, "J": {"distance": 167}}},
        "I": {"Chemin": {"F": {"distance": 250}, "J": {"distance": 84}}},
        "J": {"Chemin": {"I": {"distance": 84}, "H": {"distance": 167}, "E": {"distance": 502}}},
    }



    route_video_yt = {
        "A": {"Chemin": {"B": {"distance": 12}, "D": {"distance": 14}}},
        "B": {"Chemin": {"A": {"distance": 12}, "F": {"distance": 9}, "H": {"distance": 21}, "G": {"distance": 16}}},
        "C": {"Chemin": {"E": {"distance": 13}, "F": {"distance": 10}}},
        "D": {"Chemin": {"A": {"distance": 14}, "E": {"distance": 10}}},
        "E": {"Chemin": {"D": {"distance": 10}, "C": {"distance": 13}, "H": {"distance": 10}, "F": {"distance": 16}}},
        "F": {"Chemin": {"B": {"distance": 9}, "C": {"distance": 10}, "E": {"distance": 16}, "H": {"distance": 11}}},
        "G": {"Chemin": {"B": {"distance": 16}, "H": {"distance": 11}}},
        "H": {"Chemin": {"E": {"distance": 10}, "F": {"distance": 11}, "B": {"distance": 21}, "G": {"distance": 11}}},
    }


    print(algorithme_de_dijkstra(route_video_yt, "A", "H"))

    for i in algorithme_de_dijkstra(route_video_yt, "A", "H")["tableau"].values():
        print(i["choix"])
    # PROBLEME QUAND ON VEUT FAIRE UN CHEMIN AVEC D
