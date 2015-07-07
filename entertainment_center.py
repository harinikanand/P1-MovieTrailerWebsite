# -*- coding: cp1252 -*-
# Import the modules needed for this program
import media
import fresh_tomatoes

# Create an instance of the Movie Class for the following movies:
# Casablanca
# Frozen
# Imitation Game
# North by Northwest
# Forest Gump
# Beauty and the beast
# Planes, Trains and Automobiles
# A Beautiful mind
# Good Will Hunting
# Bourne Identity

# Casablanca
casablanca = media.Movie(
    "Casablanca",
    "It is the story of an American expatriate who must choose between \
    his love for a woman and helping her Czech Resistance leader husband \
    escape the Vichy-controlled Moroccan city  of Casablanca to continue \
    his fight against the Nazis.",
    "https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg",
    "https://www.youtube.com/watch?v=BkL9l7qovsE",
    "Humphrey Bogart, Ingrid Bergman, Paul Henreid",
    "January 23, 1943",
    "Not Rated")

# Frozen
frozen = media.Movie(
    "Frozen",
    "The film tells the story of a fearless princess who sets off on an \
    epic journey alongside a rugged iceman, his loyal pet reindeer, and \
    a naïve snowman to find her estranged sister, whose icy powers have \
    inadvertently trapped the kingdom in eternal winter.",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=TbQm5doF_Uc",
    "Kristen Bell, Idina Menzel, Jonathan Groff, Josh Gad, Santino Fontana",
    "November 27, 2013",
    "PG")

# Imitation Game
imitation_game = media.Movie(
    "Imitation Game",
    "It portrays the story British crypt analyst Alan Turing, who in the \
    film is hired to decrypt German intelligence codes for the British \
    government during World War II.",
    "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",
    "https://www.youtube.com/watch?v=nuPZUUED5uk",
    "Benedict Cumberbatch, Keira Knightley, Matthew Goode, Rory Kinnear,\
    Charles Dance, Mark Strong",
    "28 November 2014",
    "PG-13")

# North by Northwest 
north_by_northwest = media.Movie(
    "North by Northwest",
    "North by Northwest is a tale of mistaken identity, with an innocent \
    man pursued across the United States by agents of a mysterious \
    organization who want to stop his interference in their plans to \
    smuggle out microfilm containing government secrets.",
    "https://upload.wikimedia.org/wikipedia/commons/8/83/Northbynorthwest1.jpg",
    "https://www.youtube.com/watch?v=ek7T9Gyl_J4",
    "Cary Grant, Eva Marie Saint, James Mason, Jessie Royce Landis",
    "July 28, 1959",
    "Not Rated")

# Forest Gump
forest_gump = media.Movie(
    "Forest Gump",
    "The story depicts several decades in the life of Forrest Gump, as \
    low-witted and naïve, but good-hearted and athletically prodigious man\
    from Alabama who witnesses, and in some cases influences, some of the \
    defining events of the latter half of the 20th century in the United \
    States",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=uPIEn0M8su0",
    "Tom Hanks, Robin Wright, Gary Sinise, Mykelti Williamson, Sally Field",
    "July 6, 1994",
    "PG-13")

# Beauty and the Beast
beauty_and_the_beast = media.Movie(
    "Beauty and the Beast",
    "Beauty and the Beast focuses on the relationship between the Beast, a \
    prince who is magically transformed into a monster as punishment for his \
    arrogance, and Belle , a young woman whom he imprisons in his castle. \
    To become a prince again, the Beast must love Belle and win her love in \
    return, or he will remain a Beast forever.",
    "https://upload.wikimedia.org/wikipedia/en/7/7c/Beautybeastposter.jpg",
    "https://www.youtube.com/watch?v=tRlzmyveDHE",
    "Paige O'Hara, Robby Benson, Richard White, Jerry Orbach, Angela Lansbury",
    "November 22, 1991",
    "G")

# Planes, Trains and Automobiles
planes_trains_automobiles = media.Movie(
    "Planes, Trains and Automobiles",
    "The film stars Steve Martin as Neal Page, a high-strung marketing \
    executive, who meets Del Griffith, played by John Candy, an eternally\
    optimistic, overly talkative, and clumsy showercurtain ring salesman \
    who seems to live in a world governed by a different set of rules.",
    "https://upload.wikimedia.org/wikipedia/en/d/d6/Planes_trains_and_automobiles.jpg",
    "https://www.youtube.com/watch?v=VWGqGHMO294",
    "Steve Martin, John Candy",
    "November 25, 1987",
    "R")

# A Beautiful mind
a_beautiful_mind = media.Movie(
    "A Beautiful Mind",
    "The movie tells the story of young prodigy named John Nash.",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
    "https://www.youtube.com/watch?v=YWwAOutgWBQ",
    "Russell Crowe, Ed Harris, Jennifer Connelly, Christopher Plummer",
    "December 21, 2001",
    "PG-13")

# Good Will Hunting
good_will_hunting = media.Movie(
    "Good Will Hunting",
    "The  film is about a 20-year-old South Boston laborer Will Hunting, an \
    unrecognized genius who, as part of a deferred prosecution agreement after\
    assaulting a police officer, becomes a patient of a therapist and \
    studies advanced mathematics.",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=WDcMUCpppVs",
    "Matt Damon, Robin Williams, Ben Affleck, Minnie Driver, Stellan Skarsgard",
    "December 5, 1997",
    "R")

# The Bourne Identity
bourne_identity = media.Movie(
    "The Bourne Identity",
    "The film is about action spy thriller film adaptation of Robert Ludlum's \
    novel of the same name.",
    "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
    "https://www.youtube.com/watch?v=FpKaB5dvQ4g",
    "Matt Damon, Franka Potente, Chris Cooper, Clive Owen, Julia Stiles",
    "June 14, 2002",
    "PG-13")

# Create a list of movies with the objects of Movie Class
movies = [casablanca, frozen, imitation_game, north_by_northwest, forest_gump,
          beauty_and_the_beast, planes_trains_automobiles, a_beautiful_mind,
          good_will_hunting, bourne_identity]

# Provide the movies list to open_movies_page method of fresh_tomotoes to
# generate the fresh_tomotoes.html page
fresh_tomatoes.open_movies_page(movies)
