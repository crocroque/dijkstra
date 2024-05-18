<h1>Exemple de route :</h1>

    {
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


    {
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
