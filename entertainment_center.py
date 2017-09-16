'''Main Script to run, this handles commands for generating the static webpage and populating the data store'''

import fresh_tomatoes
import media


# These are a few of my favorite movies
toy_story = media.Movie(
    "Toy Story",
    "A movie about inanimate love",
    "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

despicable_me = media.Movie(
    "Despicable Me",
    "The mischievous Minions hope that Gru will return to a life of crime",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcTg3JQThacqbSPauObMc700jNW_GTAd-e9DAV_QIWvMYq8v3mVx",
    "https://www.youtube.com/watch?v=6DBi41reeF0")

sin_city = media.Movie(
    "Sin City",
    "Sin City is a 2005 American neo-noir crime anthology film written, produced, and directed by Frank Miller and Robert Rodriguez.",
    "http://www.gstatic.com/tv/thumb/movieposters/35634/p35634_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=T2Dj6ktPU5c")

star_wars = media.Movie(
    "Star Wars (Film Series)",
    "It depicts the adventures of various characters 'a long time ago in a galaxy far, far away'",
    "http://posterwire.com/wp-content/uploads/star_wars_hildebrandt_art.jpg",
    "https://www.youtube.com/watch?v=zB4I68XVPzQ")

v_vendatta = media.Movie(
    "V For Vendatta",
    "V for Vendetta is a 2005 dystopian political thriller film set in an alternative future where a neo-fascist regime has subjugated the United Kingdom.",
    "http://posterwire.com/wp-content/uploads/v_for_vendetta_b.jpg",
    "www.youtube.ng/watch?v=qxyUl9M_7vc")

pulp_fiction = media.Movie(
    "Pulp Fiction",
    "Pulp Fiction is a 1994 American black comedy neo-noir crime film that connects the intersecting storylines of Los Angeles mobsters, fringe players, small-time criminals, and a mysterious briefcase.",
    "http://www.gstatic.com/tv/thumb/movieposters/15684/p15684_p_v8_ac.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

#store movie instances in an array 
movies = [toy_story, despicable_me, sin_city, star_wars, v_vendatta, pulp_fiction]

#render and open movie trailer website
fresh_tomatoes.open_movies_page(movies)
