def decoded_message(message, shift) :

  new_message = ""  

  for n in range(0, len(message)):
    if shift >= 0:
      new_message_ord = ord(message[n]) - shift
      if int(new_message_ord) < 97:
        new_message_ord += 26
        new_message_chr = chr(new_message_ord)
        new_message += new_message_chr  
      else:
        new_message_chr = chr(new_message_ord)
        new_message += new_message_chr  
    else:
      new_message_ord = ord(message[n]) - shift
      if int(new_message_ord) > 122:
        new_message_ord -= 26
        new_message_chr = chr(new_message_ord)
        new_message += new_message_chr  
      else:
        new_message_chr = chr(new_message_ord)
        new_message += new_message_chr  

  print(new_message)

while True:
  message = input("Enter the message: ").lower()

  shift = int(input("Enter PIN: "))

  decoded_message(message, shift)

  choice = input("Want to decode more messages (YES or NO) : ").lower()

  if choice == "no":
    exit()
    
