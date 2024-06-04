import socket

def send_request(operation, operand1, operand2):
    # set to connect specifically at port 7777 at this IP address
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 7777))
    # format data into string and operands/operators
    data = f"{operation} {operand1} {operand2}"
    client_socket.send(data.encode('utf-8'))
    # print result
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Result: {response}")
    
    client_socket.close()








