def define_constants():
    turtle_colors = ["white", "gainsboro", "silver", "darkgray", "gray", "dimgray", "black whitesmoke",
                    "lightgray", "violet", "orchid", "magenta", "darkviolet", "darkmagenta", "ghostwhite",
                    "thistle", "plum", "mediumorchid", "darkorchid", "blueviolet", "purple", "aliceblue",
                    "lavender", "lightsteelblue", "mediumpurple", "mediumslateblue", "rebeccapurple",
                    "indigo", "lightcyan", "powderblue", "lightskyblue", "cornflowerblue", "slategray",
                    "darkslateblue", "blue", "azure", "paleturquoise", "skyblue", "deepskyblue",
                    "lightslategray", "slateblue", "mediumblue", "mintcream", "aquamarine", "lightblue",
                    "darkturquoise", "dodgerblue", "royalblue", "darkblue", "honeydew", "palegreen",
                    "lightgreen", "cyan", "cadetblue", "steelblue", "navy", "lightgoldenrodyellow", "yellow",
                    "lawngreen", "turquoise", "mediumturquoise", "darkcyan", "midnightblue", "lightyellow",
                    "palegoldenrod", "chartreuse", "mediumaquamarine", "lime", "teal", "darkslategray", "beige",
                    "wheat", "greenyellow", "mediumspringgreen", "limegreen", "lightseagreen", "green", "ivory",
                    "moccasin", "khaki", "springgreen", "darkseagreen", "mediumseagreen", "darkgreen", "lemonchiffon",
                    "papayawhip", "gold", "yellowgreen", "goldenrod", "seagreen", "forestgreen", "cornsilk",
                    "blanchedalmond", "tan", "darkkhaki", "darkorange", "olivedrab", "darkolivegreen", "floralwhite",
                    "navajowhite", "burlywood", "orange", "peru", "darkgoldenrod", "olive", "oldlace", "antiquewhite",
                    "sandybrown", "coral", "chocolate", "saddlebrown", "red", "linen", "bisque", "lightsalmon", "salmon",
                    "orangered", "sienna", "darkred", "seashell", "peachpuff", "darksalmon", "lightcoral", "tomato", "crimson",
                    "maroon", "snow", "mistyrose", "lightpink", "rosybrown", "indianred", "deeppink", "firebrick transparent",
                    "lavenderblush", "pink", "hotpink", "palevioletred", "mediumvioletred", "brown"]

    #Define variable to eliminate "magic numbers" & defaults
    CIRCLE_DEGREES = 360
    DEFAULT_PEN_COLOR = 'red'   #'lawngreen'
    DEFAULT_INITIAL_SPEED = 13
    DEFAULT_RADIUS = 300
    DEFAULT_DRAW_PERCENT = 100
    DEFAULT_LINE_LENGTH = 100

    sample_shape = {
        'x': 200,
        'y': 276,
        'radius': 246,
        'corners': 35,
        'percent': DEFAULT_DRAW_PERCENT,
        'turn_right': 0
    }


def init_turtle(turtle_param, initial_speed=10, pen_color='red'):
  # _______________________________________________________________
  ''' Shorter syntax for initializing the turtle the way I want it each time '''
  module_myTurtle = turtle_param
  module_myTurtle.initializeTurtle(initial_speed)
  #print(pen_color)
  module_myTurtle.color(pen_color)

def move_my_turtle(x,y):
  # _____________________________
  ''' Move the turtle without drawing '''
  myTurtle.penup()
  myTurtle.goto(x, y)
  myTurtle.pendown()
  ##myTurtle.forward(100)

#help(move_my_turtle)

def draw_my_shape(corners):
# __________________________________________
  ''' Draw a shape based on the number of corners '''
  for counter in range(corners):
      myTurtle.forward(100)
      myTurtle.right(360 / corners)

#help(draw_my_shape)

def draw_my_shape_radius(corners, radius = 300):
# __________________________________________
  ''' Draw a shape based on the number of corners and the radius '''
  circumference = 2 * math.pi * radius
  angle = 360 / corners
  line_length = circumference / corners
  for counter in range(corners):
      myTurtle.forward(line_length)
      myTurtle.right(angle)
# __________________________________________

def draw_my_shape_radius_partial(corners, radius = 300, percent=100):
# __________________________________________________________________
  ''' Draw a shape based on the number of corners and the radius
          corners is the number of corners to have in the same
          radius = the radius of the enclosing circle -- sets the length of the
                   lines
          percent is a whole number between 1 and 100 indicating how much
                  of the circle to draw

          Pre-condidtion: The turtle ins in the correct starting position
                          and is pointing in the correct direction
          Post-condiction: The turtle has painted the shape and is in thes
                           same position pointing the same way.'''

  circumference = 2 * math.pi * radius
  angle = 360 / corners
  line_length = circumference / corners
  lines_to_draw = corners * (percent / 100)
  for counter in range(corners):
      myTurtle.forward(line_length)
      myTurtle.right(angle)
      if counter > lines_to_draw:
        myTurtle.penup()

  myTurtle.pendown()
# _____________________________________________________________________


def draw_shape_dict(shape_definition):
  #__________________________________________
  ''' Draw a shape based on a dictionary of values

      shape_definition = {
        'x': ______,
        'y': ______,
        'radius': ______,
        'corners': ______,
        'percent': ______,
        'turn_right': ______
      } '''

  move_my_turtle(shape_definition['x'], shape_definition['y'])
  turn_right = shape_definition.get('turn_right', 0)
  if turn_right > 0:
    #print(f'Turning right {turn_right} degrees')
    myTurtle.right(turn_right)
  draw_my_shape_radius_partial(shape_definition['corners'], shape_definition['radius'],shape_definition['percent'])

#help(draw_my_shape_dict)


define_constants()
printn('Module tes_colabturtle_shapes has been loaded')