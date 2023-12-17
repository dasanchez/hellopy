Code using *args and **kwargs
```
def func(*args, **kwargs):
  m = ''
  s = func(*args, **kwargs)
  for i, char in enumerate(s):
    c = 'x' if start <= i < end else char
    m += c
  return m
```

Decorator template that uses *args and **kwargs
```
from functools import wraps

def decorator(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    # Do something before
    result = func(*args, **kwargs)
    # Do something after
    return result
  return wrapper

@decorator
def func():
  pass
```