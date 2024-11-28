
"""
  Removes duplicates.
"""

def include(arr, item):
  for x in arr:
    if x == item and type(item) == type(x):
      return True
  return False

def unique(arr):
  result = []
  for x in arr:
    if not include(result, x):
      result.append(x)
  return result

if __name__ == '__main__':
  print(unique([False, 1, True, 0, 1, 2, None, 0, 1, 3, 'a']))