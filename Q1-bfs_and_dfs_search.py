
# Data Dictionary
state_space_graph_from_fig1 = {
    "Kartum": ["Humera", "Metema"],
    "Humera": ["Kartum", "Gondar", "Shire"],
    "Shire": ["Humera", "Debarke", "Axum"],
    "Axum": ["Shire", "Adwa", "Asmera"],
    "Asmera": ["Axum", "Adigrat"],
    "Adigrat": ["Asmera", "Adwa", "Mekelle"],
    "Adwa": ["Axum", "Adigrat", "Mekelle"],
    "Metema": ["Kartum", "Azezo", "Gondar"],
    "Debarke": ["Shire", "Gondar"],
    "Gondar": ["Debarke", "Humera", "Metema", "Azezo"],
    "Azezo": ["Metema", "Gondar", "Bahir Dar"],
    "Mekelle": ["Adwa", "Adigrat", "Sekota", "Alamata"],
    "Sekota": ["Mekelle", "Alamata", "Lalibella"],
    "Alamata": ["Mekelle", "Sekota", "Woldia", "Samara"],
    "Kilbet Rasu": ["Fanti Rasu"],
    "Fanti Rasu": ["Kilbet Rasu", "Samara"],
    "Debre Tabor": ["Bahir Dar", "Lalibela"],
    "Bahir Dar": ["Azezo", "Debre Tabor", "Metekel", "Injibara", "Finote Selam"],
    "Lalibella": ["Debre Tabor", "Sekota", "Woldia"],
    "Woldia": ["Lalibella", "Alamata", "Samara", "Dessie"],
    "Samara": ["Fanti Rasu", "Alamata", "Woldia", "Gabi Rasu"],
    "Metekel": ["Bahir Dar", "Assosa"],
    "Injibara": ["Bahir Dar", "Finote Selam"],
    "Finote Selam": ["Injibara", "Bahir Dar", "Debre Markos"],
    "Debre Markos": ["Finote Selam", "Debre Sina"],
    "Dessie": ["Woldia", "Kemise"],
    "Kemise": ["Dessie", "Debre Sina"],
    "Debre Sina": ["Kemise", "Debre Markos", "Debre Birhan"],
    "Gabi Rasu": ["Samara", "Awash"],
    "Assosa": ["Metekel", "Dembi Dollo"],
    "Debre Birhan": ["Debre Sina", "Addis Ababa"],
    "Dembi Dollo": ["Assosa", "Gambella", "Gimbi"],
    "Gimbi": ["Dembi Dollo", "Nekemte"],
    "Nekemte": ["Gimbi", "Bedelle", "Ambo"],
    "Ambo": ["Nekemte", "Wolkite", "Addis Ababa"],
    "Addis Ababa": ["Debre Birhan", "Ambo", "Adama"],
    "Adama": ["Addis Ababa", "Batu", "Assella", "Matahara"],
    "Matahara": ["Adama", "Awash"],
    "Awash": ["Matahara", "Gabi Rasu", "Chiro"],
    "Chiro": ["Awash", "Dire Dawa"],
    "Dire Dawa": ["Chiro", "Harar"],
    "Harar": ["Dire Dawa", "Babile"],
    "Babile": ["Harar", "Jigjiga"],
    "Jigjiga": ["Babile", "Dega Habur"],
    "Dega Habur": ["Jigjiga", "Goba", "Kebri Dehar"],
    "Gambella": ["Dembi Dollo", "Gore"],
    "Gore": ["Gambella", "Tepi", "Bedelle"],
    "Bedelle": ["Nekemte", "Gore", "Jimma"],
    "Jimma": ["Bedelle", "Bonga", "Wolkite"],
    "Wolkite": ["Jimma", "Ambo", "Worabe"],
    "Buta Jirra": ["Worabe", "Batu"],
    "Batu": ["Buta Jirra", "Adama", "Shashemene"],
    "Assella": ["Adama", "Assasa"],
    "Tepi": ["Gore", "Mezan Teferi", "Bonga"],
    "Bonga": ["Tepi", "Dawro", "Jimma", "Mezan Teferi"],
    "Hossana": ["Wolaita Sodo", "Shashemene", "Worabe"],
    "Worabe": ["Hossana", "Wolkite", "Buta Jirra"],
    "Shashemene": ["Hossana", "Hawassa", "Batu"],
    "Assasa": ["Assella", "Dodolla"],
    "Mezan Teferi": ["Tepi", "Bonga", "Basketo"],
    "Dawro": ["Bonga", "Basketo", "Wolaita Sodo"],
    "Wolaita Sodo": ["Dawro", "Arba Minch", "Hossana"],
    "Hawassa": ["Shashemene", "Dilla"],
    "Dodolla": ["Shashemene", "Assasa", "Bale"],
    "Bale": ["Dodolla", "Liben", "Goba", "Sof Oumer"],
    "Liben": ["Bale"],
    "Goba": ["Bale", "Sof Oumer", "Dega Habur"],
    "Sof Oumer": ["Bale", "Goba", "Kebri Dehar"],
    "Kebri Dehar": ["Sof Oumer", "Dega Habur", "Werder", "Gode"],
    "Werder": ["Kebri Dehar"],
    "Gode": ["Kebri Dehar", "Dollo", "Mogadishu"],
    "Dollo": ["Gode"],
    "Mogadishu": ["Gode"],
    "Basketo": ["Bench Maji", "Mezan Teferi", "Dawro", "Arba Minch"],
    "Bench Maji": ["Basketo", "Juba"],
    "Juba": ["Bench Maji"],
    "Arba Minch": ["Wolaita Sodo", "Basketo", "Konso"],
    "Dilla": ["Hawassa", "Bule Hora"],
    "Bule Hora": ["Dilla", "Yabello"],
    "Konso": ["Arba Minch", "Yabello"],
    "Yabello": ["Bule Hora", "Konso", "Moyale"],
    "Moyale": ["Yabello", "Nairobi"],
    "Nairobi": ["Moyale"]
}



from collections import deque

class TravelingEthiopia:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal, strategy="BFS"):
        if strategy == "BFS":
            return self.breadth_first_search(start, goal)
        elif strategy == "DFS":
            return self.depth_first_search(start, goal)
        else:
            raise ValueError("Unsupported search strategy. Use 'BFS' or 'DFS'.")

    def breadth_first_search(self, start, goal):
        queue = deque([(start, [start])])  # Queue stores (current_node, path)
        visited = set()

        while queue:
            current_node, path = queue.popleft()
            if current_node == goal:
                return path

            visited.add(current_node)

            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None  # No path found

    def depth_first_search(self, start, goal):
        stack = [(start, [start])]  # Stack stores (current_node, path)
        visited = set()

        while stack:
            current_node, path = stack.pop()
            if current_node == goal:
                return path

            visited.add(current_node)

            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

        return None  # No path found

travel = TravelingEthiopia(state_space_graph_from_fig1)
start_city = "Addis Ababa"
goal_city = "Shashemene"
print("*************************** Using BSF and DFS Algorithm ****************************")
# Perform BFS
bfs_path = travel.search(start_city, goal_city, strategy="BFS")
print("\nBFS Path:", bfs_path)

# Perform DFS
dfs_path = travel.search(start_city, goal_city, strategy="DFS")
print("\nDFS Path:", dfs_path)