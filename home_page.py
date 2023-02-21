from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import random, time
from multiprocessing import Process

Builder.load_file("home_page.kv")

number = ["1", "2", "3", "4", "5"]
color = ["red", "green", "blue"]
number_list = []

kart = ["kart1", "kart2", "kart3", "kart4", "kart5"]
selected_list = ["selected1", "selected2", "selected3"]
selected_remove = []

class Home_page(Screen):
    def start(self):
        self.data = 0
        if len(number_list) < 6:
            index = 0
            for i in kart:
                x = random.choice(number)
                y = random.choice(color)
                number.remove(x)
                number_list.append(x)

                button = Button(on_press=self.remove)
                button.my_id = i
                button.text = number_list[index]
                button.background_color = "red"
                self.ids[i].add_widget(button)
                index += 1
        print(number_list)

    def remove(self, id):
        self.ids[id.my_id].remove_widget(id)
        self.ids[selected_list[self.data]].add_widget(id)
        selected_remove.append(id)
        self.data += 1
        if len(selected_remove) == 3:
            if selected_remove[0].text == "1" and selected_remove[1].text == "2" and selected_remove[2].text == "3":
                data = 0
                for i in range(3):
                    self.ids[selected_list[data]].remove_widget(selected_remove[data])
                    data += 1
                selected_list.clear()
                for x in range(3):
                    x+=1
                    selected_list.append("selected{}".format(x))
                self.data = 0
