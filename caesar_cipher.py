alfabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(teksts, rotacija):  #Definē "Encryption" funkciju.
  result = ""
  for c in teksts:  #Cikls, kas tiek izmantots, lai pārveidotu burtus.
    if (alfabets.find(c) == -1):  #Ja atrod c, tad tiek atņemts burts.
      result += c
    else:  #Ja a neatrod c, tad tiek pievienots viens burts.
      result += (alfabets[(alfabets.find(c) + rotacija) % len(alfabets)])
  return result




def decrypt(teksts, rotacija):  #Definē burtu d.
  result = ""
  for c in teksts:  #Cikls, kas tiek izmantots, lai pārveidotu burtus.
    if (alfabets.find(c) == -1):  #Ja a atrod c, tad tiek atņemts viens burts.
      result += c
    else:  #Ja a neatrod c, tad tiek atgriezta iepriekšējā pozīcija.
      result += (alfabets[(alfabets.find(c) - rotacija) % len(alfabets)])
  return result





w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))





if mode == 1:  #Ja ir izvēlēts 1. režīms, tad tiek printēts
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encrypt(text, rotation))
elif mode == 2:  #Ja ir izvēlēts 2. režīms, tad tiek printēta atbilde, ja nē, tad tiek izvēlēts nākošais režīms
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decrypt(text, rotation))
elif mode == 3:  #Ja izvēlēts 3. režīms, tad printēt.
  text = input("Enter the text: ")
  print("Bruteforcing...")
  for n in range(26):
    print(str(n+1) + ": " + decrypt(text, n))
    
 
  
