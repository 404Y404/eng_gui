from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config
from CreateText import CreateText


Config.set('kivy', 'keyboard_mode', 'systemanddock')


#Window.size = (240, 425)


class Container(BoxLayout):
    def gen(self):
        try:
            CreateText(self.text_field.text)
            with open("ReadyWord.txt", "r") as file:
                self.answer.text = file.read()

        except Exception as e:
            self.answer.text = "Eror!" + str(e)


class MyApp(App):

    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
