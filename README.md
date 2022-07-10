# Progress_Stage

Des paramètres sont à changer :

Les horaires :

horaire_debut="9:00"

horaire_fin="17:00"

heure_debut_repas="13:00"

heure_fin_repas="14:00"

Et également les dates de début et fin de stage :
(ex : stage du 13/06/2022 au 30/09/2022)

start_date = date(year = 2022, month =6, day=13)

end_date = date(year=2022, month=9, day=30)

Seuls les 2 jours fériés de juillet et août sont pris en compte.

Définir le taux horaire : 
taux_horaire=3.90 # € par heure

nb_minute_inutile_j = 40 # nombre de minute inutile passé par jour (cause pause café longue, retard transport, pause caca passé à scroller)

jour_paye = 31 #Jour de paiement du stage (si dernier jour du mois mettre 31)
