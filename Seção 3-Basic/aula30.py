velocidade = 61
local_carro = 99

RADAR_1 = 60 #Velocidade máxima do radar 1
LOCAL_1 = 100 #Local onde o radar 1 está
RADAR_RANGE = 1 # Adistância onde o radar pega
MAX_RAIO = LOCAL_1 + RADAR_RANGE #Minimo alcance do radar
MIN_RAIO = LOCAL_1 - RADAR_RANGE #Maximo alcance do radar


velocidade_carro_passou_do_radar = velocidade <= RADAR_1

carro_no_raio_do_radar = local_carro <= (MAX_RAIO) and local_carro >= (MIN_RAIO)

if carro_no_raio_do_radar:
    print("não recebeu multa" if velocidade_carro_passou_do_radar else "recebeu multa")
else:
    print("Longe do radar")
          