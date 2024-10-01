import redis
import time


import redis

r = redis.Redis(
  host='redis-16654.c11.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16654,
  password='')
# Configuración de Redis
redis_host = 'redis-16654.c11.us-east-1-2.ec2.redns.redis-cloud.com'
redis_port = 16654  # Cambia al puerto correspondiente
redis_password = ''

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Publicador
def publisher():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()


import redis

r = redis.Redis(
  host='redis-16654.c11.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16654,
  password='YYPVoUdvg2MVLPab7yDVraFKfGlsUNGw')