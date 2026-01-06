import csv


prodelec=[]
stockhydrau=[]
annéehydrau=[]
consoelecpompage=[]


with open('evoproductionelec.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        prodelec.append(row)
with open('evostockhydrau.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        stockhydrau.append(row)
with open('consoelecpompagestep.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        consoelecpompage.append(row)

#suppression de cette ligne car il n'y a pas de valeur et donc empèche de passer les données en float
del stockhydrau[281] 
del stockhydrau[141]
     
        
del prodelec[0]
del stockhydrau[0]
del consoelecpompage[0]
                                
        
prodelec=[float(prodelec[i+1][2].replace(",",".")) for i in range(len(prodelec)-1)]
print(prodelec)
print(type(prodelec[0]))

consoelecpompage=[float(consoelecpompage[i+1][2].replace(",",".")) for i in range(len(consoelecpompage)-1)]
print(consoelecpompage)

annéehydrau=[stockhydrau[i+1][0]for i in range(len(stockhydrau)-1)]
print(annéehydrau)

stockhydrau=[float(stockhydrau[i+1][2].replace(",",".")) for i in range(len(stockhydrau)-1)]
print(stockhydrau)



