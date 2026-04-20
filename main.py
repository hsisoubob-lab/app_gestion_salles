from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Test connexion
print("Connexion OK")

# Ajouter une salle
s = Salle("A101", "Salle informatique", "Laboratoire", 30)
dao.insert_salle(s)
print("Salle ajoutée")

# Afficher toutes les salles
salles = dao.get_salles()
for salle in salles:
    salle.afficher_infos()