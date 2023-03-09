import pandas as pd 
#on peut ameliorer ce code en le combina avec une bibliothèque graphique, une base de donnée , et une sorte base de données 
# et si
nom=[]
prenom=[]
sexe=[]
tribu=[]
contact=[]
departement=[]

while True:
    noms = input("entrer un nom:")
    prenoms = input("entrer un prénom: ")
    sexes = input(" spécifier le sexe avec la lettre M ou F : ")
    tribus = input("quelle est la tribu: ")
    contacts = int(input("quelle est le numéro de la personne :"))
    departements=input("quelle est le département")

    nom.append(noms)
    prenom.append(prenoms)
    sexe.append(sexes)
    tribu.append(tribus)
    contact.append(contacts)
    departement.append(departements)
    tags_excel = input("avez vous finis svp:")
    if tags_excel=="oui":
        print(nom)
        break
    # definissions des cols $
col1="NOM"
col2="PRENOM"
col3="SEXE"
col4="TRIBU"
col5="CONTACTS"
col6="DEPARTEMENTS"
data=pd.DataFrame({col1:nom,col2:prenom,col3:sexe,col4:tribu,col5:contact,col6:departement})
data.to_excel('sample4__data.xlsx',sheet_name='sheet1')
         
