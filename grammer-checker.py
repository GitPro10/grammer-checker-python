from gingerit.gingerit import GingerIt
parser = GingerIt()

while True:
  
  txt = str(input("\nType: "))
  parsedObj = parser.parse(txt)
 
  if parsedObj['result'] == txt:
    print("\nYour entered sentence is correct!\n(not 100% sure)")
  else:
    corrections = []
    for correction in parsedObj["corrections"]:
      if str(correction['definition']) == "None":
        pass
      else:
        
        correctWord = str(correction['correct'])
        definitionForWord = correction['definition'].title()
        
        definition = f'Definition for, "{correctWord}" is: {definitionForWord}'
        corrections.append(definition)
  
    print("\nYour entered text is wrong!")
    print("It should be like this...")
    print("\n> " + parsedObj['result'])
  
    if not corrections:
      pass
    else:
      print("\nDefinition(s):\n")
      joinedCorrentions = "\n".join(corrections)
      print(joinedCorrentions)
  exitReq = str(input("\nDo you want to exit?\n> "))
  if exitReq == "y" or exitReq == "yes":
    print("Ok!")
    break
  else:
    pass