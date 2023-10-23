import csv
import matplotlib.pyplot as plt
import time

def busca_codigo_vertical(codigo):
    codigo_str = str(codigo)
    matches = []
    tiempos = []

    for j in range(1, 51):
        nombre_archivo = "archivo" + str(j) + ".csv"
        cantidad_matches = 0
        start_time = time.time()  # Inicio del temporizador

        with open(nombre_archivo, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            columnas = list(zip(*reader))  # Transpone las filas a columnas

            for columna in columnas:
                subgrupos = [columna[i:i+8] for i in range(0, len(columna), 8)]  # Divide en grupos de 8
                for subgrupo in subgrupos:
                    if codigo_str in subgrupo:
                        cantidad_matches += subgrupo.count(codigo_str)

        end_time = time.time()  # Fin del temporizador
        execution_time = end_time - start_time
        tiempos.append(execution_time)
        matches.append(cantidad_matches)

    plt.bar(range(1, 51), matches)
    plt.xlabel('Archivo')
    plt.ylabel('Matches')
    plt.title('Matches en archivos (vertical, en grupos de 8)')
    plt.savefig('hist2_b.png')
    plt.show()

    print("Tiempos de ejecución:", tiempos)
    print("Tiempo promedio:", sum(tiempos) / len(tiempos))

if __name__ == '__main__':
    student_code = 38930338  # Reemplaza con tu código de estudiante
    busca_codigo_vertical(student_code)
