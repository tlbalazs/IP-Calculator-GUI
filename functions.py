import re


def check_input(cidr_block):
    """
    Validates the format and correctness of the provided CIDR block.

    Args:
        cidr_block (str): The CIDR block, e.g., "192.168.1.0/24".

    Returns:
        bool: True if the CIDR block is in the correct format, otherwise raises a ValueError.

    Raises:
        ValueError: If the CIDR block format is incorrect or missing.
    """
    # Regular expressions to validate IP address and prefix
    ip_regex = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    prefix_regex = r"\/(3[0-2]|[12]?[0-9])\b"

    # Check if the IP address and prefix match the expected format
    ip_is_valid = re.match(ip_regex, cidr_block.split("/")[0])
    prefix_is_valid = re.match(prefix_regex, cidr_block[-3:])

    # Raise ValueError if the IP address or prefix format is incorrect
    if not ip_is_valid:
        return False
        # raise ValueError("Wrong or missing IP parameter. "
        #                  "You must follow the IP address dotted-decimal format, such as 192.168.123.234/24!")
    if not prefix_is_valid:
        return False
        # raise ValueError("Wrong or missing IP parameter. "
        #                  "You must follow the IP address dotted-decimal format, such as 192.168.123.234/24!")
    return True


def process_input(cidr_block):
    output = cidr_block.split("/")[0].split(".")
    prefix = cidr_block.split("/")[1]
    output.append(prefix)
    return output


def check_ip_class(host_address):
    """
    Determines the IP address class based on the first octet.

    Args:
        host_address (list): The four octets of the IP address in a list.

    Returns:
        str: The IP address class ('A', 'B', 'C', 'D').
    """
    ip_class = ""

    # Extract the first octet of the IP address
    first_octet = int(host_address[0])

    # Determine the IP address class based on the first octet
    if 1 <= first_octet <= 126:
        ip_class = "A"
    elif 128 <= first_octet <= 191:
        ip_class = "B"
    elif 192 <= first_octet <= 223:
        ip_class = "C"
    elif 224 <= first_octet <= 239:
        ip_class = "D"
    return ip_class


def check_private_network(host_address, prefix):
    if '.'.join(host_address[:2]) == '10.0' and prefix >= 8:
        return True
    elif '.'.join(host_address[:2]) == '172.16' and prefix >= 12:
        return True
    elif '.'.join(host_address[:2]) == '192.168' and prefix >= 16:
        return True
    else:
        return False


def decimal_to_binary(octets):
    """
    Converts decimal octets to binary representation.

    Args:
        octets (list): List of decimal octets.

    Returns:
        list: List of binary octets as strings.
    """
    octets_binary = []
    for octet in octets:
        octet = int(octet)
        # Convert the decimal octet to binary and pad with zeros to make it 8 bits
        octets_binary.append(bin(octet)[2:].zfill(8))
    return octets_binary


def calculate_max_hosts(prefix):
    return pow(2, 32 - prefix) - 2


def formatting_list(list_to_format):
    formatted_list = [f"{'.'.join(map(str, sublist))}"
                      if isinstance(sublist, list)
                      else f"{'.'.join(map(str, sublist.split('.')))}"
                      for sublist in list_to_format]
    return formatted_list



if __name__ == '__main__':
    print(process_input('192.168.10.3/24'))