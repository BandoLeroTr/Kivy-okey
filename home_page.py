from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
import random

Builder.load_file("home_page.kv")
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
number_list = []

card = []
control_cart = []
selected_list = ["selected0", "selected1", "selected2"]
selected_remove = []
selected_remove_text = []

class Home_page(Screen):
    def debug(self):
        print(control_cart)
    def start(self, starter):
        if starter == "start_button1":
            for index in range(5):
                x = random.choice(number);number.remove(x);number_list.append(x)
                button = Button(on_press=self.remove);button.my_id = "card"+str(index);button.text = number_list[index]
                button.background_color = "red";button.font_size = "150";self.ids["card"+str(index)].add_widget(button)
                card.append(button.my_id)

            self.ids.start_boxlayout.remove_widget(self.ids.start_button1)
            self.start_button2 = Button(on_press=lambda x:self.start("start_button2"))
            self.start_button2.text="Card"

            self.ids.start_boxlayout.add_widget(self.start_button2)
            self.query()
            self.info()

        if starter == "start_button2":
            number_list.clear()

            for index in range(len(control_cart)):
                if not number:
                    self.start_button2.disabled = True
                    break
                x = random.choice(number);number.remove(x);number_list.append(x)
                button = Button(on_press=self.remove);button.my_id = control_cart[index];button.text = number_list[index]
                button.background_color = "red";button.font_size = "150";self.ids[control_cart[index]].add_widget(button)
                card.append(control_cart[index]);card.sort()

            control_cart.clear()
            self.query();self.info()

    def query(self):
        if len(card) == 5:
            self.start_button2.disabled = True
        if len(card) < 5:
            self.start_button2.disabled = False

    def remove(self, id):
        if len(selected_list) >  0:
            self.info();card.remove(id.my_id);self.query()
            control_cart.append(id.my_id);control_cart.sort()#5 buttondan seçtiğimiz butonu listeye ekliyor
            self.ids[id.my_id].remove_widget(id)#5 buttondan seçileni silme
            self.ids[selected_list[0]].add_widget(id) #5 buttondan seçileni aşağıya ekleme
            selected_remove.append(id)
            selected_list.pop(0) #3 button listesindeki 0. elemanı siliyor

            selected_remove_text.append(id.text)
            selected_remove_text.sort()
            self.info()
        if len(selected_remove_text) == 3:
            self.info()
            try:
                if selected_remove_text[0] == "1" and selected_remove_text[1] == "2" and selected_remove_text[2] == "3":
                    self.selected_remove()
                if selected_remove_text[0] == "2" and selected_remove_text[1] == "3" and selected_remove_text[2] == "4":
                    self.selected_remove()
                if selected_remove_text[0] == "3" and selected_remove_text[1] == "4" and selected_remove_text[2] == "5":
                    self.selected_remove()
                if selected_remove_text[0] == "4" and selected_remove_text[1] == "5" and selected_remove_text[2] == "6":
                    self.selected_remove()
                if selected_remove_text[0] == "5" and selected_remove_text[1] == "6" and selected_remove_text[2] == "7":
                    self.selected_remove()
                if selected_remove_text[0] == "6" and selected_remove_text[1] == "7" and selected_remove_text[2] == "8":
                    self.selected_remove()
                if selected_remove_text[0] == "7" and selected_remove_text[1] == "8" and selected_remove_text[2] == "9":
                    self.selected_remove()
                if selected_remove_text[0] == "1" and selected_remove_text[1] == "1" and selected_remove_text[2] == "1":
                    self.selected_remove()
                if selected_remove_text[0] == "2" and selected_remove_text[1] == "2" and selected_remove_text[2] == "2":
                    self.selected_remove()
                if selected_remove_text[0] == "3" and selected_remove_text[1] == "3" and selected_remove_text[2] == "3":
                    self.selected_remove()
                if selected_remove_text[0] == "4" and selected_remove_text[1] == "4" and selected_remove_text[2] == "4":
                    self.selected_remove()
                if selected_remove_text[0] == "5" and selected_remove_text[1] == "5" and selected_remove_text[2] == "5":
                    self.selected_remove()
                if selected_remove_text[0] == "6" and selected_remove_text[1] == "6" and selected_remove_text[2] == "6":
                    self.selected_remove()
                if selected_remove_text[0] == "7" and selected_remove_text[1] == "7" and selected_remove_text[2] == "7":
                    self.selected_remove()
                if selected_remove_text[0] == "8" and selected_remove_text[1] == "8" and selected_remove_text[2] == "8":
                    self.selected_remove()
                if selected_remove_text[0] == "9" and selected_remove_text[1] == "9" and selected_remove_text[2] == "9":
                    self.selected_remove()
            except:
                pass
    def selected_remove(self):
        for i in range(3):
            self.ids["selected"+str(i)].remove_widget(selected_remove[i])
            selected_list.append("selected"+str(i))
        selected_remove.clear();number_list.clear();selected_remove_text.clear()
        self.info()

    def info(self):
        print("number",len(number),number)
        print("number_list",len(number_list),number_list)
        print("card",len(card),card)
        print("control_cart",len(control_cart), control_cart)
        print("selected_list",len(selected_list),selected_list)
        print("selected_remove",len(selected_remove),selected_remove)
        print("selected_remove_text",len(selected_remove_text),selected_remove_text)
        print("--------------------------------------------------")
