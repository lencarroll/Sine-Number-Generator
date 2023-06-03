import time
import msvcrt
import numpy as np
import secrets

# For this function you are informed (optional) when the timer starts. You have 10 seconds to press the 'Enter' key. If you do it within the time range of [0.0001, 10), your time is accepted.
# That time is then used in the equation |sin((t+-noise)*pi*10)|. Whatever the value is, that's the random number.
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

    # Noise is generated using the cryptographically secure secrets method. Even if this eventually becomes biased, the average user will struggle to bias the rest of the work.
    noise = secrets.randbits(53) / (2 ** 53)
    noise_sign = round(secrets.randbits(53) / (2 ** 53))

    if noise_sign == 0: 
        random_number = (duration+noise)/10
    elif noise_sign == 1:
        random_number = np.abs((duration - noise)/10)
    if duration/time < 0.00001:
        print("There is an issue with your key press, please try again!")
        return random(verbose)
    elif duration/time >= 1 or random_number >= 1:
        print("You took too long, you will need to try again!")
        return random(verbose)
    else:
        return np.abs(np.sin(random_number*np.pi*100))
