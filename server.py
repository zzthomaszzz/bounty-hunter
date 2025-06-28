import socket
import threading
import random
import pickle
from bounty_hunter import *
from player import Player

HOST = '127.0.0.1'  # Localhost
PORT = 5000

sockets = []
players = []

def process_data(data, _id):
    data = pickle.loads(data)
    flag = data[0]
    body = data[1]
    match flag:
        case "pick":
            match body:
                case Sniper.name:
                    res = Sniper()
                case Bruiser.name:
                    res = Bruiser()
                case Protector.name:
                    res = Protector()
                case Tank.name:
                    res = Tank()
                case _:
                    res = BountyHunter()
            player_data = Player(res, _id)
            players.append(player_data)
            message = pickle.dumps(player_data)
            return message



def handle_client(client_socket, addr, _id):
    try:
        print(f"Accepted connection from {addr}")
        while True:
            try:
                data = client_socket.recv(4048)
                if not data:
                    break
                res = process_data(data, _id)
                print(f"Received from {addr}: {data}")
                client_socket.sendall(res)
            except ConnectionResetError:
                break
        print(f"Client {addr} disconnected")
    finally:
        if client_socket in sockets:
            sockets.remove(client_socket)
        for player in players:
            if player.id ==_id:
                players.remove(player)
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        _id = random.random()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr, _id))
        sockets.append([client_socket, _id])
        client_handler.start()


start_server()