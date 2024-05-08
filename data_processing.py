# import functions
#
# host_address = []
# prefix = 0
#
#
# def process_input(cidr):
#     global host_address
#     global prefix
#     host_address, prefix = functions.process_input(cidr)
#
#
# def calculate_values():
#     global host_address, prefix
#     ip_class = functions.check_ip_class(host_address)
#     is_private_network = functions.check_private_network(host_address, prefix)
#     netmask = functions.calculate_netmask(prefix)
#     wildcard = functions.calculate_wildcard_mask(netmask)
#     network_address = functions.calculate_network_address(host_address, netmask)
#     first_address = functions.calculate_first_address(network_address)
#     broadcast = functions.calculate_broadcast_address(network_address, wildcard)
#     last_address = functions.calculate_last_address(broadcast)
#     host_address_binary = functions.decimal_to_binary(host_address)
#     max_hosts = functions.calculate_max_hosts(prefix)
#
#     netmask_binary = functions.decimal_to_binary(netmask)
#     network_address_binary = functions.decimal_to_binary(network_address)
#     first_address_binary = functions.decimal_to_binary(first_address)
#     last_address_binary = functions.decimal_to_binary(last_address)
#     broadcast_binary = functions.decimal_to_binary(broadcast)
#     wildcard_binary = functions.decimal_to_binary(wildcard)
#
#     decimal_list = [host_address, netmask, wildcard, network_address,
#                     first_address, last_address, broadcast]
#     binary_list = [host_address_binary, netmask_binary, wildcard_binary, network_address_binary,
#                    first_address_binary, last_address_binary, broadcast_binary]
#     return decimal_list, binary_list
#
#
# def formatting_list(list_to_format):
#     formatted_list = [f"{'.'.join(map(str, sublist))}"
#                       if isinstance(sublist, list)
#                       else f"{'.'.join(map(str, sublist.split('.')))}"
#                       for sublist in list_to_format]
#     return formatted_list
