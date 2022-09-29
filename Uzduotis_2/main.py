import pprint

# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "get_user_average_age" - kaip argumentą priims "users" sąrašą ir
# duoto sąrašo atveju grąžins visų vartotojų amžiaus vidurkį kaip skaičių,
# suapvalintą iki artimiausio sveikojo skaičiaus.

# 2. funkcija "get_users_names" - kaip argumentą priims sąrašą ir duoto sąrašo
# atveju grąžins sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka,
# pvz. ['Alex John', 'Ann Smith', ...].

users = [
  { 'id': '1', 'name': 'John Smith', 'age': 20 },
  { 'id': '2', 'name': 'Ann Smith', 'age': 24 },
  { 'id': '3', 'name': 'Tom Jones', 'age': 31 },
  { 'id': '4', 'name': 'Rose Peterson', 'age': 17 },
  { 'id': '5', 'name': 'Alex John', 'age': 25 },
  { 'id': '6', 'name': 'Ronald Jones', 'age': 63 },
  { 'id': '7', 'name': 'Elton Smith', 'age': 16 },
  { 'id': '8', 'name': 'Simon Peterson', 'age': 30 },
  { 'id': '9', 'name': 'Daniel Cane', 'age': 51 },
]

# 1 funkcija

def get_user_average_age(users):
    """Grąžina visų vartotojų amžiaus vidurkį kaip skaičių, suapvalintą iki artimiausio sveikojo skaičiaus."""
    total_user_age = 0
    for user in users:
      total_user_age += user['age']
      
    avg_user_age=int(round(total_user_age/len(users)))
    
    return avg_user_age

print(get_user_average_age(users))

# 2 funkcija

def get_users_names(users):
    """Grąžina sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka."""
    names=[]
    for user in users:
      names.append(user['name'])
    names.sort()
    
    return names

print(get_users_names(users))