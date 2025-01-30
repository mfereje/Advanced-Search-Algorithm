import heapq

class AStarSearch:
    def __init__(self, graph, heuristic):

        self.graph = graph
        self.heuristic = heuristic

    def search(self, start, goal):

        open_set = [] # Priority queue of nodes to explore
        heapq.heappush(open_set, (0 + self.heuristic[start], 0, start, [start]))

        visited = set()

        while open_set:
            f_cost, g_cost, current, path = heapq.heappop(open_set)

            if current in visited:
                continue

            visited.add(current)

            # Goal reached
            if current == goal:
                return g_cost, path

            # Explore neighbors
            for neighbor, cost in self.graph.get(current, []):
                if neighbor not in visited:
                    new_g_cost = g_cost + cost
                    new_f_cost = new_g_cost + self.heuristic[neighbor]
                    heapq.heappush(open_set, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))

        return float('inf'), []  # If no path is found

heuristics = {
        "Kartum": 81,
        "Humera": 65,
        "Shire": 67,
        "Axum": 66,
        "Asmera": 68,
        "Adigrat": 62,
        "Adwa": 65,
        "Metema": 62,
        "Debarke": 60,
        "Gondar": 56,
        "Azezo": 55,
        "Mekelle": 58,
        "Sekota": 59,
        "Alamata": 53,
        "Kilbet Rasu": 55,
        "Fanti Rasu": 49,
        "Debre Tabor": 52,
        "Bahir Dar": 48,
        "Lalibela": 57,
        "Woldia": 50,
        "Samara": 42,
        "Metekel": 59,
        "Injibara": 44,
        "Finote Selam": 42,
        "Debre Markos": 39,
        "Dessie": 44,
        "Kemise": 40,
        "Debre Sina": 33,
        "Gabi Rasu": 32,
        "Assosa": 51,
        "Debre Birhan": 31,
        "Dembi Dollo": 49,
        "Gimbi": 43,
        "Nekemte": 39,
        "Ambo": 31,
        "Addis Ababa": 26,
        "Adama": 23,
        "Matahara": 26,
        "Awash": 27,
        "Chiro": 31,
        "Dire Dawa": 31,
        "Harar": 35,
        "Babile": 37,
        "Jigjiga": 40,
        "Dega Habur": 45,
        "Gambella": 51,
        "Gore": 46,
        "Bedelle": 40,
        "Jimma": 33,
        "Wolkite": 25,
        "Buta Jirra": 21,
        "Batu": 19,
        "Assella": 22,
        "Tepi": 41,
        "Bonga": 33,
        "Hossana": 21,
        "Worabe": 22,
        "Shashemene": 16,
        "Assasa": 18,
        "Mezan Teferi": 37,
        "Dawro": 23,
        "Wolaita Sodo": 17,
        "Hawassa": 15,
        "Dodolla": 19,
        "Robe": 22,
        "Liben": 11,
        "Goba": 40,
        "Sof Oumer": 45,
        "Kebri Dehar": 40,
        "Werder": 46,
        "Gode": 35,
        "Dollo": 18,
        "Mokadisho": 40,
        "Basketo": 23,
        "Bench Maji": 28,
        "Juba": 50,
        "Arba Minch": 13,
        "Dilla": 12,
        "Bule Hora": 8,
        "Konso": 9,
        "Yabello": 6,
        "Moyale": 0,
        "Nairobi": 22
    }
    # Define the state space graph (example structure)
