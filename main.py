import socket
import pygame
import pickle

HOST = '127.0.0.1'
PORT = 5000


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.settimeout(0.2)

print(f"Connected to server at {HOST}:{PORT}")

player_count_tick_rate = 20
player_count_count = 0

def init_map():
    data = None
    flag = "map"
    message = [flag, data]
    message = pickle.dumps(message)
    client_socket.sendall(message)
    response = client_socket.recv(4048)
    response = pickle.loads(response)
    return response

def init_player(pick):
    flag = "pick"
    message = [flag, pick]
    message = pickle.dumps(message)
    client_socket.sendall(message)
    response = client_socket.recv(4048)
    response = pickle.loads(response)
    return response

def get_all_position():
    data = None
    flag = "position"
    message = [flag, data]
    message = pickle.dumps(message)
    client_socket.sendall(message)
    response = client_socket.recv(4048)
    response = pickle.loads(response)
    return response

def get_player_count():
    data = None
    flag = "player_count"
    message = [flag, data]
    message = pickle.dumps(message)
    client_socket.sendall(message)
    response = client_socket.recv(4048)
    response = pickle.loads(response)
    return response

def get_all_player_pick():
    data = None
    flag = "player_pick"
    message = [flag, data]
    message = pickle.dumps(message)
    client_socket.sendall(message)
    response = client_socket.recv(4048)
    response = pickle.loads(response)
    return response

player = init_player("Sniper")
position = get_all_position()
player_count = get_player_count()
Map = init_map()

print(player)
print(position)
print(player_count)
print(Map)







