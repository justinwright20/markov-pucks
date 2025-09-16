import random
from PIL import Image



class MarkovPuckPicker:
    def __init__(self, transition_matrix):
        # Store transition matrix
        self.transition_matrix = transition_matrix
         # Keep a list of all possible puck states
        self.pucks = list(transition_matrix.keys())

    def generate_sequence(self, currentPuck="choice1", length=10):
         # Generate a sequence of puck choices using the transition matrix probabilities
        return random.choices(
            self.pucks,
            weights=[self.transition_matrix[currentPuck][next_puck] for next_puck in self.pucks],
            k=length
        )

    
def overlay_logo_on_puck(puck_file, logo_file, scale=0.45):
    # Convert both the puck image and logo image into an RGBA image
    puck = Image.open(puck_file).convert("RGBA")
    logo = Image.open(logo_file).convert("RGBA")
    
    # Scale the logo so that it only is 45% of the puck
    target = int(puck.width * scale)
   
    # Pillow method that makes the logo fit within the desired width and height
    logo.thumbnail((target, target))
    
    # Center logo
    x = (puck.width - logo.width) // 2
    y = (puck.height - logo.height) // 2

    # Put the logo on top of the puck
    puck.alpha_composite(logo, (x, y))

    return puck
    
def combine_row(images, gap=10, bg=(255, 255, 255, 0)):
    # Calculating the total width of image by adding image widths and gap spacing
    combined_image_widths = sum(img.width for img in images)
    total_gaps = gap * (len(images) - 1)
    w = combined_image_widths + total_gaps

    # Using the height of the tallest image to set as image height
    h = max(img.height for img in images)

    # Creates a new "blank canvas"
    three_pucks = Image.new("RGBA", (w, h), bg)

    # Place images next to each other
    for idx, img in enumerate(images):
        x_axis_placement = idx * (img.width + gap)
        three_pucks.alpha_composite(img, (x_axis_placement, 0))

    return three_pucks

def paste_row_on_rink(rink_file, combined_pucks, out_file="rinkPic.png"):
    # Convert rink image into RGBA
    rink = Image.open(rink_file).convert("RGBA")
    row  = combined_pucks.copy()

    # Center the row on top of the rink
    x = (rink.width - row.width) // 2
    y = (rink.height - row.height) // 2

    # Put the row of pucks on top of the rink background
    rink.alpha_composite(row, (x, y))

    rink.save(out_file)
    rink.show()


def main():
    # Transition matrix describing probabilities 
    puckMaker = MarkovPuckPicker({
        "choice1":    {"choice1": 0.2, "choice2": 0.4, "choice3": 0.1, "choice4": 0.15, "choice5": 0.15},
        "choice2":    {"choice1": 0.1, "choice2": 0.25, "choice3": 0.3, "choice4": 0.15, "choice5": 0.2},
        "choice3":    {"choice1": 0.1, "choice2": 0.1, "choice3": 0.5, "choice4": 0.15, "choice5": 0.15},
        "choice4":    {"choice1": 0.3, "choice2": 0.3, "choice3": 0.1, "choice4": 0.15, "choice5": 0.15},
        "choice5":    {"choice1": 0.4, "choice2": 0.1, "choice3": 0.1, "choice4": 0.2, "choice5": 0.2},
    })

    # Generate a set of 3 pucks
    puck_sequence = puckMaker.generate_sequence(currentPuck="choice1", length=3)

    # Dictionary of the 5 different logos we can use
    logos = {
        "choice1": "assets/choice1.png",
        "choice2": "assets/choice2.png",
        "choice3": "assets/choice3.png",
        "choice4": "assets/choice4.png",
        "choice5": "assets/choice5.png",
    }

    # Blank puck picture 
    puck_file = "assets/blackPuck.png"

    # Build the set of 3 pucks with logos
    pucks = []
    for choice in puck_sequence:
        puck = overlay_logo_on_puck(puck_file, logos[choice])
        pucks.append(puck)

     # Combine the 3 pucks into one set
    row_output = combine_row(pucks, gap=20)

    # Put the set over the rink background
    paste_row_on_rink("assets/rinkPic.png", row_output, out_file=f"examples/pucks_on_rink{random.randint(1000,9999)}.png")

if __name__ == "__main__":
    main()