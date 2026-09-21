import re

ip_pattern = r"\d+\.\d+\.\d+\.\d+"
status_pattern = r"\d{3}$"

def parse_log_line(line):
    ip_match = re.search(ip_pattern, line)
    if ip_match:
        ip = ip_match.group()
    else:
        print("Invalid log line:", line)
        return None

    status_match = re.search(status_pattern, line)
    if status_match:
        error_code = int(status_match.group())
    else:
        print("Invalid status line:", line)
        return None

    return error_code, ip

def update_count(dictionary, key):
    if key in dictionary:
        dictionary[key] += 1

    else:
        dictionary[key] = 1

def log_analyzer():
    ip_holder = {}

    failed_logins = 0

    failed_ips = {}

    status_codes = {}

    total_requests = 0

    with open("access.log", "r") as file:

        for line in file:

            result = parse_log_line(line)

            if result is None:
                continue
            error_code, ip = result

            update_count(ip_holder, ip)

            if error_code == 401:

                failed_logins += 1

                update_count(failed_ips, ip)

            update_count(status_codes, error_code)

            total_requests += 1

    return ip_holder, failed_ips, status_codes, failed_logins, total_requests

ip_holder, failed_ips, status_codes, failed_logins, total_requests = log_analyzer()

def print_report(ip_holder, failed_ips, status_codes, failed_logins, total_requests):
    print("========== LOG ANALYZER ==========")
    print(f"Total requests: {total_requests}")
    print(f"Failed requests: {failed_logins}")

    print("Suspicious IPs:")
    for ip, failed_count in failed_ips.items():
        if failed_count >= 3:
            print('Brute-force detected:')
            print(f'Suspicious IP : {ip} -- {failed_count}')

    print('Status codes:')
    for status_code, count in status_codes.items():
        print(f'{status_code} : {count}')

    print("ip count:")
    for ip, count in ip_holder.items():
        print(f'{ip} : {count}')

print_report(ip_holder, failed_ips, status_codes, failed_logins, total_requests)

