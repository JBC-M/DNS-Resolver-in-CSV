import csv
import socket

def dns_lookup(ip_addresses):
    dns_names = {}
    for ip in ip_addresses:
        try:
            dns_name_full = socket.gethostbyaddr(ip)[0]
            dns_name_truncated = dns_name_full.split('.')[0]
            dns_names[ip] = dns_name_truncated
        except socket.herror:
            dns_names[ip] = "N/A"
    return dns_names

if __name__ == "__main__":
    # Input CSV file containing IP addresses
    input_csv_file = "ip_addresses.csv"
    # Output CSV file to save results
    output_csv_file = "dns_names.csv"

    ip_addresses = []
    with open(input_csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            ip_addresses.extend(row)

    result = dns_lookup(ip_addresses)

    # Write results to a new CSV file
    with open(output_csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "DNS Name"])  # Write header
        for ip, dns_name in result.items():
            writer.writerow([ip, dns_name])

    print("Results saved to:", output_csv_file)
