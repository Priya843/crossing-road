from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#inhertance class
class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
   # for turtle to start from -ve y axis and turning it to north
    self.go_to_start()
    self.setheading(90)
    
  def go_up(self):
    self.forward(MOVE_DISTANCE)
    
  #if player reaches the other end let it go back to the start 
  def go_to_start(self):
    self.goto(STARTING_POSITION)

    
    #win if player reacher other side 
  def is_at_finish_line(self):
      if self.ycor()>FINISH_LINE_Y:
        return True
      else:
        return False
        
    
    
