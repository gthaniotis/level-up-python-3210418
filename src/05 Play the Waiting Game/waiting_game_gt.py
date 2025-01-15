from time import time
from random import randint

def waiting_game():
    target = randint(2, 4)
    print(f"Your target time is {target} seconds")
    input(" --- Press Enter to Begin --- ")
    start_time = time()
    input(f"Press Enter again after {target} seconds")
    elapsed_time = time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")
    if elapsed_time == target:
        print("Right on the money!")
    elif elapsed_time < target:
        print(f"{target - elapsed_time:.3f} seconds too soon")
    else:
        print(f"{elapsed_time - target:.3f} seconds too late")

waiting_game()