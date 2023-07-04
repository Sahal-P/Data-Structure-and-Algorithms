
def encodedecode(arr):
  encoded =""
  for i in arr:
    lent = len(i)
    encoded+=(f"{lent}#{i}")
  decoded =[]
  num=""
  for t,j in enumerate(encoded):
    if j.isdigit():
      num+=j
    if j == "#":
      word=""
      for k in range(1,int(num)+1):
        word+=encoded[t+k]
      decoded.append(word)
      word=""
      num=""
      
  print(decoded)
    