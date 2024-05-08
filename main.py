import PySimpleGUI as sg
import functions
from ipaddress import IPv4Cidr

sg.theme("Black")

label = sg.Text("Add a IPv4 CIDR Block, i.e., a.b.c.d/n")
input_box = sg.InputText(tooltip="Enter a IPv4 address", key="cidr")
calculate_button = sg.Button("Calculate", size=10)
label_ha = sg.Text("Host Address:")
label_netmask = sg.Text("Netmask:")
label_wc = sg.Text("Wildcard:")
label_na = sg.Text("Network Address:")
label_fa = sg.Text("First Address:")
label_la = sg.Text("Last Address:")
label_bc = sg.Text("Broadcast:")
column_layout = sg.Column([[label_ha], [label_netmask], [label_wc], [label_na], [label_fa], [label_la], [label_bc]])
header = ['Host Address', 'Netmask', 'Wildcard', 'Network Address', 'First Address', 'Last Address', 'Broadcast']
rows = []


table = sg.Table(values=rows, headings=header,
                 auto_size_columns=True,
                 display_row_numbers=False,
                 justification='center', key='table',
                 selected_row_colors='red on yellow',
                 enable_events=True,
                 expand_x=True,
                 expand_y=True,
                 enable_click_events=False,
                 num_rows=3,
                 row_height=40,
                 hide_vertical_scroll=True,
                 border_width=5,
                 def_col_width=36
                 )


exit_button = sg.Button("Exit")


window = sg.Window("IP Calculator App",
                   layout=[[label],
                           [input_box, calculate_button],
                           [table],
                           [exit_button]
                           ],
                   font=('Helvetica', 12), size=(2500, 300)
                   )

while True:
    event, values = window.read()
    match event:
        case "Calculate":
            if not functions.check_input(values['cidr']):
                sg.popup("You must follow the IP address dotted-decimal format, such as 192.168.123.234/24!")
                break
            else:
                list_of_elements = functions.process_input(values['cidr'])
                cidr = IPv4Cidr(first_octet=list_of_elements[0], second_octet=list_of_elements[1],
                                third_octet=list_of_elements[2], forth_octet=list_of_elements[3],
                                prefix=list_of_elements[4])

                binary_row = [functions.decimal_to_binary(x) for x in [cidr.get_all_address[i] for i in range(7)]]

                rows.append(functions.format_list(cidr.get_all_address))
                rows.append(functions.format_list(binary_row))
                window['table'].update(values=rows)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()
