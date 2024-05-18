
 
# Exemple de route 1 :
    Route_Exemple1 = {
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


![alt text](https://github.com/crocroque/dijkstra/blob/main/DijkstraExample.png)


# Exemple de route 2 :
    Route_Exemple2 = {
        "A": {"Chemin": {"B": {"distance": 12}, "D": {"distance": 14}}},
        "B": {"Chemin": {"A": {"distance": 12}, "F": {"distance": 9}, "H": {"distance": 21}, "G": {"distance": 16}}},
        "C": {"Chemin": {"E": {"distance": 13}, "F": {"distance": 10}}},
        "D": {"Chemin": {"A": {"distance": 14}, "E": {"distance": 10}}},
        "E": {"Chemin": {"D": {"distance": 10}, "C": {"distance": 13}, "H": {"distance": 10}, "F": {"distance": 16}}},
        "F": {"Chemin": {"B": {"distance": 9}, "C": {"distance": 10}, "E": {"distance": 16}, "H": {"distance": 11}}},
        "G": {"Chemin": {"B": {"distance": 16}, "H": {"distance": 11}}},
        "H": {"Chemin": {"E": {"distance": 10}, "F": {"distance": 11}, "B": {"distance": 21}, "G": {"distance": 11}}},
    }

![alt text](https://github.com/crocroque/dijkstra/blob/main/DijkstraExample2.png)

# Exemple de code :
    from dijkstra import Algorithme_de_dijkstra
    
    algo = Algorithme_de_dijkstra(route=Route_Exemple2, lettre_depart="A", lettre_arrive="H")

    print(algo.meilleur_chemin)
    
> ['A', 'B', 'F', 'H']

    print(algo.distance)
    
> 32

    print(algo.tableau)

> {

> 'step 0': {'A': 0, 'B': '∞', 'C': '∞', 'D': '∞', 'E': '∞', 'F': '∞', 'G': '∞', 'H': '∞', 'choix': ('A', 0)},

>  'step 1': {'A': '|', 'B': 12, 'C': '∞', 'D': 14, 'E': '∞', 'F': '∞', 'G': '∞', 'H': '∞', 'choix': ('B', 12, 'A')},

>  'step 2': {'A': '|', 'B': '|', 'C': '∞', 'D': 14, 'E': '∞', 'F': 21, 'G': 28, 'H': 33, 'choix': ('D', 14, 'A')},

>  'step 3': {'A': '|', 'B': '|', 'C': '∞', 'D': '|', 'E': 24, 'F': 21, 'G': 28, 'H': 33, 'choix': ('F', 21, 'B')},

>  'step 4': {'A': '|', 'B': '|', 'C': 31, 'D': '|', 'E': 24, 'F': '|', 'G': 28, 'H': 32, 'choix': ('E', 24, 'D')},

>  'step 5': {'A': '|', 'B': '|', 'C': 31, 'D': '|', 'E': '|', 'F': '|', 'G': 28, 'H': 32, 'choix': ('G', 28, 'B')},

>  'step 6': {'A': '|', 'B': '|', 'C': 31, 'D': '|', 'E': '|', 'F': '|', 'G': '|', 'H': 32, 'choix': ('C', 31, 'F')},

>  'step 7': {'A': '|', 'B': '|', 'C': '|', 'D': '|', 'E': '|', 'F': '|', 'G': '|', 'H': 32, 'choix': ('H', 32, 'F')}}
