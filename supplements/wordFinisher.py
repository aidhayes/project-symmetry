import PySimpleGUI as sg

lst = sorted([
    'Global', 'USA', 'India', 'Brazil', 'Russian', 'France', 'UK', 'Italy',
    'Spain', 'Germany', 'Colombia', 'Argentina', 'Mexico', 'Turkey', 'Poland',
    'Iran', 'Ukraine', 'South Africa', 'Peru', 'Netherlands', 'Alaska'])
width = max(map(len, lst)) + 2

font = ("Courier New", 16)
sg.theme("DarkBlue3")
sg.set_options(font=font)

layout = [[sg.Combo(lst, size=(width, 5), key='COMBO'), sg.Button('Exit')]]
window = sg.Window("COMBO", layout, finalize=True)
combo = window['COMBO']
combo.bind('<Key>', ' Key')
combo.bind('<Enter>', ' Enter')
user_event = False

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'COMBO Enter':
        combo.Widget.select_range(0, 'end')
    elif event == 'COMBO Key':
        entry = values['COMBO'].lower()
        if user_event:
            user_event = False
        else:
            if entry:
                index = None
                for i, item in enumerate(lst):
                    if item.lower().startswith(entry):
                        index = i
                        break
                if index is not None:
                    user_event = True
                    combo.Widget.set(lst[index])
                    combo.Widget.event_generate('<Key-Down>')
                    combo.Widget.current(index)

    print(event, values)

window.close()