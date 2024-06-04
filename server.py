import socket

def handle_client(client_socket):
    # Receive data from client socket and decode it from bytes to a UTF-8 string
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        print("No data received.")
        return
    # Turn data into string/numbers
    operation, operand1, operand2 = data.split()
    operand1 = float(operand1)
    operand2 = float(operand2)

    if operation == '+':
        result = operand1 + operand2 # addition
    elif operation == '-':
        result = operand1 - operand2 # subtraction
    elif operation == '*':
        result = operand1 * operand2 # multiplication
    elif operation == '/':
        if operand2 == 0:
            result = float('inf')  # Handle division by zero
        else:
            result = operand1 / operand2  # division

    client_socket.send(str(result).encode('utf-8'))
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 7777))
    server_socket.listen(1)
    print("Server is listening on port 7777")
    # Tried to make it so that it continuously accepts the client connection but any user error will cause an immediate rejection to the connection
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
