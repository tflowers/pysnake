#----------------------------------------------------------------------------
#THE BEER-WARE LICENSE" (Revision 42):
#<tdflowers@gmail.com> wrote this file. As long as you retain this notice you
#can do whatever you want with this stuff. If we meet some day, and you think
#this stuff is worth it, you can buy me a beer in return Tim Flowers
#----------------------------------------------------------------------------


import curses


#TODO:  Write my own banner funcitons (IE dynamically generate banners given string)
def end_banner(window, color):
  height, width = window.getmaxyx()
  ban_ln1 = " #####     #    #     # #######         ####### #     # ####### ######"
  ban_ln2 = "#     #   # #   ##   ## #               #     # #     # #       #     #"
  ban_ln3 = "#        #   #  # # # # #               #     # #     # #       #     #"
  ban_ln4 = "#  #### #     # #  #  # #####           #     # #     # #####   ######"
  ban_ln5 = "#     # ####### #     # #               #     #  #   #  #       #   #"
  ban_ln6 = "#     # #     # #     # #               #     #   # #   #       #    #"
  ban_ln7 = " #####  #     # #     # #######         #######    #    ####### #     #"

  ypos = (height / 2) - 6
  xpos = (width - len(ban_ln1)) / 2

  window.addstr(ypos, xpos, ban_ln1, color)
  window.addstr(ypos + 1, xpos, ban_ln2, color)
  window.addstr(ypos + 2, xpos, ban_ln3, color)
  window.addstr(ypos + 3, xpos, ban_ln4, color)
  window.addstr(ypos + 4, xpos, ban_ln5, color)
  window.addstr(ypos + 5, xpos, ban_ln6, color)
  window.addstr(ypos + 6, xpos, ban_ln7, color)
  window.addstr(ypos + 10, xpos, "PRESS ANY KEY TO CONTINUE", color)
  window.refresh()






def snake_banner(window, color):
  height, width = window.getmaxyx()
    
  ban_ln1 = "  ####   #    #    ##    #    #  ######"
  ban_ln2 = " #       ##   #   #  #   #   #   #"
  ban_ln3 = "  ####   # #  #  #    #  ####    #####"
  ban_ln4 = "      #  #  # #  ######  #  #    #"
  ban_ln5 = " #    #  #   ##  #    #  #   #   #"
  ban_ln6 = "  ####   #    #  #    #  #    #  ######"

  ypos = (height / 2) - 6
  xpos = (width - len(ban_ln1)) / 2

  window.addstr(ypos, xpos, ban_ln1, color)
  window.addstr(ypos + 1, xpos, ban_ln2, color)
  window.addstr(ypos + 2, xpos, ban_ln3, color)
  window.addstr(ypos + 3, xpos, ban_ln4, color)
  window.addstr(ypos + 4, xpos, ban_ln5, color)
  window.addstr(ypos + 5, xpos, ban_ln6, color)
  window.addstr(ypos + 10, xpos, "PRESS ANY KEY TO CONTINUE", color)
  window.refresh()


class Colors(object):

  def __init__(self):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(5, curses.COLOR_RED,   curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLUE,  curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)

    self.BLACK_WHITE = curses.color_pair(1)
    self.BLACK_BLACK = curses.color_pair(2)
    self.BLACK_RED   = curses.color_pair(3)
    self.BLACK_BLUE  = curses.color_pair(4)
    self.RED_BLACK   = curses.color_pair(5)
    self.BLUE_BLACK  = curses.color_pair(6)
    self.GREEN_BLACK = curses.color_pair(7)
    self.GREEN_BLACK = curses.color_pair(7)


class Direction(object):
  UP    = (-1, 0)
  DOWN  = (1,  0)
  LEFT  = (0, -1)
  RIGHT = (0,  1)




