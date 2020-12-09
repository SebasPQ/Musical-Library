from MusicLib_PathFinder import PathFinder

library = PathFinder("songs_data.csv")
library.simulate_paths(10000, progress=1000)
library.start()