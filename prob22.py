#copier le fichier en une liste
def sorted_list():
    with open("0022_names.txt",'r') as file:
        contenu=file.read()
    # Diviser la chaîne en une liste en utilisant la virgule comme séparateur
        l=contenu.split(",")
    # Enlever les guillemets doubles de chaque élément de la liste
        liste_sans_guillemet=[element.strip('"')for element in l]
        l1=sorted(liste_sans_guillemet)
    return l1
#print(sorted_list())

def alphabetical_value(c):
    return ord(c)-64
#print(alphabetical_value("L"))

def sum_alphabetical_value(ch):
    s=0
    for e in ch:
        s+=alphabetical_value(e)
    return s
#print(sum_alphabetical_value("COLIN"))

def total_name_scores():
    l=sorted_list()
    s=0
    for i in range(len(l)):
        s+=(i+1)*sum_alphabetical_value(l[i])  #score de chaque element de la liste
    return s
print(total_name_scores())
        
    
