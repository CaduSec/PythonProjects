import time
import subprocess

while True:
    # Set the IP range for the network to be scanned
    network = "192.168.1.0/24"

    # Run nmap to scan the network for live hosts
    results = subprocess.run(["nmap", "-sn", network, "-n", "-T4"], stdout=subprocess.PIPE)

    # Split the output into lines
    lines = results.stdout.decode().strip().split("\n")

    # Print the header row
    print("IP address\tStatus\tDNS name")

    # Iterate over the lines
    for line in lines:
        # Split the line into columns
        columns = line.split()

        # Print the IP address, status, and DNS name
        print(f"{columns[0]}\t{columns[1]}\t{columns[2]}")

    # Wait 20 minutes before scanning again
    time.sleep(1200)
