import socket
import sys
import termios
import tty
import time

class MovementSocket:
    def __init__(self, linear, angular):
        self.linear = linear
        self.angular = angular

    def move(self, sock):
        try:
            sock.send(f"{self.linear} {self.angular}".encode())
            time.sleep(0.1)
        except ConnectionRefusedError:
            print('The bot is not yet connected.')

    @classmethod
    def forward(cls, sock):
        cls(1, 0).move(sock)

    @classmethod
    def backward(cls, sock):
        cls(-1, 0).move(sock)

    @classmethod
    def turn_left(cls, sock):
        cls(0, 1).move(sock)

    @classmethod
    def turn_right(cls, sock):
        cls(0, -1).move(sock)

    @staticmethod
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    @classmethod
    def from_keyboard(cls):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('localhost', 3535))

        while True:
            input = cls.getch()
            if input == "\x1b":  # start of an escape sequence
                input += cls.getch() + cls.getch()
            if input == "\x1b[A":  # up arrow
                cls.forward(sock)
                print('You moved forward')
            elif input == "\x1b[B":  # down arrow
                cls.backward(sock)
                print('You moved backward')
            elif input == "\x1b[D":  # left arrow
                cls.turn_left(sock)
                print('You turned left')
            elif input == "\x1b[C":  # right arrow
                cls.turn_right(sock)
                print('You turned right')
            elif input == "\x03":  # Ctrl+C to exit
                print('Exiting...')
                sock.close()
                break

MovementSocket.from_keyboard()
