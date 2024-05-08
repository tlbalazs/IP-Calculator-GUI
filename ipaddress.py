class IPv4Cidr:
    def __init__(self, first_octet, second_octet, third_octet, forth_octet, prefix):
        self.first_octet = first_octet
        self.second_octet = second_octet
        self.third_octet = third_octet
        self.forth_octet = forth_octet
        self.prefix = prefix

    @property
    def full_cidr_address(self):
        return f'{self.first_octet}.{self.second_octet}.{self.third_octet}.{self.forth_octet}/{self.prefix}'

    @property
    def get_host_address(self):
        return f'{self.first_octet}.{self.second_octet}.{self.third_octet}.{self.forth_octet}'

    @property
    def get_prefix(self):
        return f'{self.prefix}'

    @property
    def get_all_address(self):
        return [self.get_host_address_list(), self.calculate_netmask(), self.calculate_wildcard_mask(),
                self.calculate_network_address(), self.calculate_first_address(), self.calculate_last_address(),
                self.calculate_broadcast_address()]

    def get_host_address_list(self):
        return [int(self.first_octet), int(self.second_octet), int(self.third_octet), int(self.forth_octet)]

    def calculate_netmask(self):
        """
        Calculates the netmask value based on the given prefix.

        Args:
            prefix (int): The prefix length.

        Returns:
            list: The netmask value as a list of four octets.
        """
        netmask = []
        for index in range(4):
            # Determine the value for the current octet based on the prefix
            if index < int(self.prefix) // 8:
                netmask.append(255)
            else:
                # Calculate the value for the remaining bits in the current octet
                netmask.append(256 - pow(2, 8 - (int(self.prefix) % 8)))
                # Reset prefix to zero for the remaining octets
                prefix = 0
        return netmask

    def calculate_network_address(self):
        network_address = [0, 0, 0, 0]
        for index in range(4):
            network_address[index] = (int(self.get_host_address_list()[index]) & int(self.calculate_netmask()[index]))
        return network_address

    def calculate_first_address(self):
        first_address = [0, 0, 0, 0]
        for index in range(4):
            first_address[index] = self.calculate_network_address()[index]
            if index == 3:
                first_address[index] = int(self.calculate_network_address()[index]) + 1
        return first_address

    def calculate_wildcard_mask(self):
        """
        Calculates the wildcard mask based on the provided netmask.

        Args:
            netmask (list): The netmask value as a list of four octets.

        Returns:
            list: The wildcard mask as a list of four octets.
        """
        wildcard = [0, 0, 0, 0]
        # Calculate the wildcard mask for each octet
        for index in range(4):
            # Use bitwise operations to calculate the wildcard mask
            wildcard[index] = (1 << 8) - 1 - int(self.calculate_netmask()[index])
        return wildcard

    def calculate_broadcast_address(self, host=None, wildcard=None):
        if wildcard is None:
            wildcard = self.calculate_wildcard_mask()
        if host is None:
            host = self.get_host_address_list()
        broadcast = []
        for h, w in zip(host, wildcard):
            broadcast.append(int(h) | w)
        return broadcast

    def calculate_last_address(self, broadcast=None):
        if broadcast is None:
            broadcast = self.calculate_broadcast_address()
        last_address = broadcast.copy()
        last_address[3] = last_address[3] - 1
        return last_address


if __name__ == '__main__':
    cidr_address = IPv4Cidr('192', '168', '10', '54', '24')
    print(cidr_address.full_cidr_address)
    print(cidr_address.calculate_netmask())
    print(cidr_address.calculate_network_address())
    print(cidr_address.calculate_first_address())
    print(cidr_address.calculate_wildcard_mask())
    print(cidr_address.calculate_broadcast_address())
    print(cidr_address.calculate_last_address())
    print(cidr_address.get_all_address)
