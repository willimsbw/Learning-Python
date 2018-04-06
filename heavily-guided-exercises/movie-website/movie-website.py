import movies

def print_all_movie_attributes(object):
    print("title: " + object.title +
    "\nplot summary: " + object.plot_summary +
    "\ntrailer url: " + object.trailer_url +
    "\nposwer image url: " + object.poster_image_url)


toy_story = movies.Movie("Toy Story",
                        "toys are alive!",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "https://vignette.wikia.nocookie.net/pixar/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20160329080002")

avatar = movies.Movie("Avatar",
                    "blue alien native americans get dances with wolves'd by white people",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                    "https://www.movieposter.com/posters/archive/main/98/MPW-49246")

lady_bird = movies.Movie("Lady Bird",
                        "A teenager (Saoirse Ronan) navigates a loving but turbulent relationship with her strong-willed mother (Laurie Metcalf) over the course of an eventful and poignant senior year of high school.",
                        "https://www.youtube.com/watch?v=cNi_HC839Wo",
                        "https://cdn.tuftsdaily.com/2017/11/MV5BMjg1NDY0NDYzMV5BMl5BanBnXkFtZTgwNzIwMTEwNDI@._V1_SY1000_CR006761000_AL_-938x535.jpg")


print_all_movie_attributes(toy_story)
print_all_movie_attributes(avatar)
print_all_movie_attributes(lady_bird)
lady_bird.show_trailer()
toy_story.show_trailer()
avatar.show_trailer()
