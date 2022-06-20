from datetime import date , datetime
import random
horaire_debut="9:00"
horaire_fin="17:00"
heure_debut_repas="13:00"
heure_fin_repas="14:00"


liste_jour_conge=[date(2022, 7, 14),date(2022, 8, 15)]

start_date = date(year = 2022, month =6, day=13)
end_date = date(year=2022, month=9, day=30)
delta = end_date - start_date
nb_jour_tot = delta.days+1-(delta.days//7)*2
#print("Tu dois travailler {} jours au total".format(nb_jour_tot))

for jour_conge in liste_jour_conge :
    if jour_conge>start_date:
        if jour_conge<end_date:
            nb_jour_tot-=1
print("Tu dois travailler {} jours au total (sans j. fériés)".format(nb_jour_tot))

today = date.today()
delta = end_date - today
nb_jour_restant = delta.days+1-(delta.days//7)*2
#print("Il te reste {} jours à travailler".format(nb_jour_restant))

for jour_conge in liste_jour_conge :
    if jour_conge>today:
        if jour_conge<end_date:
            nb_jour_restant-=1
print("Il te reste {} jours à travailler (sans j. fériés)".format(nb_jour_restant))

########HEURE###########

time_start = datetime.strptime(horaire_debut,"%H:%M")
time_end = datetime.strptime(horaire_fin,"%H:%M")

time_start_miam = datetime.strptime(heure_debut_repas,"%H:%M")
time_fin_miam = datetime.strptime(heure_fin_repas,"%H:%M")

time_interval = time_end - time_start
time_now = str(datetime.now().hour)+":"+str(datetime.now().minute)
time_now = datetime.strptime(time_now,"%H:%M")

nb_minute_restant=nb_jour_restant*7*60
nb_minute_restant_j=0
if (time_end<time_now):
    time_avant_fin_j =  time_now - time_end
    hours = time_avant_fin_j.seconds//3600
    minutes = time_avant_fin_j.seconds%60
    print("Frérot rentre chez toi, t'as finis le boulot depuis {} heures et {} minutes.\nT'es pas payé pour faire des heures sup.".format(hours,minutes))

elif (time_now<time_start_miam):
    #avant le repas
    time_avant_fin_j =  time_start_miam - time_now
    minutes = (time_avant_fin_j.seconds)//60
    nb_minute_restant_j=minutes
    print("Plus que {} minutes avant la pause repas, Courage!".format(minutes))
    time_avant_fin_j =  time_end - time_fin_miam
    minutes = (time_avant_fin_j.seconds)//60
    nb_minute_restant_j+=minutes

elif (time_now>time_fin_miam):
    #après le repas
    time_avant_fin_j =  time_end - time_now
    minutes = (time_avant_fin_j.seconds)//60
    nb_minute_restant_j=minutes

else :
    #pendant le repas
    print("Va manger, j'ai faim")
    time_avant_fin_j =  time_end - time_fin_miam
    minutes = (time_avant_fin_j.seconds)//60
    nb_minute_restant_j=minutes

print("Il te reste {} minutes de boulot pour la journée, soit {} heure(s) et {} minutes".format(nb_minute_restant_j,nb_minute_restant_j//60,nb_minute_restant_j%60))

nb_minute_restant = (nb_jour_restant-1)*7*60 + nb_minute_restant_j

print("Il te reste {} heures et {} minutes avant la fin de ton stage".format(nb_minute_restant//60,nb_minute_restant_j%60))
print("Tu as donc fait {} % de ton stage".format((1-(nb_minute_restant/ (nb_jour_tot*7*60) ))*100))

liste_motivation=[
    "Rien à foutre de ta dépression",
    "Et ça fait bim, bam, boum, allez cheh comme ça tu l'as dans la tête pour la journée",
    "C'est pas le monde des bisounours",
    "Il y a vraiment plus de saisons",
    "Dis-moi, t'as pris du muscle",
    "Allez souris, ça va bien se passer\n\nSouris j'ai dit, ça va sécréter de la dopamine, l'hormone du bonheur",
    "T'imagines tu meurs avant la fin de ton stage, ce serait relou.",
    "Dis-toi qu'à la fin du mois, t'auras un gros sala... ouais non en fait oublie.",
    "Allez mon gars, je sais que c'est dur, comme du pain rassis",
    "Tu veux arrêter c'est ça, tu crois que c'est simple la vie.",
    "Je sais qui m'a codée mais il doit être vachement beau",
    "T'sais que t'es beau (belle)!",
    "Oulah, il y a une salle ambiance ici, y'a un enterrement.",
    "\"C'est à moi que tu parles ? C'est à moi que tu parles ? On m'appelle MONSIEUR Porc\" Pumba, Le Roi Lion",
    "\"Yo la carpette, je t'ai pas vu depuis des mille et des cents ! Serre-moi donc le pompom !\" Le Génie dans Aladdin",
    "T'as essayé la cripto ?",
    "Pain au chocolat ou Chocolatine (Ptdr je suis trop drôle, ceci est un cri d'appel : sauvez-moi)",
    "Aussinon je peux te passer un site très utile : \nhttps://www.pole-emploi.fr/accueil/",
    "Ce serait pas cool d'être un chat, pépère ?",
    "\"Il n'est pas de punition plus terrible que le travail inutile et sans espoir\" Albert Camus",
    "Arrête de te plaindre, moi à ton âge, j'avais une orange à Noël",
    "Il ne suffit pas de ressembler à Cetelem pour faire du Cetelem",
    "\nJe m'ennuie à mourir. L'ennui, c'est que je n'en meurs pas.\" Marise Arnaud",
    "Pense à une piscine, un petit coktail, le chant des oiseaux et des cigales. Voilà détendu ? Maintenant retourne au boulot feignasse, les vacances c'est pas pour toute suite.",
    "Le travail c'est comme le chocolat... à toi de finir, je vais pas faire tout le boulot"
]

index_citation= random.randint(0,len(liste_motivation)-1)
print("Aller un petit remontant :\n"+liste_motivation[index_citation])