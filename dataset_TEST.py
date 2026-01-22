import pandas as pd
import numpy as np

# Fixer la seed pour reproductibilité
np.random.seed(42)

# Nombre de clients
n_clients = 1000

# Génération de variables réalistes pour un dataset bancaire
df = pd.DataFrame({
    "ID_Client": np.arange(1, n_clients + 1),
    "Age": np.random.randint(18, 75, n_clients),
    "Revenu_annuel": np.random.randint(20000, 150000, n_clients),
    "Montant_prêt": np.random.randint(5000, 500000, n_clients),
    "Durée_prêt_mois": np.random.choice([12, 24, 36, 48, 60, 72, 84], n_clients),
    "Score_Crédit": np.random.randint(300, 850, n_clients),
    "Nombre_de_credits_ouverts": np.random.randint(0, 10, n_clients),
    "Retards_30j": np.random.poisson(0.5, n_clients),
    "Retards_60j": np.random.poisson(0.2, n_clients),
    "Encours_total": np.random.randint(1000, 200000, n_clients),
    "Type_de_prêt": np.random.choice(["Personnel", "Immobilier", "Auto", "Carte"], n_clients),
    "Historique_defauts": np.random.randint(0, 5, n_clients)
})

print(df.head())