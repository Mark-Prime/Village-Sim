import argparse
import random

from utility.framerate import current_time, pause_on_frame
from utility.console import clear_console
from classes.village import Village
from classes.villager import Villager

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Name of the village")
parser.add_argument("-p", "--population",
                    help="Change starting population", type=int)
args = parser.parse_args()

name = args.name or "Village"
population = args.population or 100
    
def main(name, population):
    village = Village(name, population)
    
    # Show initial state
    clear_console()
    print(village)
    
    # Allow people to read the innitial state
    pause_on_frame(current_time())
    
    while village.is_alive():
        # Lock in the time the loop starts
        # This is later used to make sure it doesn't run too fast
        # Giving people time to read the output.
        start = current_time()
        
        clear_console()
        
        village.advance_month()
        
        # Show current state
        print(village)
        
        # Pauses the loop so people can read the output
        
        pause_on_frame(start)
        
    print(f'The village has been destroyed on date {village.date} with {Villager.TOTAL} total villagers.')
    
main(name, population)