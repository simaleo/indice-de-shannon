#------------------------------------------------------------------------------------
#Script permettant de calculer l'indice de Shannon-Weaver et d’équitabilité de Piélou
#								  Creer par: Sima leo
#------------------------------------------------------------------------------------


#Importattion des librairies
import pandas
import numpy as np
import os

#Se placer dans le dossier qui contient les donnees
path = 'chemin complet du dossie'
os.chdir(path)

#Importation des donnees
df = pandas.read_excel('donnees.xlsx')

#Remplacer les valeurs nulles par des nan
df = df.replace({0:np.nan})

#Selection des especes
var = ['An. gb s.l', 'An. mar', 'An. mou s.l',
	   'An. fun s.l', 'An. nili s.l', 'An. pal ']

#Dataframe avec les especes selectionnes
dt = df[var]

#Nombre d'especes par site
richesse = df['Richesse']

#Creation de la fonction qui va calculer calculer l'indice de Shannon-Weaver et d’équitabilité de Piélou
def indice(data, richesse):

#	Creation des listes vides
	shannon = []
	pielou = []
	
#	liste des index
	indexe = df['Locality']

	#	Indice de shannon
	for i in range(len(data.index)):
		n = data.iloc[i].dropna()
		N = n.sum()		
		pi = n/N		
		sh = -(pi * np.log2(pi)).sum().round(2)
		shannon.append(sh)

	#	Indice d’équitabilité de Piélou
	for sh, j in zip(shannon, richesse):
		R = (sh/np.log2(j)).round(2)
		pielou.append(R)
			
#	Creation du dataframe
	ar = np.array([shannon, pielou]).T
	dft = pandas.DataFrame(ar, index = indexe, columns = ['Shannon', 'Pielou'])
	
#	Affichage des resultats
	print(dft)
	

#Appel de la fonction
indice(dt, richesse)








