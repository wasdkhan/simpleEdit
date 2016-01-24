import sys, re  #sys for args,exit and re for regex
f = open(sys.argv[1], 'r+') #open in read and write
f.seek(0) #go to beginning
text = f.readlines()
for i in range(len(text)):
  print str(i) + ' ' + text[i], #print with line numbers
while True: #keep asking for input until exit
  command = raw_input('--> ') 
  helpText = '''  'x' to exit
  'h' for help
  'ra' to read all text
  'Operation;LineNumber;Content' to edit (args are seperated by semicolons) 
    'd' operation to delete line (needs Line#)
    'r' operation to read line (needs Line#)
    'w' operation to splice in line after line number(needs Line# and Content)
      ex) d:3, r:15, w:16:Hello World!'''
  if command=='x' or command == 'quit' or command == 'exit':
    f.close() #leaves file open until exit
    sys.exit("editing complete")
  elif command=='h' or command=='help':
    print helpText
  elif command=='ra':
    f.seek(0)
    text = f.readlines()  #go to beginning and read again 
    for i in range(len(text)):
      print str(i) + ' ' + text[i],
  else:
    pars = re.search(r'(\w);(\d+);?(.*)',command) #search for raw string of one letter,one or more digit,0 or 1 semicolon, 0 or more non-newline characters
    if pars:  #if command is proper (pars!=None/False)
      lineNum = int(pars.group(2))  #line no. to edit
      oper = pars.group(1)  #operation to do
      content = pars.group(3) #what to write if there is content
      f.seek(0)
      if oper == 'r': print text[lineNum], #read line ',' is added for no \n 
      elif oper == 'd': 
        delLine = text.pop(lineNum) #delete line
        print 'del@' + str(lineNum) + ':' + delLine,  #show what is deleted
      elif oper == 'w': text.insert(lineNum+1, content+'\n')  #insert content on next line with \n
      f.seek(0)
      if oper != 'r': #reconstructing file based on changes during w or d
        for i in range(len(text)): f.write(text[i]) #write to file all of new elements
        f.truncate()  #truncate file (deletes rest)