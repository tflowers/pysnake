
#----------------------------------------------------------------------------
#THE BEER-WARE LICENSE" (Revision 42):
#<tdflowers@gmail.com> wrote this file. As long as you retain this notice you
#can do whatever you want with this stuff. If we meet some day, and you think
#this stuff is worth it, you can buy me a beer in return Tim Flowers
#----------------------------------------------------------------------------


from pysnake.view import Direction

class Snake(object):

  def __init__(self, starty, startx):
    self.body = [(starty, startx - i) for i in range(4)]
    self.head = self.body[0]
    self.direction = Direction.RIGHT

  def move(self):
    new_head = tuple(sum(x) for x in zip(self.head, self.direction))
    if new_head in self.body:
      return False
    self.head = new_head
    self.body.insert(0, self.head)
    self.body.pop()
    return True

  def grow(self):
    self.body.append(self.body[-1])

