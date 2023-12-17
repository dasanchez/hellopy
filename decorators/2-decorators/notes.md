* A decorator is a callable that takes another function as an argument, extending the behaviour of that function without explicitly modifying that function.
* Decorators can access and modify input arguments and return values.

Decorator template:
```
def my_decorator_func()
  def wrapper():
    # Do something here
    result = func()
    # Do something after
    return result
  return wrapper

@my_decorator
def func():
  pass
```