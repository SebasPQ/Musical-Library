import time
import random
from MusicLib_PathFinder import PathFinder

tests_number = 10000

test_library = PathFinder("songs_data.csv")

# crea simulaciones
simulation_time_i = time.time()
test_library.simulate_paths_2(tests_number)
simulation_time_f = time.time()

simulation_time = (simulation_time_f - simulation_time_i)

# escoge canción aleatoria
find_time = 0
for i in range(tests_number):
    song_name = test_library.random_song()
    # busca la canción
    find_time_i = time.time()
    test_library.find_song(song_name)
    find_time_f = time.time()
    find_time += (find_time_f - find_time_i)

# encontrar recomendación
recommend_time = 0
for i in range(tests_number):
    path_i = [random.randint(0, tests_number-1)]
    # busca las rutas o recomendaciones de esa canción
    recommend_time_i = time.time()
    final_path, frequencies = test_library.next_paths(path_i)
    recommend_time_f = time.time()
    recommend_time += (recommend_time_f - recommend_time_i)

print("\n     PRUEBAS DE TIEMPO DE FUNCIONES PARA {} DATOS\n".format(tests_number))
print("Tiempo para crear las simulaciones (paths): {} s".format(simulation_time))
print("Tiempo para buscar canciones: {} s".format(find_time))
print("Tiempo para encontrar recomendaciones de canciones: {} s".format(recommend_time))
