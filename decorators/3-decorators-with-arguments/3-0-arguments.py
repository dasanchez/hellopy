def test_arguments(*args, **kwargs):
  print(args)
  print(kwargs)

test_arguments(1, 2, 3, a = 4, b = 5, c = 6)