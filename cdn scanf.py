import socket


def check_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)  # 设置超时时间为3秒
        try:
            sock.connect((ip, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False


def check_multiple_ips(ips, port):
    results = {}
    for ip in ips:
        status = check_port(ip, port)
        results[ip] = "Open" if status else "Closed"
    return results


if __name__ == "__main__":
    # IP list
    proxy_ips = [
        "x.x.x.x",
    ]
    port_to_check = 536
    status_results = check_multiple_ips(proxy_ips, port_to_check)

    for ip, status in status_results.items():
        print(f"IP: {ip}, Port {port_to_check}: {status}")
