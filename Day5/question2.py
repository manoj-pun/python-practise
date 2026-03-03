#Create a program that takes a list of tuples (name, score) and sorts them by score descending using a
#lambda, then prints a leaderboard.

# def print_leaderboard(data):
#     # Sort by score (index 1 of tuple) in descending order
#     sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

#     print(data)
    
#     print("🏆 Leaderboard 🏆")
#     print("-" * 25)
    
#     for rank, (name, score) in enumerate(sorted_data, start=1):
#         print(f"{rank}. {name} - {score}")


# # Example usage
# players = [
#     ("Manoj", 85),
#     ("David", 92),
#     ("Sita", 78),
#     ("Rohan", 95),
#     ("Gita", 88)
# ]

# print_leaderboard(players)


######
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} - {self.score}"


class Leaderboard:
    def __init__(self, players):
        self.players = players

    def sort_by_score(self):
        # Using .sort() with lambda (descending)
        self.players.sort(key=lambda player: player.score, reverse=True)

    def display(self):
        print("🏆 Leaderboard 🏆")
        print("-" * 25)
        for rank, player in enumerate(self.players, start=1):
            print(f"{rank}. {player.name} - {player.score}")


# Example usage
players_list = [
    Player("Manoj", 85),
    Player("David", 92),
    Player("Sita", 78),
    Player("Rohan", 95),
    Player("Gita", 88)
]

leaderboard = Leaderboard(players_list)
leaderboard.sort_by_score()
leaderboard.display()