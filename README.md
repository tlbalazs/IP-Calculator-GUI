# IP Calculator Application

This program is an IP Calculator application developed using PySimpleGUI. It allows users to input an IPv4 CIDR block (e.g., "a.b.c.d/n") and calculates various network properties, including the host address, netmask, wildcard mask, network address, first address, last address, and broadcast address.

## main.py

This script serves as the main entry point for the application. It creates a graphical user interface (GUI) using PySimpleGUI elements such as text inputs, buttons, and tables. Users can input a CIDR block and click the "Calculate" button to trigger the calculation of network properties. The calculated results are displayed in a table format.

## ipaddress.py

This module defines a class called `IPv4Cidr`, representing an IPv4 CIDR block. It provides methods to calculate various network properties based on the given CIDR block, including the netmask, network address, first address, wildcard mask, broadcast address, and last address. Additionally, it includes properties to retrieve the full CIDR address, host address, and prefix length.

## functions.py

This module contains utility functions used in the application. These functions handle tasks such as input validation, processing input data, converting decimal octets to binary, determining IP address class, checking for private networks, and formatting lists.
