class Algorithme_de_dijkstra:
    def __init__(self, route, lettre_depart: str, lettre_arrive: str, tableau_vide_char: str = "∞", tableau_rempli_char: str = "|"):
        lettre_choisi = []
        tableau_dijkstra = {}
        etapes_dict = {}
        etape_nbr = 0

        for i in route.keys():
            tableau_dijkstra[i] = tableau_vide_char if i != lettre_depart else 0

        while True:
            etapes_dict[f"step {etape_nbr}"] = tableau_dijkstra.copy()

            # on cherche le choix
            choix_potentielle = []
            for i in etapes_dict[f"step {etape_nbr}"].items():
                if type(i[1]) is int:
                    choix_potentielle.append(i)

            choix = min(choix_potentielle, key=lambda x: x[
                1])  # key=lambda x: x[1] car on donne un tuple et ca bug ducoup on prend seuleument la 2eme valeur

            position = choix[0]
            distance = choix[1]
            lettre_choisi.append(position)

            etapes_dict[f"step {etape_nbr}"][
                "choix"] = choix  # on met une virgule aprés position pour montrer qu'on ajoute un tuple

            # on complète le tableau de djikstra à l'etape suivante
            etape_nbr += 1
            if etape_nbr == len(route):
                break

            for i in route.keys():
                if i in lettre_choisi:
                    tableau_dijkstra[i] = tableau_rempli_char

                elif i in route[position]["Chemin"].keys():
                    precedent_contenu = etapes_dict[f"step {etape_nbr - 1}"][i]
                    if type(precedent_contenu) is int and precedent_contenu < distance + route[position]["Chemin"][i][
                        "distance"]:
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

        for i in etapes_dict.values():
            if i['choix'][0] == lettre_arrive:
                distance = i['choix'][1]
                break

        self.meilleur_chemin = chemin
        self.distance = distance
        self.steps = etapes_dict
