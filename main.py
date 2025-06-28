import socket
import pygame
import pickle

HOST = '127.0.0.1'
PORT = 5000


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.settimeout(0.2)

print(f"Connected to server at {HOST}:{PORT}")

def init_player(pick):
    flag = "pick"
    message = [flag, pick]
    message = pickle.dumps(message)
    client_socket.sendall(message)
    response = client_socket.recv(4048)
    response = pickle.loads(response)
    return response

def get_all_position():
    players_position = []
    flag = "position"
    message = flag
    message = pickle.dumps(message)
    client_socket.sendall(message)
    response = client_socket.recv(4048)
    response = pickle.loads(response)
    return response

player = init_player("Sniper")
print(player)







