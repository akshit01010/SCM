try:
  if '1' != 1:
        raise ValueError("someError")
  else:
        print("someError has not occurred")
except ValueError:
    print("someError has occurred")
