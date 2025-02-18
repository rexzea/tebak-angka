from kivy.lang import Builder
from kivymd.app import MDApp
import random



KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    MDLabel:
        text: "🎮 Game Tebak Angka (1-10)"
        theme_text_color: "Primary"
        font_style: "H5"
        halign: "center"

    MDLabel:
        id: label_kesempatan
        text: "Kesempatan: 5"
        font_style: "Subtitle1"
        halign: "center"

    MDTextField:
        id: input_tebakan
        hint_text: "Masukkan angka"
        helper_text: "Tebak angka antara 1-10"
        helper_text_mode: "on_focus"
        font_size: "18sp"
        size_hint_x: None
        width: 250
        pos_hint: {"center_x": 0.5}

    MDRaisedButton:
        text: "Cek Tebakan"
        pos_hint: {"center_x": 0.5}
        on_release: app.cek_tebakan()

    MDLabel:
        id: label_hasil
        text: ""
        font_style: "H6"
        halign: "center"

    MDRaisedButton:
        text: "Restart Game"
        pos_hint: {"center_x": 0.5}
        on_release: app.restart_game()
        md_bg_color: 1, 0, 0, 1  # Warna merah
'''



class TebakAngkaApp(MDApp):
    def build(self):
        self.angka_rahasia = random.randint(1, 10)
        self.kesempatan = 5  # batas tebakan
        return Builder.load_string(KV)

    def cek_tebakan(self):
        try:
            tebakan = int(self.root.ids.input_tebakan.text)

            if tebakan == self.angka_rahasia: # jika tebakan benar
                self.root.ids.label_hasil.text = "🎉 Benar! Kamu menang!"
                self.root.ids.label_hasil.theme_text_color = "Custom"
                self.root.ids.label_hasil.text_color = (0, 1, 0, 1)  # hijau


            else: # jika tebakan salah
                self.kesempatan -= 1
                self.root.ids.label_kesempatan.text = f"Kesempatan: {self.kesempatan}"

                if self.kesempatan == 0: # jika kesempatan habis
                    self.root.ids.label_hasil.text = "❌ Game Over! Jawabannya: " + str(self.angka_rahasia)
                    self.root.ids.label_hasil.theme_text_color = "Custom"
                    self.root.ids.label_hasil.text_color = (1, 0, 0, 1)  # merah

 
                elif tebakan < self.angka_rahasia: # jika tebakan terlalu kecil
                    self.root.ids.label_hasil.text = "📉 Terlalu kecil!"
                    self.root.ids.label_hasil.text_color = (1, 0.5, 0, 1)  # oren
                else:
                    self.root.ids.label_hasil.text = "📈 Terlalu besar!"
                    self.root.ids.label_hasil.text_color = (0, 0, 1, 1)  # biru

        except ValueError:
            self.root.ids.label_hasil.text = "⚠️ Masukkan angka yang valid!"
            self.root.ids.label_hasil.text_color = (1, 0.5, 0, 1)  # oren

    def restart_game(self):
        self.angka_rahasia = random.randint(1, 10)
        self.kesempatan = 5
        self.root.ids.label_hasil.text = ""
        self.root.ids.label_kesempatan.text = "Kesempatan: 5"
        self.root.ids.input_tebakan.text = ""

if __name__ == "__main__":
    TebakAngkaApp().run()
