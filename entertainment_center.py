
import video
import movie
import tv_show
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
                        120,
                        "G",
                        "A story of a boy and his toys to life",
                        "http://images.ciatr.jp/2015/07/28182108/group-disney-announces-toy-story-4-is-happening-126226-640x432.jpeg",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")
avater = movie.Movie("Avater",
                        120,
                        "G",
                        "A Marine on an alian planet",
                        "https://i.kinja-img.com/gawker-media/image/upload/rpmlcli7mfr4petrpqqc.jpg",
                        "https://www.youtube.com/watch?v=qYe-ncx3rVE")
akira = movie.Movie("AKIRA",
                        120,
                        "G",
                        "Psychicer in Tokyo 2020",
                        "http://blog-imgs-19.fc2.com/c/i/n/cinemaxj/AKIRA.jpg",
                        "https://www.youtube.com/watch?v=LALsuMWv2ps")
gundam = movie.Movie("GUNDAM",
                        120,
                        "G",
                        "War in the space with battle vehicles called GUNDAM",
                        "http://blogs.c.yimg.jp/res/blog-55-71/universalcentuly/folder/1698020/20/62936720/img_0",
                        "https://www.youtube.com/watch?v=wpQUmdw5U8Y")
jurassic_park = movie.Movie("JURASSIC PARK",
                        120,
                        "G",
                        "Clone dinosaur assault people",
                        "http://ecx.images-amazon.com/images/I/71sXDxo9k7L._SL1106_.jpg",
                        "https://www.youtube.com/watch?v=lc0UehYemQA")
life_is_beautiful = movie.Movie("Life is Beautiful",
                        120,
                        "G",
                        "a father with great humanity in WW2",
                        "http://thumbnail.image.rakuten.co.jp/@0_mall/elcommun/cabinet/poster_cinema/img55479640.jpg?_ex=350x350&s=2&r=1",
                        "https://www.youtube.com/watch?v=w5RyZ9qAEKs")
walking_dead = tv_show.TvShow("WALKING DEAD",
                        60,
                        "PG",
                        "Escape from walking dead!!",
                        "http://cdn.bgr.com/2015/01/the-walking-dead-season-5-trailer.png",
                        "https://www.youtube.com/watch?v=R1v0uFms68U",
                        [["season1",11,"danger"],["season2",12,"more danger"],["season3",10,"danger*3"],["season4",8,"danger*4"],["season5",9,"danger*5"]],
                        ["episode1","episode2","episode3","episode4"],
                        "FOX")
blaking_bad = tv_show.TvShow("BLAKING BAD",
                        60,
                        "PG-13",
                        "A Sience Teacher fall in drug dealer",
                        "http://www.themindtrap.com/img/rooms/breaking-bad-1.jpg",
                        "https://www.youtube.com/watch?v=HhesaQXLuRY",
                        [["season1",11,"bad"],["season2",12,"worse"],["season3",10,"worst"]],
                        ["episode1","episode2","episode3","episode4"],
                        "AMC")

movies = [toy_story, avater, akira, gundam, jurassic_park,life_is_beautiful]
tv_shows = [walking_dead, blaking_bad]

fresh_tomatoes.open_movies_page(movies,tv_shows)
