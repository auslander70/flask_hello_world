import functools

def twist(function):
  @functools.wraps(function)
  def wrapper(*args, **kwargs):
    print("Shep Schwab shopped at Scott's Schnapps shop")
  return wrapper