class GameWindow(object):

  def __init__(self, screen):
    self.screen = screen
    self.colors = Colors()
    self.scr_height, self.scr_width = self.screen.getmaxyx()


  def init_board_win(self):
    height = self.scr_height - 4
    width = self.scr_width - 4
    ypos = 2
    xpos = 2
    self.board_window = self.game_window.derwin(height, width, ypos, xpos)
    self.board_window.nodelay(True)
    self.board_window.keypad(1)
    self.board_window.border()
    self.board_window.refresh()

  def init_title_win(self):
    height = 2
    width = self.scr_width - 4
    ypos = 0
    xpos = 2
    self.title_window = self.game_window.derwin(height, width, ypos, xpos)
    self.title_window.addstr(1, (width - 2) / 2, "SNAKE", self.colors.GREEN_BLACK)
    self.title_window.refresh()

  def init_stats_win(self):
    height = 2
    width = 12
    ypos = 0
    titlewin_height, titlewin_width = self.title_window.getmaxyx()
    xpos = titlewin_width - width
    self.stats_window = self.title_window.derwin(height, width, ypos, xpos)
    self.stats_window.addstr(0,0, "Score: ", self.colors.RED_BLACK)
    self.stats_window.addstr(1,0, "Level: ", self.colors.RED_BLACK)
    self.stats_window.refresh()

  def render(self):
    self.game_window = self.screen.subwin(0,0)
    self.game_window.clear()
    self.init_title_win()
    self.init_stats_win()
    self.init_board_win()
    self.height, self.width = self.board_window.getmaxyx()

  def getch(self):
    return self.board_window.getch()

  def draw(self, obj):
    for point in obj:
      self.plot(point)
    self.board_window.refresh()

  def erase(self, obj):
    for point in obj:
      self.unplot(point)
    self.board_window.refresh()

  def plot(self, point):
    y, x = point
    self.board_window.addch(y, x, ' ',  self.colors.BLACK_WHITE)
    
  def unplot(self, point):
    y, x = point
    self.board_window.addch(y, x, ' ',  self.colors.BLACK_BLACK)

  def addch(self, point, ch):
    y, x = point
    self.board_window.addch(y, x, ch)

  def set_score(self, score):
    self.stats_window.addstr(0, 8, str(score), curses.A_BOLD)
    self.stats_window.refresh()

  def set_level(self, level):
    self.stats_window.addstr(1, 8, str(level), curses.A_BOLD)
    self.stats_window.refresh()


class MenuWindow(object):

  def __init__(self, screen):
    self.screen = screen
    self.colors = Colors()
    self.scr_height, self.scr_width = self.screen.getmaxyx()

  def render(self):
    self.main_menu_window = self.screen.subwin(0,0)
    self.main_menu_window.clear()
    snake_banner(self.main_menu_window, self.colors.BLUE_BLACK)
    self.main_menu_window.refresh()

class GameOverWindow(object):

  def __init__(self, screen):
    self.screen = screen
    self.colors = Colors()
    self.scr_height, self.scr_width = self.screen.getmaxyx()

  def render(self):
    self.end_window = self.screen.subwin(0,0)
    self.end_window.clear()
    end_banner(self.end_window, self.colors.BLUE_BLACK)
    self.end_window.refresh()


class View(object):

  def __init__(self):
    self.screen = curses.initscr()
    self.screen.nodelay(True)
    self.screen.keypad(1)
    self.curview = None
    curses.curs_set(0)

  def __del__(self):
    del(self.curview)
    curses.endwin()

  def gamewindow(self):
    self.curview = GameWindow(self.screen)
    self.curview.render()

  def gameoverwindow(self):
    self.curview = GameOverWindow(self.screen)
    self.curview.render()

  def menuwindow(self):
    self.mw = MenuWindow(self.screen)
    self.mw.render()

  def getch(self, blocking=False):
    if blocking:
      self.screen.nodelay(False)
    else: 
      self.screen.nodelay(True)
      
      
    c = self.screen.getch()
    if c == curses.KEY_UP:
      return Direction.UP
    if c == curses.KEY_DOWN:
      return Direction.DOWN
    if c == curses.KEY_LEFT:
      return Direction.LEFT
    if c == curses.KEY_RIGHT:
      return Direction.RIGHT
    else: 
      return c
    
  def draw(self, obj):
    pass

  def erase(self, obj):
    pass

  def plot(self, point):
    pass

  def unplot(self, point):
    pass

  def render_score(self, score):
    pass

  def render_level(self, level):
    pass

