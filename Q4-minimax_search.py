class MiniMax:
    def __init__(self, graph):
        self.graph = graph

    def minimax(self, state, depth, maximizing_player):
        # Base case: if depth is 0 or the state has a utility value
        if depth == 0 or self.graph[state]["utility"] is not None:
            return self.graph[state]["utility"]

        neighbors = self.graph[state]["neighbors"]

        if maximizing_player:
            max_eval = float('-inf')
            for neighbor in neighbors:
                eval = self.minimax(neighbor, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for neighbor in neighbors:
                eval = self.minimax(neighbor, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, start, depth):
        best_value = float('-inf')
        best_state = None

        for neighbor in self.graph[start]["neighbors"]:
            move_value = self.minimax(neighbor, depth - 1, False)
            if move_value > best_value:
                best_value = move_value
                best_state = neighbor

        return best_state, best_value



state_space_graph_from_fig4= {
        "Shambu": {"neighbors": ["Gedo"], "utility": 4},
        "Fincha": {"neighbors": ["Gedo"], "utility": 5},
        "Gedo": {"neighbors": ["Shambu", "Fincha", "Ambo"], "utility": 0},
        "Gimbi": {"neighbors": ["Nekemte"], "utility": 8},
        "Ambo": {"neighbors": ["Gedo", "Nekemte", "Addis Ababa"], "utility": 0},
        "Addis Ababa": {"neighbors": ["Ambo", "Buta Jirra", "Adama"], "utility": 0},
        "Nekemte": {"neighbors": ["Gimbi", "Limu", "Ambo"], "utility": 0},
        "Limu": {"neighbors": ["Nekemte"], "utility": 8},
        "Adama": {"neighbors": ["Addis Ababa", "Mojo", "Dire Dawa"], "utility": 0},
        "Buta Jirra": {"neighbors": ["Addis Ababa", "Worabe", "Wolkite"], "utility": 0},
        "Dire Dawa": {"neighbors": ["Adama", "Harar", "Chiro"], "utility": 0},
        "Harar": {"neighbors": ["Dire Dawa"], "utility": 10},
        "Chiro": {"neighbors": ["Dire Dawa"], "utility": 6},
        "Worabe": {"neighbors": ["Buta Jirra", "Hossana", "Durame"], "utility": 0},
        "Wolkite": {"neighbors": ["Buta Jirra", "Bench Maji", "Tepi"], "utility": 0},
        "Hossana": {"neighbors": ["Worabe"], "utility": 6},
        "Durame": {"neighbors": ["Worabe"], "utility": 5},
        "Bench Maji": {"neighbors": ["Wolkite"], "utility": 5},
        "Tepi": {"neighbors": ["Wolkite"], "utility": 6},
        "Mojo": {"neighbors": ["Adama", "Kaffa", "Dilla"], "utility": 0},
        "Kaffa": {"neighbors": ["Mojo"], "utility": 7},
        "Dilla": {"neighbors": ["Mojo"], "utility": 9}
    }



minimax = MiniMax(state_space_graph_from_fig4)
start_state = "Addis Ababa"  # Starting state for the agent
depth = 6  # Depth limit for the search

best_state, best_value = minimax.best_move(start_state, depth)
print(f"\nBest move from {start_state} is to {best_state} with a utility of {best_value}")


