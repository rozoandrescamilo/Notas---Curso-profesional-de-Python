def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower() #Borrar espacios de la palabra
    return string == string[::-1] #Poner la palabra al revés 

def run():
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()