state_space_graph_from_fig3= {
        "Kartum":[
            ("Humera", 21),
        ("Metema", 19  )],

        "Humera":[
            ( "Kartum",21),
        ( "Gondar", 9),
        ("Shire", 8)],

        "Shire":[
            ( "Humera", 8),
            ("Debarke",7),
            ("Axum", 2)
        ],
        "Axum":[
            ("Shire", 2),
            ("Adwa", 1),
            ("Asmera", 5)
    ],
        "Asmera":[
            ("Axum", 5),
           ( "Adigrat", 9)
        ],
        "Adigrat":[
           ( "Asmera",9),
           ( "Adwa",4),
        ( "Mekelle", 4)
        ],
        "Adwa":[
            ("Axum", 1),
            ("Adigrat", 4),
            ("Mekelle", 7)
        ],
        "Metema":[
            ("Kartum", 19),
           ( "Azezo", 7),
           ( "Gondar", 7)
        ],
        "Debarke":[
           ( "Shire", 7),
            ("Gondar",4)
        ],
        "Gondar":[
            ("Debarke", 4),
            ("Humera", 9),
           ( "Metema",7),
           ( "Azezo", 1),
           ( "Debre Tabor", 6)
        ],
        "Azezo":[
           ( "Metema",7),
           ( "Gondar",1),
           ( "Bahir Dar", 7)
        ],
        "Mekelle":[
            ("Adwa", 7),
           ( "Adigrat", 4),
            ("Sekota", 9),
            ("Alamata", 5)
        ],
        "Sekota":[
            ("Mekelle",9),
           ( "Alamata",6),
           ( "Lalibela",6)
        ],
        "Alamata":[
           ( "Mekelle",5),
           ( "Sekota",6),
           ( "Woldia",3),
           ( "Samara",11)
        ],
        "Kilbet Rasu":[
          (  "Fanti Rasu",6)
        ],
        "Fanti Rasu":[
           ( "Kilbet Rasu",6),
           ( "Samara",7)
        ],
        "Debre Tabor":[
           ( "Bahir Dar",4),
           ( "Lalibela",8),
           ( "Gondar",6)
        ],
        "Bahir Dar":[
           ( "Azezo",7),
           ( "Debre Tabor",4),
            ("Metekel",11),
            ("Injibara",4),
           ( "Finote Selam",6)
        ],
        "Lalibela":[
           ( "Debre Tabor",8),
          (  "Sekota",6),
           ( "Woldia",7)
        ],
        "Woldia":[
           ( "Lalibela",7),
          (  "Alamata",3),
           ( "Samara",8),
          (  "Dessie",6)
        ],
        "Samara":[
           ( "Fanti Rasu",7),
          (  "Alamata",11),
          (  "Woldia",8),
          (  "Gabi Rasu",10)
        ],
        "Metekel":[
          (  "Bahir Dar",11)
        ],
        "Injibara":[
          (  "Bahir Dar",4),
           ( "Finote Selam",2)
        ],
        "Finote Selam":[
            ("Injibara",2),
           ( "Bahir Dar",6),
           ( "Debre Markos",3)
        ],
        "Debre Markos":[
           ( "Finote Selam",3),
          (  "Debre Sina",17),
          (  "Addis Ababa",13)
        ],
        "Dessie":[
            ("Woldia",6),
          (  "Kemise",4)
        ],
        "Kemise":[
           ( "Dessie",4),
           ( "Debre Sina",7)
        ],
        "Debre Sina":[
            ("Kemise",7),
           ( "Debre Markos",17),
          (  "Debre Birhan",2)
        ],
        "Gabi Rasu":[
           ( "Samara",10),
           ( "Awash",5)
        ],
        "Assosa":[
           ( "Dembi Dollo",12),
           ( "Gimbi",8)
        ],
        "Debre Birhan":[
           ( "Debre Sina",2),
            ("Addis Ababa",5)
        ],
        "Dembi Dollo":[
            ("Assosa",12),
            ("Gambella",4),
            ("Gimbi",6)
        ],
        "Gimbi":[
            ("Dembi Dollo",6),
           ( "Nekemte",4),
            ("Assosa",8)
        ],
        "Nekemte":[
           ( "Gimbi",4),
            ("Bedelle",4),
            ("Ambo",8)
        ],
        "Ambo":[
           ( "Nekemte",8),
            ("Wolkite",6),
            ("Addis Ababa",5)
        ],
        "Addis Ababa":[
            ("Debre Birhan",5),
           ( "Ambo",5),
           ( "Adama",3),
            ("Debre Markos",13)
        ],
        "Adama":[
            ("Addis Ababa",3),
            ("Batu",4),
            ("Assella",4),
           ( "Matahara",3)
        ],
        "Matahara":[
           ( "Adama",3),
            ("Awash",1)
        ],
        "Awash":[
            ("Matahara",1),
            ("Gabi Rasu",5),
            ("Chiro",4)
        ],
        "Chiro":[
           ( "Awash",4),
           ( "Dire Dawa",8)
        ],
        "Dire Dawa":[
           ( "Chiro",8),
           ( "Harar",4)
        ],
        "Harar":[
            ("Dire Dawa",4),
           ( "Babile",2)
        ],
        "Babile":[
           ( "Harar",2),
            ("Jigjiga",3),
           ( "Goba",28)
        ],
        "Jigjiga":[
            ("Babile",3),
            ("Dega Habur",5)
        ],
        "Dega Habur":[
           ( "Jigjiga",5),
           ( "Kebri Dehar",6),
        ],
        "Gambella":[
           ( "Dembi Dollo",4),
           ( "Gore",5)
        ],
        "Gore":[
            ("Gambella",5),
           ( "Tepi",9),
           ( "Bedelle",6)
        ],
        "Bedelle":[
           ( "Nekemte",4),
            ("Gore",6),
           ( "Jimma",7)
        ],
        "Jimma":[
            ("Bedelle",7),
           ( "Bonga",4),
           ( "Wolkite",8)
        ],
        "Wolkite":[
            ("Jimma",8),
            ("Ambo",6),
            ("Worabe",5),
           ( "Hossana",5),
            ("Buta Jirra",4)
        ],
        "Buta Jirra":[
           ( "Worabe",2),
            ("Batu",2),
            ("Wolkite",4)
        ],



        "Batu":[
            ("Buta Jirra",2),
           ( "Adama",4),
            ("Shashemene",3)
        ],
        "Assella":[
            ("Adama",4),
            ("Assasa",4)
        ],
        "Tepi":[
           ( "Gore",9),
            ("Mezan Teferi",4),
            ("Bonga",8)
        ],
        "Bonga":[
            ("Tepi",8),
           ( "Dawro",10),
          (  "Jimma",4),
           ( "Mezan Teferi",4)
        ],
        "Hossana":[
           ( "Wolaita Sodo",4),
            ("Shashemene",7),
            ("Worabe",2),
           ( "Wolkite",5)
        ],
        "Worabe":[
            ("Hossana",2),
            ("Buta Jirra",2),
            ("Wolkite",5),
           ( "Shashemene",6)
        ],
        "Shashemene":[
            ("Hossana",7),
            ("Hawassa",1),
           ( "Batu",3),
            ("Dodolla",3),
            ("Worabe",6)
        ],
        "Assasa":[
          (  "Assella",4),
           ( "Dodolla",1)
        ],
        "Mezan Teferi":[
           ( "Tepi",4),
           ( "Bonga",4)
        ],
        "Dawro":[
            ("Bonga",10),
           ( "Wolaita Sodo",6)
        ],
        "Wolaita Sodo":[
            ("Dawro",6),
            ("Arba Minch",4),
           ( "Hossana",4)
        ],
        "Hawassa":[
           ( "Shashemene",1),
           ( "Dilla",3)
        ],
        "Dodolla":[
           ( "Shashemene",3),
           ( "Assasa",1),
            ("Robe",13)
        ],
        "Robe":[
            ("Dodolla",13),
            ("Liben",11),
           ( "Goba",18),
           ( "Sof Oumer",23)
        ],
        "Liben":[
           ( "Robe",11),
           ( "Moyale",11)
        ],
        "Goba":[
           ( "Robe",18),
          (  "Sof Oumer",6),
           ( "Babile",28)
        ],
        "Sof Oumer":[
           ( "Robe",23),
          (  "Goba",6),
           ( "Gode",23)
        ],
        "Kebri Dehar":[
            ("Dega Habur",6),
           ( "Werder",6),
           ( "Gode",5)
        ],
        "Werder":[(
            "Kebri Dehar",6
        )],
        "Gode":[
           ( "Kebri Dehar",5),
            ("Dollo",17),
           ( "Mokadisho",22),
           ( "Sof Oumer",23)
        ],
        "Dollo":[
           ( "Gode",17),
           ( "Moyale",18)
        ],
        "Mokadisho":[
            ("Gode",22),
            ("Moyale",40)
        ],
        "Basketo":[
            ("Bench Maji",5),
            ("Arba Minch",10)
        ],
        "Bench Maji":[
            ("Basketo",5),
            ("Juba",22)
        ],
        "Juba":[(
            "Bench Maji",22
        )],
        "Arba Minch":[
           ( "Wolaita Sodo",4),
            ("Basketo",10),
           ( "Konso",4)
        ],
        "Dilla":[
            ("Hawassa",3),
            ("Bule Hora",4)
        ],
        "Bule Hora":[
           ( "Dilla",4),
          (  "Yabello",2)
        ],
        "Konso":[
           ( "Arba Minch",4),
           ( "Yabello",3)
        ],
        "Yabello":[
            ("Bule Hora",2),
            ("Konso",3),
            ("Moyale",6)
        ],
        "Moyale":[
            ("Yabello",6),
            ("Nairobi",22),
            ("Liben",11),
           ( "Dollo",18),
           ( "Mokadisho",40)
        ],
        "Nairobi":[(
            "Moyale",22)]

        }

initial_state = "Addis Ababa"
goal_state = "Moyale"
astar = AStarSearch(state_space_graph_from_fig3, heuristics)


cost, path = astar.search(initial_state, goal_state)
print(f"Start: {initial_state} -> Goal: Moyale")
print(f"Total Cost: {cost}")
print(f"Path: {' -> '.join(path)}\n")

