import customtkinter as ctk
from tkinter import ttk, messagebox
from services.services_salle import ServiceSalle
from models.salle import Salle

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Gestion des Salles")
        self.geometry("800x600")
        self.service_salle = ServiceSalle()

        # Cadre Informations Salle
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.cadreInfo, text="Code Salle :").grid(row=0, column=0, padx=10, pady=5)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Description :").grid(row=1, column=0, padx=10, pady=5)
        self.entry_description = ctk.CTkEntry(self.cadreInfo)
        self.entry_description.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Catégorie :").grid(row=2, column=0, padx=10, pady=5)
        self.entry_categorie = ctk.CTkEntry(self.cadreInfo)
        self.entry_categorie.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Capacité :").grid(row=3, column=0, padx=10, pady=5)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=5)

        # Cadre Actions
        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10, fill="x")

        ctk.CTkButton(self.cadreActions, text="Ajouter", command=self.ajouter_salle).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(self.cadreActions, text="Modifier", command=self.modifier_salle).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(self.cadreActions, text="Supprimer", command=self.supprimer_salle).grid(row=0, column=2, padx=10, pady=10)
        ctk.CTkButton(self.cadreActions, text="Rechercher", command=self.rechercher_salle).grid(row=0, column=3, padx=10, pady=10)

        # Cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self, corner_radius=10)
        self.cadreList.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "description", "categorie", "capacite"), show="headings")
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")
        self.treeList.column("code", width=50)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        # Charger la liste au démarrage
        self.lister_salles()

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))

    def ajouter_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_description.get(),
            self.entry_categorie.get(),
            self.entry_capacite.get()
        )
        resultat, message = self.service_salle.ajouter_salle(salle)
        messagebox.showinfo("Info", message)
        self.lister_salles()

    def modifier_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_description.get(),
            self.entry_categorie.get(),
            self.entry_capacite.get()
        )
        resultat, message = self.service_salle.modifier_salle(salle)
        messagebox.showinfo("Info", message)
        self.lister_salles()

    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service_salle.supprimer_salle(code)
        messagebox.showinfo("Info", "Salle supprimée avec succès")
        self.lister_salles()

    def rechercher_salle(self):
        code = self.entry_code.get()
        salle = self.service_salle.rechercher_salle(code)
        if salle:
            self.entry_code.delete(0, "end")
            self.entry_code.insert(0, salle.code)
            self.entry_description.delete(0, "end")
            self.entry_description.insert(0, salle.description)
            self.entry_categorie.delete(0, "end")
            self.entry_categorie.insert(0, salle.categorie)
            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, salle.capacite)
        else:
            messagebox.showerror("Erreur", "Salle non trouvée")