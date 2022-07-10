# Progress_Stage
launch_buttons:
  colab_url: "https://colab.research.google.com/github/julien-leplat/Progress_Stage" 

Affichage :
![image](https://user-images.githubusercontent.com/80824116/178150433-a77e53ac-7603-4735-9f87-17b6b64f1684.png)


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
