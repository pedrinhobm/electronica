import time 

def devuelve_tiempos(N):
    

    tiempos=[]
    datos=[]
    datos_ordenados=[]


    #PARA LEER 
    tik_leer = time.perf_counter_ns()
    with open("pacientes.csv","r",encoding="utf-8") as f:
        for i,linea in enumerate(f): 
          datos.append(linea)  # guardando DATOS
          if i+1 > N:
              break
    datos = datos[1:]                   #PARA ELIMINAR LA PRIMERA linea DEL ARCHIVO LEIDO
    tok_leer = time.perf_counter_ns()


    #PARA ORDENAR
    tik_ordenar = time.perf_counter_ns()
    datos_ordenados = [mee.strip().split(',') for mee in datos]
    datos_ordenados.sort(key=lambda x: int(x[4]))
    tok_ordenar = time.perf_counter_ns()


    #PARA LEER 
    tik_escribir = time.perf_counter_ns()
    with open("pacientes_ordenado.csv",'w', encoding= "utf-8") as a:
        for lineas_para_escribir in datos_ordenados:
            lineas_para_escribir = ",".join(lineas_para_escribir) + "\n"
            a.write(lineas_para_escribir)
    tok_escribir = time.perf_counter_ns()
    

    #PARA ESCRIBIR
    t_leer = tok_leer-tik_leer
    t_ordenar = tok_ordenar-tik_ordenar
    t_escribir = tok_escribir - tik_escribir

    tiempos=[t_leer,t_ordenar,t_escribir]

    return tiempos

if __name__ == '__main__':
    N1 = 500
    N2 = 2500
    N3 = 5000
    ts_500=devuelve_tiempos(N1)
    ts_2500=devuelve_tiempos(N2)
    ts_5000=devuelve_tiempos(N3)
    print("Para N = " f"{N1}"", el tiempo de lectura es "f"{ts_500[0]} ns"", el de escritura es "f"{ts_500[1]} ns"", y el de ordernar los pacientes es " f"{ts_500[2]} ns"".")
    print("Para N = " f"{N2}"", el tiempo de lectura es "f"{ts_2500[0]} ns"", el de escritura es "f"{ts_2500[1]} ns"", y el de ordernar los pacientes es " f"{ts_2500[2]} ns"".")
    print("Para N = " f"{N3}"", el tiempo de lectura es "f"{ts_5000[0]} ns "", el de escritura es "f"{ts_5000[1]} ns"", y el de ordernar los pacientes es " f"{ts_5000[2]} ns"".")

