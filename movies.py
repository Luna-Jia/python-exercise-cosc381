class Movies:
    def __init__(self, movies_file):
        self._movies = []

        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx%3 == 0:
                    movie_name = line.rstrip()
                if row_idx%3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx%3 == 2:
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                    movie_name = None
                    movie_cast = None
                row_idx += 1

        if movie_name and movie_cast:
            # Add the last movie to the list
            self._movies.append(
                {
                    'name': movie_name,
                    'cast': movie_cast
                }
            )
    def list_movies_and_cast(self):
        for movie in self._movies:
            print(f"Movie: {movie['name']}")
            print("Cast: " + ", ".join(movie['cast']))
            print()  # For readability
    
    def search_movie_names(self, search_term):
        # Make the search case-insensitive
        search_term = search_term.lower()
        found_movies = [movie['name'] for movie in self._movies if search_term in movie['name'].lower()]
        
        if found_movies:
            print(f"Movies containing '{search_term}':")
            for movie in found_movies:
                print(movie)
        else:
            print(f"No movies found with the term '{search_term}' in their names.")
    
    def search_movie_cast(self, search_term):
        # Make the search case-insensitive
        search_term = search_term.lower()
        found_movies = []

        for movie in self._movies:
            # Find cast members that contain the search term
            matching_cast = [cast_member for cast_member in movie['cast'] if search_term in cast_member.lower()]
            if matching_cast:
                found_movies.append((movie['name'], matching_cast))

        if found_movies:
            print(f"Movies and cast members containing '{search_term}':")
            for movie_name, cast_members in found_movies:
                print(f"{movie_name}")
                print(cast_members)
        else:
            print(f"No movies found with cast members that contain the term '{search_term}'.")



    
    
    

if __name__ == "__main__":
    movies = Movies('./movies.txt')

    
