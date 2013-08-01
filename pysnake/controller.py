#----------------------------------------------------------------------------
#THE BEER-WARE LICENSE" (Revision 42):
#<tdflowers@gmail.com> wrote this file. As long as you retain this notice you
#can do whatever you want with this stuff. If we meet some day, and you think
#this stuff is worth it, you can buy me a beer in return Tim Flowers
#----------------------------------------------------------------------------


from pysnake.view import Direction
import sys
import pysnake
import traceback
from time import sleep

class PySnake(object):
  
  def __init__(self):
    self.game = pysnake.Game()
    
  def user_input(self):
    c = self.view.getch()
    if c == ord('q'):
      return False
    return True

  def main_menu(self):
    self.game.game_menu()
    self.game.getch(True)
    self.gameloop()
        
  def end_menu(self):
    self.game.end_menu()
    c = self.game.getch(True)
    if c == ord('q'):
      sys.exit()
    else:
      self.gameloop()
      
      
    self.gameloop()

  def gameloop(self):
    self.game.start_game()
    snake = self.game.add_snake()
    while True:
      if not self.game.tick():
        break
      c = self.game.getch()
      if c == ord('q'):
        break
      if c == Direction.UP:
        snake.direction = c
      if c == Direction.DOWN:
        snake.direction = c
      if c == Direction.LEFT:
        snake.direction = c
      if c == Direction.RIGHT:
        snake.direction = c
      sleep(.1)

    self.end_menu()
