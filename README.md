# markov-pucks

System Title: Markov 3 Puck Picker

Project Description:

This project uses a Markov chain model to generate sequences of 3 hockey pucks with different logos, place those logos on top of a blank puck image, and then place the set of generated pucks on top of a hockey rink background. This idea behind this project was to use a computer to come up with a set up pucks to use in a hypothetical hockey game, where one puck is used per hockey period.

System Documentation:

The program can be broken down into 5 basic parts:
1. Use a Markov model.
    Define a transition matrix with probabilities that are used to select which logos will be placed on the pucks.
2. Generate a sequence of 3 pucks.
    Using the probabilities from the Markov model, a sequence of 3 puck logos will be selected.
3. Placing logos on the pucks.
    Each selected logo is resized and placed on the center of the puck.
4. Generated pucks are placed side by side.
    The three pucks that are created are put together 3 in a row.
5. Place set of pucks over rink background
    The set of pucks us placed on top of a picture of the Bowdoin rink.


How to Set Up and Run The Code:

1. You need the Python3 programming language
2. You have to install the Pillow library ----> pip install pillow
3. Once you clone the repository, your repository will include an "assets" folder where all the logos and pictures are stored, an "examples" folder where the finished product will be saved, and the HockeyPucks.py file where the code can be executed. 
4. To run the program, type into the terminal ----> python3 HockeyPucks.py.


Reflection:

This system is personally meaningful because collecting hockey pucks with different logos was always something you looked forward to when going to different tournaments as a kid. Even now, I still have a collection of pucks in my bedroom of all various sorts, with pucks with dates that go back as far as the late 2000s. Just off the top of my head, I can remember the specific tournament pucks, organizations, 2010 Vancouver olympics, as well as pucks from professional games that I've been able to collect over the years. I think its also a cool piece of being in a home guy and being able to play with pucks with your logos and designs on them. 

This project genuinely challenged me as a programmer because I had to quickly learn how to navigate the Pillow library, which isn't something I have ever previously worked with. I definitely pushed myself outside of my comfort zone becuase not only was I using a new library, but I had never previously done any sort of image generation or image compiling before. This is an important challenge for me because it's my first real glimpse into being able to realize what capailities computers have and the true ability to be able to really do whatever I want (that I'm capable of). Next steps for me would be to become more comfortable with Pillow. I think another interesting element I could experiment with would be also adding a markov model that determines what background would be used. Maybe I could even create a link between which backgrounds show up and their effect on which pucks get selected for the game! Aside from this project, next steps I would want to take would be to learn about what other libraries are out there that you can be creative with and to start working with and becoming more familiar with them. 

I think my system is creative because it is essentially choosing from a bunch of objects and generating a specific set. While the creativity doesn't come from new logos or new art work that is being put on the pucks, it comes from the the familiar logos being combined in unpredictable ways. I believe that this structured randomness is creativity.


Sources:

1. https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
2. https://www.geeksforgeeks.org/python/python-pillow-a-fork-of-pil/
3. https://realpython.com/image-processing-with-the-python-pillow-library/


