
import time

def ciclo():
    cnt = 0
    print("¡Holaaa! El programa está iniciando...")

    try:
        while True:
            print(f"{cnt}: Ciclo en ejecución...")

            if cnt > 0 and cnt % 5 == 0:
                print("¡Aviso! Se han completado 5 ciclos más.")

            cnt += 1
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n¡Programa detenido por el usuario!")
        print(f"Se completaron {cnt} ciclos.")

if __name__ == "__main__":
    ciclo()
