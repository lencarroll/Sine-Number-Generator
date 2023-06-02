# Sine-Number-Generator

This project continues from other random generator projects I have explored before, such as https://github.com/lencarroll/Random-Number-Generator.

In this project we generate a number baed on how long it takes you to press the 'Enter' key. The time taken (which should be less than 10 seconds) is then used in the equation:

$$sin(\frac{1000t\pi}{10})$$

The reason I used this equation instead of something much simpler (such as $n = \frac{t}{0}$), is because the latter equation would make it very easy to bias the number generation (if you want a value less than 0.2, just press the keyboard before 2 seconds) but with this equation, it is quite difficult to bias it. For example:
If the time take was 2.111111 seconds, the number generated would be about 0.34, but using 2.112111 it would give you a value of 0.62. So being off by merely 10 milliseconds can cause such a massive change. 

Now I caution to call this a random number generator because it is theoretically possible (just difficult) to bias the number generation, if you have a really good setup to ensure that the keyboard is always pressed at the exact same time. I experimented with this using the software MacroRecorder, and although rounded down to one decimal I could get the numbers the same, beyond 1 decimal point they were always different.

The function has only one (optional) argument and that is ```verbose```. By default it is set to 1, which means that before the timer starts you are informed. If you choose ```verbose = 0```, you won't be informed which can make things even more unpredictable in a sense.
