max=0
i=0
a= input("Inserisci un numero: ")
a= int(a)
while i<10:
	if a>max:
		max=a
	i+=1
	a=input("Inserisci un altro numero: ")
	a= int (a)
print ("Il max è: ",max)