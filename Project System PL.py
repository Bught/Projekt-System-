#__Autor__ = Bught
print("")
print("witaj w Mojim Projekcie System")
print("Tu możesz wpisać dowolny login i hasło")
print("Ps: do niczgo mie można wykorzystać tech haseł ponieważ ten program powstał w języku python w"
      " celach chumorystycznych oraz na ocene i nie ma połączenia z internetem")
print("")
print("Podaj Login Do Systemu lub aby się zarejestrować ")
user_name = input()
print("Podaj Hasło")
has_lo = input()
print("")
if has_lo == has_lo:
    while 3>2:
        print("Analizowanie Tożsamości. Login do konta: " +user_name)
        break
print("Wysyłanie danych do servera")
print("")
print("Ping Servera 2")
print("")
print("Potwirdz tożmość wpsując ponownie hasło")
log_on = input("Podaj hasło ponownie: ")
if log_on == has_lo:
    print("Logowanie Się Powiodło")
    print("")
    print("Proszę Czekać")
    print("")
    print("łączenie z bazą danych")
    print("")
    print("!Wszystko gotowe!")
    input()
else:
    print("")
    print("logowanie NIE powiodło sie wyłącz Konsolę aby się Połączyć ponownie")
    input()
