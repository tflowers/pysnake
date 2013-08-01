#----------------------------------------------------------------------------
#THE BEER-WARE LICENSE" (Revision 42):
#<tdflowers@gmail.com> wrote this file. As long as you retain this notice you
#can do whatever you want with this stuff. If we meet some day, and you think
#this stuff is worth it, you can buy me a beer in return Tim Flowers
#----------------------------------------------------------------------------


import pysnake
from pysnake.models import Snake
from view import Direction
import random

class Board(object):
  
  def __init__(self, view):
    self.view = view
    self.height = view.height
    self.width = view.width
    self.snakes = {}
    self.food = []
    self.score = 0
    self.level = 1
    self.view.set_score(self.score)
    self.view.set_level(self.level)

  def add_snake(self):
    snake = Snake(self.height / 2, self.width / 2)
    self.snakes[snake] = snake.body 
    return snake

  def add_food(self):
    y = random.randint(1, self.height-1)
    x = random.randint(1, self.width-1)
    food = (y, x)
    self.food.append(food)
    self.view.addch(food, "0")
    return food

  def check_food(self, snake):
    if snake.head in self.food:
      self.food.remove(snake.head)
      self.add_score()
      for x in range(10):
        snake.grow()


  def move_snakes(self):
    for snake in self.snakes:
      tmp_snake = list(self.snakes[snake])
      self.check_food(snake)
      if not snake.move():
        return False
      if self.check_collisions(snake.head):
        return False
      self.erase(tmp_snake)
      self.draw(snake.body)
      del(tmp_snake)
      return True

  def draw(self, obj):
    self.view.draw(obj)

  def add_score(self):
    self.score += 1
    if self.score % 5 == 0:
      self.add_level()
    self.view.set_score(self.score)

  def add_level(self):
    self.level += 1
    self.view.set_level(self.level)

    
  def erase(self, obj):
    self.view.erase(obj)

  def check_collisions(self, point):
    y, x = point
    if y == 0 or y >= self.height:
      return True
    if x == 0 or x >= self.width:
      return True
    return False



class Game(object):

  def __init__(self):
    self.mainview = pysnake.View()
    self.view = self.mainview.curview
    self.ticks = 0

  def game_menu(self):
    self.mainview.menuwindow()
    self.view = self.mainview.curview

  def start_game(self):
    self.mainview.gamewindow()
    self.view = self.mainview.curview
    self.board = Board(self.view)

  def end_menu(self):
    self.mainview.gameoverwindow()

  def tick(self):
    self.ticks += 1
    if self.ticks % 50 == 0: 
      self.add_food()
    if not self.board.move_snakes():
      return False
    return True

  def add_snake(self):
    return self.board.add_snake()

  def add_food(self):
    self.board.add_food()

  def getch(self, blocking=False):
    return self.mainview.getch(blocking)


