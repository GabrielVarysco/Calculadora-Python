class Singleton:
    __instancia = None

    def __novo__(cls):
        if not cls.__instancia:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

s1 = Singleton()
s2 = Singleton()

print(s1 == s2)


