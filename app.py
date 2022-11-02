import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.0')  # Kivy ver where the code has been tested!


class MyApp(App):
    def build(self):
        self.title = 'APP'
        return Label(text='PB')


if __name__ == '__main__':
    MyApp().run()
