import time
import msvcrt
import numpy as np

# For this function you are informed (optional) when the timer starts. You have 10 seconds to press the 'Enter' key. If you do it within the time range of [0.01, 10), your time is accepted.
# That time is then used in the equation |sin(t*pi*100)|. Whatever the value is, that's the random number.
# If you are outside the time range, the number generation will fail and you have to start over.
def random(verbose=None):
    if verbose == None:
        verbose = 1
    start_time = time.time()
    if verbose == 1:
        print("Press the 'Enter' key to register the time! If you take longer than 10 seconds to type, you will have to retry.")
    msvcrt.getch()
    end_time = time.time()
    duration = end_time - start_time
    
    random_number = duration/10
    if random_number < 0.001:
        print("There is an issue with your key press, please try again!")
    elif random_number >= 1:
        print("You took too long, you will need to try again!")
    else:
        return np.abs(np.sin(random_number*np.pi*100))
