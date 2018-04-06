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

school_of_rock = movies.Movie("School of Rock",
                            "Overly enthusiastic guitarist Dewey Finn (Jack Black) gets thrown out of his bar band and finds himself in desperate need of work. Posing as a substitute music teacher at an elite private elementary school, he exposes his students to the hard rock gods he idolizes and emulates -- much to the consternation of the uptight principal (Joan Cusack). As he gets his privileged and precocious charges in touch with their inner rock 'n' roll animals, he imagines redemption at a local Battle of the Bands.",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcRMRyrfvOfl7RStLTmLNBIf86oc677YSkxdw1XeNHV928aAdL_3")

coco = movies.Movie("Coco",
                    "Despite his family's generations-old ban on music, young Miguel dreams of becoming an accomplished musician like his idol Ernesto de la Cruz. Desperate to prove his talent, Miguel finds himself in the stunning and colorful Land of the Dead. After meeting a charming trickster named Héctor, the two new friends embark on an extraordinary journey to unlock the real story behind Miguel's family history.",
                    "https://www.youtube.com/watch?v=xlnPHQ3TLX8",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcS3FGIsangc2iauB89mttkiBAvIDj_O952Ypk2p5QqABby--L6d")

midnight_in_paris = movies.Movie("Midnight in Paris",
                                "Gil Pender (Owen Wilson) is a screenwriter and aspiring novelist. Vacationing in Paris with his fiancee (Rachel McAdams), he has taken to touring the city alone. On one such late-night excursion, Gil encounters a group of strange -- yet familiar -- revelers, who sweep him along, apparently back in time, for a night with some of the Jazz Age's icons of art and literature. The more time Gil spends with these cultural heroes of the past, the more dissatisfied he becomes with the present.",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4",
                                "https://www.movieposter.com/posters/archive/main/145/MPW-72510")

movie_list = [toy_story, avatar, lady_bird, school_of_rock, coco, midnight_in_paris]

for film in movie_list:
    print_all_movie_attributes(film)
    film.show_trailer()
