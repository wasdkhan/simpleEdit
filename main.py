import sys, re
f = open(sys.argv[1], 'r+')
f.seek(0)
text = f.readlines()
for i in range(len(text)):
  print str(i) + ' ' + text[i],
while True:
  command = raw_input('--> ')
  helpText = '''  'x' to exit
  'h' for help
  'R' to read full text
  'Operation;LineNumber;Content' to edit (args are seperated by semicolons) 
    'd' operation to delete line (needs Line#)
    'r' operation to read line (needs Line#)
    'w' operation to splice in line after line number(needs Line# and Content)
      ex) d:3, r:15, w:16:Hello World!'''
  if command=='x' or command == 'quit' or command == 'exit':
    f.close()
    sys.exit("editing complete")
  elif command=='h' or command=='help':
    print helpText
  elif command=='R':
    f.seek(0)
    text = f.readlines()
    for i in range(len(text)):
      print str(i) + ' ' + text[i],
  else:
    pars = re.search('(\w);(\d+);*(.*)',command)
    if pars:
      lineNum = int(pars.group(2))
      oper = pars.group(1)
      content = pars.group(3)
      f.seek(0)
      if oper == 'r': print text[lineNum],
      elif oper == 'd': 
        delLine = text.pop(lineNum)
        print 'del@' + str(lineNum) + ':' + delLine,
      elif oper == 'w': text.insert(lineNum+1, content)
      if oper != 'r':
        for i in range(len(text)): f.write(text[i])