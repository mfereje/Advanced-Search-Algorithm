import heapq

# Graph representation as an adjacency list
state_space_graph_from_fig2= {
        "Kartum": [("Humera", 21), ("Metema", 19)],
        "Humera": [("Kartum", 21), ("Gondar", 9), ("Shire", 8)],
        "Shire": [("Humera", 8), ("Debarke", 7), ("Axum", 2)],
        "Axum": [("Shire", 2), ("Adwa", 1), ("Asmera", 5)],
        "Asmera": [("Axum", 5), ("Adigrat", 9)],
        "Adigrat": [("Asmera", 9), ("Adwa", 4), ("Mekelle", 4)],
        "Adwa": [("Axum", 1), ("Adigrat", 4), ("Mekelle", 7)],
        "Metema": [("Kartum", 19), ("Azezo", 7), ("Gondar", 7)],
        "Debarke": [("Shire", 7), ("Gondar", 4)],
        "Gondar": [("Debarke", 4), ("Humera", 9), ("Metema", 7), ("Azezo", 1)],
        "Azezo": [("Metema", 7), ("Gondar", 1), ("Bahir Dar", 7)],
        "Mekelle": [("Adwa", 7), ("Adigrat", 4), ("Sekota", 9), ("Alamata", 5)],
        "Sekota": [("Mekelle", 9), ("Alamata", 6), ("Lalibela", 6)],
        "Alamata": [("Mekelle", 5), ("Sekota", 6), ("Woldia", 3), ("Samara", 11)],
        "Kilbet Rasu": [("Fanti Rasu", 6)],
        "Fanti Rasu": [("Kilbet Rasu", 6), ("Samara", 7)],
        "Debre Tabor": [("Bahir Dar", 4), ("Lalibela", 8)],
        "Bahir Dar": [("Azezo", 7), ("Debre Tabor", 4), ("Metekel", 11), ("Injibara", 4), ("Finote Selam", 6)],
        "Lalibela": [("Debre Tabor", 8), ("Sekota", 6), ("Woldia", 7)],
        "Woldia": [("Lalibela", 7), ("Alamata", 3), ("Samara", 8), ("Dessie", 6)],
        "Samara": [("Fanti Rasu", 7), ("Alamata", 11), ("Woldia", 8), ("Gabi Rasu", 9)],
        "Metekel": [("Bahir Dar", 11)],
        "Injibara": [("Bahir Dar", 4), ("Finote Selam", 2)],
        "Finote Selam": [("Injibara", 2), ("Bahir Dar", 6), ("Debre Markos", 3)],
        "Debre Markos": [("Finote Selam", 3), ("Debre Sina", 17)],
        "Dessie": [("Woldia", 6), ("Kemise", 4)],
        "Kemise": [("Dessie", 4), ("Debre Sina", 6)],
        "Debre Sina": [("Kemise", 6), ("Debre Markos", 17), ("Debre Birhan", 2)],
        "Gabi Rasu": [("Samara", 9), ("Awash", 5)],
        "Assosa": [("Dembi Dollo", 12)],
        "Debre Birhan": [("Debre Sina", 2), ("Addis Ababa", 5)],
        "Dembi Dollo": [("Assosa", 12), ("Gambella", 4), ("Gimbi", 6)],
        "Gimbi": [("Dembi Dollo", 6), ("Nekemte", 4)],
        "Nekemte": [("Gimbi", 4), ("Bedelle", 0), ("Ambo", 9)],
        "Ambo": [("Nekemte", 9), ("Wolkite", 6), ("Addis Ababa", 5)],
        "Addis Ababa": [("Debre Birhan", 5), ("Ambo", 5), ("Adama", 3)],
        "Adama": [("Addis Ababa", 3), ("Batu", 4), ("Assella", 4), ("Matahara", 3)],
        "Matahara": [("Adama", 3), ("Awash", 1)],
        "Awash": [("Matahara", 1), ("Gabi Rasu", 5), ("Chiro", 4)],
        "Chiro": [("Awash", 4), ("Dire Dawa", 8)],
        "Dire Dawa": [("Chiro", 8), ("Harar", 4)],
        "Harar": [("Dire Dawa", 4), ("Babile", 2)],
        "Babile": [("Harar", 2), ("Jigjiga", 3), ("Goba", 28)],
        "Jigjiga": [("Babile", 3), ("Dega Habur", 5)],
        "Dega Habur": [("Jigjiga", 5), ("Kebri Dehar", 6)],
        "Gambella": [("Dembi Dollo", 4), ("Gore", 5)],
        "Gore": [("Gambella", 5), ("Tepi", 9), ("Bedelle", 6)],
        "Bedelle": [("Nekemte", 0), ("Gore", 6), ("Jimma", 7)],
        "Jimma": [("Bedelle", 7), ("Bonga", 4), ("Wolkite", 8)],
        "Wolkite": [("Jimma", 8), ("Ambo", 6), ("Worabe", 5)],
        "Buta Jirra": [("Worabe", 2), ("Batu", 2)],
        "Batu": [("Buta Jirra", 2), ("Adama", 4), ("Shashemene", 3)],
        "Assella": [("Adama", 4), ("Assasa", 4)],
        "Tepi": [("Gore", 9), ("Mezan Teferi", 4), ("Bonga", 8)],
        "Bonga": [("Tepi", 8), ("Dawro", 10), ("Jimma", 4), ("Mezan Teferi", 4)],
        "Hossana": [("Wolaita Sodo", 4), ("Shashemene", 7), ("Worabe", 2)],
        "Worabe": [("Hossana", 2), ("Buta Jirra", 2), ("Wolkite", 5)],
        "Shashemene": [("Hossana", 7), ("Hawassa", 1), ("Batu", 3), ("Dodolla", 3)],
        "Assasa": [("Assella", 4), ("Dodolla", 1)],
        "Mezan Teferi": [("Tepi", 4), ("Bonga", 4)],
        "Dawro": [("Bonga", 10), ("Wolaita Sodo", 6)],
        "Wolaita Sodo": [("Dawro", 6), ("Arba Minch", 0), ("Hossana", 4)],
        "Hawassa": [("Shashemene", 1), ("Dilla", 3)],
        "Dodolla": [("Shashemene", 3), ("Assasa", 1), ("Bale", 13)],
        "Bale": [("Dodolla", 13), ("Liben", 11), ("Goba", 18), ("Sof Oumer", 23)],
        "Liben": [("Bale", 11)],
        "Goba": [("Bale", 18), ("Sof Oumer", 6), ("Babile", 28)],
        "Sof Oumer": [("Bale", 23), ("Goba", 6), ("Gode", 23)],
        "Kebri Dehar": [("Dega Habur", 6), ("Werder", 6), ("Gode", 5)],
        "Werder": [("Kebri Dehar", 6)],
        "Gode": [("Kebri Dehar", 5), ("Dollo", 17), ("Mogadishu", 22), ("Sof Oumer", 23)],
        "Dollo": [("Gode", 17)],
        "Mogadishu": [("Gode", 22)],
        "Basketo": [("Bench Maji", 5), ("Arba Minch", 10)],
        "Bench Maji": [("Basketo", 5), ("Juba", 22)],
        "Juba": [("Bench Maji", 22)],
        "Arba Minch": [("Wolaita Sodo", 0), ("Basketo", 10), ("Konso", 4)],
        "Dilla": [("Hawassa", 3), ("Bule Hora", 4)],
        "Bule Hora": [("Dilla", 4), ("Yabello", 3)],
        "Konso": [("Arba Minch", 4), ("Yabello", 3)],
        "Yabello": [("Bule Hora", 3), ("Konso", 3), ("Moyale", 6)],
        "Moyale": [("Yabello", 6), ("Nairobi", 22)],
        "Nairobi": [("Moyale", 22)]
    }


