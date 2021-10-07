import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Your Input')],
            [sg.Multiline(key="input")],
            [sg.Button('Echo'), sg.Button('Cancel')],
            [sg.Text('Output for you')],
            [sg.Output(key="output")]
        ]

# Create the Window
window = sg.Window('Echo GUI', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    # print('You entered ', values[0])
    # values[1] = values[0]
    window.find_element("output")(values["input"])

window.close()
