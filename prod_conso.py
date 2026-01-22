import csv


prodelec=[]
annéehydrau=[]
consoelecpompage=[]
datesprodhydrau=[]

with open('evoproductionelec.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        prodelec.append(row)
with open('consoelecpompagestep.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        consoelecpompage.append(row)
     
        
del prodelec[0]

del consoelecpompage[0]
                                
        
prodelechydrau=[float(ligne[2].replace(",",".")) for ligne in prodelec if ligne[1]=="Production hydraulique"]
datesprodhydrau= [ligne[0] for ligne in prodelec if ligne[1]=="Production hydraulique"]


print(prodelechydrau)
#print(type(prodelec[0]))
print(datesprodhydrau)


consoannée=[consoelecpompage[i+1][0]for i in range(len(consoelecpompage)-1)]
consoelecpompage=[float(consoelecpompage[i+1][2].replace(",",".")) for i in range(len(consoelecpompage)-1)]
#print(consoelecpompage)

#écriture en mois pour la lecture du graphique
moisconso= list(range(1,len(consoannée)+1))
moisprod= list(range(1,len(datesprodhydrau)+1))



from matplotlib import pyplot as plt


plt.plot(moisconso,consoelecpompage,color='b')
plt.plot(moisprod,prodelechydrau,color='r')


plt.title("hydraulique sur 11 ans")
plt.ylabel('énergie (GWh)')
plt.xlabel('mois de 2014 à 2025')
plt.show()
