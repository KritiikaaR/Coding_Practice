import random
from collections import deque

# Base class for all board blocks
class Block:
    def __init__(self, name, position):
        self.name = name       
        self.position = position  # Position on the board

class PropertyBlock(Block):
    # Represents a property that can be bought
    def __init__(self, name, position, price, rent):
        super().__init__(name, position)
        self.price = price      # Purchase price
        self.rent = rent        # Rent charged if landed on
        self.owner = None       # Owner of the property (None if unowned)

# Represents a "Chance" block
class ChanceBlock(Block):
    def __init__(self, position):
        super().__init__("Chance", position)

# Represents the "Go" block (starting position)
class GoBlock(Block):
    def __init__(self, position):
        super().__init__("Go", position)


# BST for Property Sorting
class TreeNode:
    def __init__(self, property_block):
        self.property = property_block
        self.left = None
        self.right = None

 # BST to keep properties sorted by price
class PropertyBST:
    def __init__(self):
        self.root = None

    def insert(self, property_block):
        def _insert(node, block):
            if not node:
                return TreeNode(block)
            if block.price < node.property.price:
                node.left = _insert(node.left, block)
            else:
                node.right = _insert(node.right, block)
            return node
        self.root = _insert(self.root, property_block)


# Return properties in ascending order of price
    def in_order(self):
        result = []
        def _in_order(node):
            if node:
                _in_order(node.left)
                result.append(f"{node.property.name} (${node.property.price})")
                _in_order(node.right)
        _in_order(self.root)
        return result


# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0       # Current position on the board
        self.properties = []    # List of owned properties
        self.balance = 500      # Starting balance


# Game Setup
board = [
    GoBlock(0),
    PropertyBlock("Mediterranean Ave", 1, 60, 2),
    ChanceBlock(2),
    PropertyBlock("Baltic Ave", 3, 60, 4),
    PropertyBlock("Reading Railroad", 4, 200, 25)
]

chance_deck = deque([
    "Pay $50",
    "Collect $100",
    "Move forward 2 spaces",
    "Go to Start"
])

move_history = []             # Track all moves
property_tree = PropertyBST()  # Tree to store purchased properties


# Main Game Logic
def main():
    num_players = int(input("Enter number of players: "))
    players = [Player(f"Player {i+1}") for i in range(num_players)]
    num_turns = 5  # Total number of turns

    for turn in range(num_turns):
        print(f"\n--- Turn {turn + 1} ---")
        for player in players:
            roll = random.randint(1, 6)  # Dice roll
            player.position = (player.position + roll) % len(board)
            block = board[player.position]
            print(f"{player.name} rolled {roll} and landed on {block.name} (Position {player.position})")

            # If landed on a property
            if isinstance(block, PropertyBlock):
                print(f"Property: {block.name}, Price: ${block.price}, Rent: ${block.rent}")
                if not block.owner:  # If property is unowned
                    if player.balance >= block.price:
                        block.owner = player.name
                        property_tree.insert(block)
                        player.properties.append(block)
                        player.balance -= block.price
                        move_history.append(f"{player.name} purchased {block.name} for ${block.price}")
                    else:
                        move_history.append(f"{player.name} could not afford {block.name}")
                else:
                    # Pay rent to the owner if someone else owns it
                    if block.owner != player.name:
                        player.balance -= block.rent
                        move_history.append(f"{player.name} paid ${block.rent} rent to {block.owner}")

            # If landed on a chance block
            elif isinstance(block, ChanceBlock):
                card = chance_deck.popleft()
                print(f"Chance Card: {card}")
                if "Pay" in card:
                    amount = int(card.split("$")[1])
                    player.balance -= amount
                elif "Collect" in card:
                    amount = int(card.split("$")[1])
                    player.balance += amount
                elif "Move forward" in card:
                    steps = int(card.split("forward ")[1].split()[0])
                    player.position = (player.position + steps) % len(board)
                elif "Go to Start" in card:
                    player.position = 0
                move_history.append(f"{player.name} drew a chance card: '{card}'")
                chance_deck.append(card)  # Put card back at the end

            # For "Go" block or other non-property blocks
            else:
                move_history.append(f"{player.name} landed on {block.name}")

            print(f"{player.name} Balance: ${player.balance}")
            print("Move History (latest):", move_history[-1])
            print("Properties owned (sorted):", property_tree.in_order())

    # Determine winner based on balance
    winner = None
    highest_balance = -1
    for player in players:
        print(f"{player.name} final balance: ${player.balance}")
        if player.balance > highest_balance:
            highest_balance = player.balance
            winner = player

    print(f"\nThe winner is {winner.name} with a final balance of ${winner.balance}!")


if __name__ == "__main__":
    main()
