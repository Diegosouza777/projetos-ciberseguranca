import socket

alvo= input("digite o endereço ip do alvo -")

for porta in range (1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    resultado = s.connect_ex((alvo, porta))

    if resultado == 0:

        print (f"Porta {porta} aberta")

        try:
            s.send(b"HEAD / HTTP/1.0\n\r\n\r")
            banner = s.recv(1024)

            print(f"Banner: {banner.decode().strip()}")

        except:
            print("banner não encontrado")

s.close