#import meshtastic
from enum import Enum
from random import randrange
from rich import inspect
from rich.console import Console
from rich.pretty import Pretty
from rich.table import Table

# Pseudocode: 
# If Server:
    # Get list of nodes
    # Show user list of nodes
    # Ask user which node to invite
    # Send invite
    # Wait for invite accepted
    # Goto board setup

# If Client:
    # Sit and wait for DM with right format
    # Prompt to accept/deny
    # Wait for accept
    # Goto board setup

# Assuming 10x10 board

# Board Setup:
    # Display board
    # Display preview of ship
    # Request position&rotation (origin top left of ship)
        # 2, 3, Y
        # 5, 2, N
    # Repeat until board filled
    # Send "ready" message

# Define data structures
class Board_Space(Enum):
    EMPTY = 0,
    SHIP = 1,
    HIT = 2,
    MISS = 3

BOARD_SIZE = 10

# Connect to Meshtastic Node
# interface = meshtastic.serial_interface.SerialInterface()
console = Console()

def render_board_space(space):
    match space:
        case Board_Space.EMPTY:
            return "-"
        case Board_Space.SHIP:
            return "D"
        case Board_Space.HIT:
            return "X"
        case Board_Space.MISS:
            return "o"
        case _:
            return "?"
        
def render_board(board):
    table = Table(show_lines=True, show_footer=True)
    table.add_column("") # For left side coords
    for i in range(BOARD_SIZE):
        table.add_column(header=str(i), footer=str(i))
    table.add_column("") # For right side coords
    
    for i in range(BOARD_SIZE):
        rendered_row = [render_board_space(space) for space in board[i]]
        table.add_row(*([str(i)] + rendered_row) + [str(i)])
    
    return table


# Construct an NxN grid of board_space enums
board = [[Board_Space.EMPTY for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

console.print(render_board(board))

