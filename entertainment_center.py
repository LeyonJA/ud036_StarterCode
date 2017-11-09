# Entertainment Center python file as submmited by Leyon Anderson
#
# Builds a movie website based on predefined thumbnails using the class 'Movie'
# and the provided repository.

import media
import fresh_tomatoes

# Raw data for movie tumbnails.
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY&t=38s")
john_wick = media.Movie("John Wick", "An American neo-noir action thriller film about legendary assassin John Wick.",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
ratatouille = media.Movie("Ratatouille", "The unthinkable combination of a rat and a 5-star gourmet restaurant come together for the ultimate fish-out-of-water tale.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
force_awakens = media.Movie("Star Wars: The Force Awakens", "Follows Rey, Finn and Poe Dameron's search for Luke Skywalker and their fight alongside the Resistance.",
                            "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                            "https://www.youtube.com/watch?v=sGbxmsDFVnE")
hunger_games = media.Movie("The Hunger Games", "An American post-apocalyptic dystopian science fiction action adventure.",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")
green_mile = media.Movie("The Green Mile", "An American fantasy crime drama film.",
                         "https://upload.wikimedia.org/wikipedia/en/e/e2/The_Green_Mile_%28movie_poster%29.jpg",
                         "https://www.youtube.com/watch?v=ctRK-4Vt7dA")

# Stores the movie tumbnails in a list and passes it to open_movies_page() to
# generate the website.
movies = [toy_story, avatar, john_wick, ratatouille, force_awakens, hunger_games,
          green_mile]

fresh_tomatoes.open_movies_page(movies)
