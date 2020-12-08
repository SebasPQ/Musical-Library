import os
import time
import random
import operator


class PathFinder:

    paths = []
    choice = "0"
    library = {}
    frequencies = {}
    interactions = []
    message = "MusicLib: path finder"

    def __init__(self, name):
        try:
            with open(name, "r", encoding="utf-8") as file:
                self.interactions = [line[:-1] for line in file.readlines()]
                csv = [interaction.split(",") for interaction in self.interactions]
        except (FileNotFoundError, OSError):
            self.library = {}
        else:
            artists = set(row[0] for row in csv)
            for artist in artists:
                songs = []
                for row in csv:
                    if row[0] == artist:
                        songs.append(row[1])
                self.library[artist] = songs

    def _add_path(self, path_i, path=""):
        path += "." + str(path_i[0])
        sub_path = "." + str(path_i[1])
        if path in self.frequencies.keys():
            if sub_path in self.frequencies.get(path).keys():
                frequency = self.frequencies.get(path).get(sub_path)
                self.frequencies[path][sub_path] = frequency+1
            else:
                self.frequencies[path][sub_path] = 1
        else:
            self.frequencies[path] = {sub_path: 1, }
        if len(path_i) > 2:
            return self._add_path(path_i[1:], path=path)

    def _create_path(self, num_interactions, path="", add=True):
        path_i = []
        while num_interactions > 0:
            path_i.append(random.randint(0, len(self.interactions)-1))
            path += "." + str(path_i[-1])
            num_interactions -= 1
        if add:
            self.paths.append(path)
            self._add_path(path_i)
        else:
            return path, path_i

    def get_info_path(self, path, info=""):
        path = path[1:].split(".")
        if path[0] != '':
            path = [int(num) for num in path]
            for index in path:
                info += self.interactions[index] + " | "
        return info[:-3]

    def get_info_path_i(self, path_i):
        return [self.interactions[i] for i in path_i]

    def simulate_paths(self, num_paths, max_interactions=10, progress=120, num_i=0):
        while num_i < num_paths:
            if not num_i % progress:
                percentage = int(100*num_i/num_paths)
                self.charging_screen("Creando simulaciones ({}/{})".format(num_i, num_paths), percentage)
            self._create_path(random.randint(2, max_interactions))
            num_i += 1
        self.charging_screen("Creando simulaciones ({}/{})".format(num_paths, num_paths), 100)
        input("\n    Presiona una tecla para continuar al menu...")

    def next_paths(self, path_i):
        path = "." + ".".join(str(i) for i in path_i)
        if path in self.frequencies.keys():
            return path, sorted(self.frequencies.get(path).items(), key=operator.itemgetter(1), reverse=True)
        else:
            if len(path_i) > 1:
                return self.next_paths(path_i[1:])
            else:
                return "", []

    def select(self, message, options):
        self.clear()
        print("    {}\n".format(message))
        numbers = []
        for index, option in enumerate(options):
            i = index + 1
            numbers.append(str(i))
            print("      {}. {}".format(i, option))
            if i == len(options):
                self.choice = input("\n    Elige un numero: ")
        if self.choice not in numbers and numbers:
            print("\n    ¡No ingresaste una opcion valida! Por favor intentalo de nuevo.")
            time.sleep(2)
            self.select(message, options=options)

    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("\n\n  {}\n\n".format(self.message))

    def start(self):
        options_menu = ["Crear una simulacion", "Encontrar recomendaciones", "Salir"]
        if self.frequencies:
            options_menu[1] = options_menu[1] + " (simulaciones creadas: {})".format(len(self.paths))
        else:
            options_menu[1] = options_menu[1] + " (no se han creado simulaciones)"
        self.select("Menu principal:", options_menu)
        if self.choice == "1":
            self.select("Generador de simulaciones.", [])
            num1 = int(input("      -Ingrese la cantidad de datos a simular: "))
            num2 = int(input("      -Ingrese el numero maximo de interacciones: "))
            self.paths.clear()
            self.frequencies.clear()
            self.simulate_paths(num1, num2)
            print("\n    ¡Simulaciones creadas con exito!")
            time.sleep(2)
            self.start()
        elif self.choice == "2":
            self.select("Generar una ruta.", [])
            num1 = int(input("      -Ingrese el numero de interacciones en la ruta: "))
            path, path_i = self._create_path(num1, add=False)
            print("\n      ¡Ruta creada con exito!")
            time.sleep(1)
            self.select("Informacion de la ruta.", [])
            print("      -La ruta simulada ({}) es: \n".format(path))
            for i, interaction in enumerate(self.get_info_path_i(path_i)):
                print("        {}. {}".format(i+1, interaction))
            init = time.time_ns()
            final_path, frequencies = self.next_paths(path_i)
            # se puede agregar los paths para solo la última canción
            final = time.time_ns()
            print("\n      -Las primeras recomendaciones para la ruta '{}' son:\n".format(final_path))
            sum_frequencies = 0
            for index, frequency in frequencies:
                print("        + {}  # {}".format(self.interactions[int(index[1:])], frequency))
                sum_frequencies += frequency
            print("\n      -INFORMACION DE LA BUSQUEDA:")
            print("\n        + Ruta original: {}".format(self.get_info_path(path)))
            print("\n        + Ruta final seleccionada: {}".format(self.get_info_path(final_path)))
            print("\n        + Cantidad de rutas encontradas: {}".format(len(frequencies)))
            print("\n        + Frecuencia total de la ruta: {}".format(sum_frequencies))
            print("\n        + Cantidad de rutas simuladas: {}".format(len(self.paths)))
            print("\n        + Tiempo de ejecucion: {} nanosegundos".format(final-init))
            input("\n    Presiona cualquier tecla para volver al menu...")
            self.start()
        elif self.choice == "3":
            print("\n    Gracias por usar la aplicacion, hasta pronto.")
            time.sleep(2)

    def charging_screen(self, message, percentage, edge="  "):
        self.clear()
        print("    {}\n\n".format(message))
        progress_bar = "[{}{}]".format("#" * percentage, " " * (100 - percentage))
        print("    {}{}{}{}".format(edge, progress_bar[:49], "|{}%|".format(percentage), progress_bar[54:]), end="\n\n")


library = PathFinder("data 2020.csv")
library.simulate_paths(10000, progress=100)
library.start()
