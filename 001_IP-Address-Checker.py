# Read an IP address from user input, strip whitespace, and split into octets
ip: list[int] = list(map(int, input("Enter an IP address:").strip().split('.')))

# Create a copy of the IP address as a string for display purposes
ipCopy = list(map(str, ip))
ipCopy = '.'.join(ipCopy)  # Join the list of string octets into a single string

# Print the formatted IP address
print(ipCopy)

# Initialize a counter for valid octets and a flag for validity
trueOctetCount: int = 0
flag: bool = True

# Loop through each octet to validate
for octet in ip:
    # Check if the octet is within the valid range of 0-255
    if octet in range(0, 256):
        trueOctetCount += 1  # Increment the valid octet count
    else:
        flag = False  # Set flag to False if an invalid octet is found
        break  # Exit the loop early since we found an invalid octet

# Check if the flag is still True and if we have exactly 4 valid octets
if flag == True and trueOctetCount == 4:
    print(f"Valid IP: {ipCopy}")  # Print the valid IP address
else:
    # Print an error message if the IP address is invalid
    print(f"Invalid IP address - each octet should be between {{0-255}}: {ipCopy}")
