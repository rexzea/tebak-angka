import random
import math

class RexzeaGuessNumber:
    def __init__(self):
        self.max_number = 100
        self.attempts = 0

    def player_vs_ai_mode(self):
        print("\n--- Mode: Player vs Advanced AI (Bersama-sama Menebak) ---")
        target_number = random.randint(1, self.max_number)
        self.attempts = 0
        player_guess = None
        ai_guess = None

        possible_numbers = set(range(1, self.max_number + 1))

        while player_guess != target_number or ai_guess != target_number:
            self.attempts += 1
            
            while True:
                try:
                    player_guess = int(input(f"Tebakan Anda (1-{self.max_number}): "))
                    if 1 <= player_guess <= self.max_number:
                        break
                    else:
                        print(f"Mohon masukkan angka antara 1 dan {self.max_number}.")
                except ValueError:
                    print("Masukkan angka yang valid!")

            if not ai_guess:
                ai_guess = random.choice(list(possible_numbers))
            else:
                if ai_guess < target_number:
                    possible_numbers = {n for n in possible_numbers if n > ai_guess}
                elif ai_guess > target_number:
                    possible_numbers = {n for n in possible_numbers if n < ai_guess}
                
                if possible_numbers:
                    ai_guess = min(possible_numbers, key=lambda x: abs(x - math.floor(self.max_number/2)))
            
            if player_guess < target_number:
                print("Tebakan kamu terlalu kecil!")
            elif player_guess > target_number:
                print("Tebakan kamu terlalu besar!")
            else:
                print(f"Selamat! kamu menebak dengan benar di percobaan ke-{self.attempts}!")

            if ai_guess < target_number:
                print("Tebakan AI terlalu kecil!")
            elif ai_guess > target_number:
                print("Tebakan AI terlalu besar!")
            else:
                print(f"AI menebak dengan benar di percobaan ke-{self.attempts}!")

            if player_guess == target_number and ai_guess == target_number:
                break

        print(f"Angka yang benar adalah: {target_number}")
        print(f"Total percobaan: {self.attempts}")

    def player_guess_ai_number(self):
        print("\n--- Mode: Player Menebak Angka AI ---")
        target_number = random.randint(1, self.max_number)
        self.attempts = 0

        while True:
            self.attempts += 1
            try:
                player_guess = int(input(f"Tebakan kamu (1-{self.max_number}): "))
                
                if player_guess < target_number:
                    print("Tebakan kamu terlalu kecil!")
                elif player_guess > target_number:
                    print("Tebakan kamu terlalu besar!")
                else:
                    print(f"Selamat! kamu menebak dengan benar di percobaan ke-{self.attempts}!")
                    break
            except ValueError:
                print("Masukkan angka yang valid!")

        print(f"Angka yang benar adalah: {target_number}")

    def ai_guess_player_number(self):
        print("\n--- Mode: AI Menebak Angka Player ---")
        print("Silakan pilih angka rahasia antara 1 dan 100.")
        
        self.attempts = 0
        left, right = 1, self.max_number
        possible_numbers = set(range(1, self.max_number + 1))
        
        while True:
            self.attempts += 1
            
            ai_guess = (left + right) // 2
            
            print(f"AI menebak: {ai_guess}")
            
            while True:
                feedback = input("Tekan 'B' jika lebih besar, 'K' jika lebih kecil, 'Y' jika benar: ").lower()
                
                if feedback == 'b':
                    left = ai_guess + 1
                    possible_numbers = {n for n in possible_numbers if n > ai_guess}
                    break
                elif feedback == 'k':
                    right = ai_guess - 1
                    possible_numbers = {n for n in possible_numbers if n < ai_guess}
                    break
                elif feedback == 'y':
                    print(f"AI berhasil menebak di percobaan ke-{self.attempts}!")
                    return
                else:
                    print("Input tidak valid. Gunakan 'B', 'K', atau 'B'.")
            if not possible_numbers:
                print("Terjadi kesalahan dalam input. Mohon ulangi.")
                break

    def main_menu(self):
        while True:
            print("\n--- TEBAK ANGKA AI ---")
            print("1. Player vs AI (Bersama-sama Menebak)")
            print("2. Player Menebak Angka AI")
            print("3. AI Menebak Angka Player")
            print("4. Keluar")
            
            try:
                choice = int(input("Pilih mode permainan (1-4): "))
                
                if choice == 1:
                    self.player_vs_ai_mode()
                elif choice == 2:
                    self.player_guess_ai_number()
                elif choice == 3:
                    self.ai_guess_player_number()
                elif choice == 4:
                    print("Terima kasih telah bermain!")
                    break
                else:
                    print("Pilihan tidak valid. Mohon pilih 1-4.")
            except ValueError:
                print("Masukkan angka yang valid!")

def main():
    game = RexzeaGuessNumber()
    game.main_menu()

if __name__ == "__main__":
    main()