# Uniform Cost Search
def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, []))  # (cost, city, path)
    visited = set()

    while priority_queue:
        cost, city, path = heapq.heappop(priority_queue)

        if city in visited:
            continue
        visited.add(city)
        path = path + [city]

        # Check if we reached the goal
        if city == goal:
            return cost, path

        # Explore neighbors
        for neighbor, neighbor_cost in graph.get(city, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + neighbor_cost, neighbor, path))

    return float("inf"), []  # No path found


# Customized UCS for visiting all goal states
def visit_all_goals(graph, start, goals):
    total_cost = 0
    current_city = start
    visited_goals = set()
    path = []

    while len(visited_goals) < len(goals):
        # Find the closest unvisited goal
        remaining_goals = [goal for goal in goals if goal not in visited_goals]
        closest_goal = None
        closest_cost = float("inf")
        shortest_path = []

        for goal in remaining_goals:
            cost, goal_path = uniform_cost_search(graph, current_city, goal)
            if cost < closest_cost:
                closest_goal = goal
                closest_cost = cost
                shortest_path = goal_path

        # Update total cost and visited goals
        total_cost += closest_cost
        visited_goals.add(closest_goal)
        current_city = closest_goal
        path += shortest_path[:-1]  # Avoid duplicate cities

    path.append(current_city)  # Add the final city
    return total_cost, path


# Example usage
start_city = "Addis Ababa"
goal_city = "Lalibela"
print("\n *********Uniform Cost Search (Addis Ababa -> Lalibela):  *************")
cost, path = uniform_cost_search(state_space_graph_from_fig2, start_city, goal_city)
print(f"\nCost: {cost},\n Path:  {' -> '.join(path)}")

goal_states = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minch"]
print("\n***********Customized Uniform Cost Search (Visit All Goals): **************")
total_cost, full_path = visit_all_goals(state_space_graph_from_fig2, start_city, goal_states)
print(f"\nTotal Cost: {total_cost},\n Path: {' -> '.join(full_path)}")

