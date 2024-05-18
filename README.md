<h1>Exemple de route :</h1>

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

    
![^^](/DijkstraExemple.png")
