import movies

toy_story = movies.Movie("toys are alive!", "https://www.youtube.com/watch?v=KYz2wyBy3kc", "https://vignette.wikia.nocookie.net/pixar/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20160329080002", "Toy Story")

print(toy_story.plot_summary)
print(toy_story.trailer_url)
print(toy_story.poster_image_url)
print(toy_story.title)

avatar = movies.Movie("blue alien native americans get dances with wolves'd by white people", "https://www.youtube.com/watch?v=5PSNL1qE6VY", "https://www.movieposter.com/posters/archive/main/98/MPW-49246", "Avatar")

print(avatar.plot_summary)
print(avatar.trailer_url)
print(avatar.poster_image_url)
print(avatar.title)
