from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()


print("Connexion OK")

s = Salle("A101", "Salle informatique", "Laboratoire", 30)
dao.insert_salle(s)
print("Salle ajoutée")


salles = dao.get_salles()
for salle in salles:
    salle.afficher_infos()
    from services.services_salle import ServiceSalle
    from models.salle import Salle

    service = ServiceSalle()


    s = Salle("B202", "Salle de classe", "Classe", 25)
    resultat, message = service.ajouter_salle(s)
    print(message)


    salles = service.recuperer_salles()
    for salle in salles:
        salle.afficher_infos()
        print("---")


    s = service.rechercher_salle("B202")
    if s:
        s.afficher_infos()


    s.capacite = 40
    resultat, message = service.modifier_salle(s)
    print(message)


    service.supprimer_salle("B202")
    print("Salle supprimée")