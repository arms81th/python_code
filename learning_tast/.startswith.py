name=input("Your name: ")

if name.startswith(("mister","mr.")):
  print("Man")
elif name.startswith(("missis","ms.")):
  print("Woman")
else:
  print("not specified")
