#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)
print(r)
print(dir(r))
 try:
     print(Rectangle:" {} - {}".format(r.width), r.height))
 except Exception as e:
     pribt ("[{}] {}".format(e.__class.__name__. e))
     try:
         r2 = Rectangle(4, True)
     except Exception as e :
         print("[{}] {} ". formart(e.__class__.__name__. e))
