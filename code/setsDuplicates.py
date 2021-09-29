# def remove_duplicates(some_list):
#     without_duplicates = [] #lista que contenga elementos sin repetir
#     for element in some_list:
#         if element not in without_duplicates: #Si no esta elemento lo agrega a la lista
#             without_duplicates.append(element)
#     return without_duplicates

# def run():
#     random_list = [1, 1, 2, 2, 4]
#     print(remove_duplicates(random_list))

# if __name__ == "__main__":
#     run()
def remove_duplicates(some_list):
    return set(some_list)

def run():
    random_list = [1, 1, 2, 2, 4, 5, 5, 6, 6]
    print(remove_duplicates(random_list))

if __name__ == "__main__":
    run()
