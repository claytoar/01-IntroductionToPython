"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Abi Clayton.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(20)

susan = rg.SimpleTurtle('turtle')
susan.pen = rg.Pen('green', 10)
susan.speed = 15

size = 50

for k in range(10):
    susan.draw_circle(size)
    susan.right(36)

trinidad = rg.SimpleTurtle('arrow')
trinidad.pen = rg.Pen('blue', 5)
trinidad.speed = 10

size = 100

trinidad.pen_up()
trinidad.go_to(rg.Point(50, -250))
trinidad.pen_down()

for k in range(5):
    trinidad.draw_regular_polygon(5,size)
    trinidad.pen_up()
    trinidad.left(45)
    trinidad.forward(15)
    trinidad.right(45)
    trinidad.pen_down()
    size = size - 20

window.close_on_mouse_click()