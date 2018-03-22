mac= (input("Digite seu mac: "))
num= mac.isdigit()
if num == False: 
  print("Deve conter apenas números")
print(mac.replace('0','A',1))
