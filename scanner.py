import socket

print("=== Simple Network Scanner ===")
print("Scanning...\n")


target = "192.168.1."
ports = [21, 22, 80, 443]  # FTP, SSH, HTTP, HTTPS

print("Scanning network and ports...\n")

for i in range(1, 255):
    ip = target + str(i)
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        result = s.connect_ex((ip, port))
        
        if result == 0:
            print(f"[+] {ip} has port {port} OPEN")
        
        s.close()