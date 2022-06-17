import sys
import math

args = sys.argv

# print(args[1])

def is_num(s):
  try:
      float(s)
  except ValueError:
      return False
  else:
      return True

if len(args) <= 1:
  print("入力値がありません")
elif len(args) > 1 and not is_num(args[1]): 
  print("数値を入力してください")
elif is_num(args[1]): 
  r = float(args[1])
  area = math.pi * r * r

  print('{0}'.format(area))


