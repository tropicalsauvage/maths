from tabulate import tabulate

# Données de l'exemple
categories = ['Back-End', 'Front-End', 'DataBases']
donnees = [
    ['Node.js', 'React.js', 'MariaDB'],
    ['Rubis', 'HTML', 'MongoDB'],
    ['PHP', 'CSS', 'NOSQL']
]

# Affichage de la table
print(tabulate(donnees, headers=categories, tablefmt='grid'))