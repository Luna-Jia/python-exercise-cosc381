from movies import Movies

movies = Movies('./movies.txt')

def main():
    while True:
        print("q: quit")
        print("sn: search movie names")
        print("sc: search cast")
        print("list: print all the movie names")
        option = input("Choose an option: ")

        if(option == 'q'):break
        elif (option == "sn"):
            name = input("Enter a search term:")
        elif (option == "sc"):
            cast = input("Enter a search term:")
        elif (option == "list"):
            movies.list_movies_and_cast()
        else:
            print("q: quit")
            print("sn: search movie names")
            print("sc: search cast")
            print("list: print all the movie names")

main()






