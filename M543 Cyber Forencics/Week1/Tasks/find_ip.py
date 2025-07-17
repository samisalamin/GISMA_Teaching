from collections import defaultdict

# Read the log file
with open("access_log.txt", "r") as file:
    lines = file.readlines()

ip_counts = defaultdict(int)
failed_attempts = defaultdict(int)

# Process each line
for line in lines:
    parts = line.strip().split(" | ")
    if len(parts) == 3:
        timestamp, ip, status = parts
        ip_counts[ip] += 1
        if status == "LOGIN_FAILED":
            failed_attempts[ip] += 1

# Identify suspicious IPs
suspicious_ips = [ip for ip, count in failed_attempts.items() if count > 3]

# Output results
print("IP Address Counts:")
for ip, count in ip_counts.items():
    print(f"{ip}: {count} attempts")

print("\nSuspicious IPs (more than 3 failed attempts):")
for ip in suspicious_ips:
    print(ip)
