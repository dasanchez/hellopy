def pfib(a, *args):
  print(a)
  print(args)

pfib(1)
pfib(1, 1, 2, 3)

def pfib(a, **kwargs):
  print(a)
  print(kwargs)

pfib(1)
pfib(1, se=1, th=2, fo=3, fi=5)

def pfib(*args, **kwargs):
  print(args)
  print(kwargs)

pfib()
pfib(1)
pfib(1, 1, 2, 3)
pfib(fi=1, se=1, th=2, fo=3)
pfib(1, 1, 2, fo=3)

def wrapper(*args, **kwargs):
  print(*args)
  print('Leaving wrapper')
  pfib(*args, **kwargs)

print('Calling wrapper function:')
wrapper(1, 1, 2, fo=3)