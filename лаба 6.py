class Lamps:
    className = 'Lamps'
    count = 0

    def __init__(self, name, power, energy_consumption, service_life):
        self.name = name
        self.power = power
        self.consumption = energy_consumption
        self.service_life = service_life
        Lamps.count += 1
    def get_name(self):
        return self.name
    
    def set_name(self, n):
        self.name = n

    def get_power(self):
        return self.power

    def set_power(self, power):
        if power > 0:
            self.power = power
        else:
            self.power = 1

    def get_consump(self):
        return self.consumption

    def set_consump(self, energy_consumption):
        if energy_consumption > 0:
            self.consumption = energy_consumption
        else:
            self.consumption = 0.25

    def get_service_life(self):
        return self.service_life

    def set_service_life(self, service_life):
        if service_life > 0:
            self.service_life = service_life
        else:
            self.service_life = 0.25

    def info(self):
        print(self.name)
        print(f"Мощность излучения: {self.power} Вт")
        print(f'Потребление энергии: {self.consumption} Вт')
        print(f"Срок службы: {self.service_life} г.")

    # через сколько дней лампа перегорит при работе 8 часов в сутки
    def Days(self):
        print(f'лампа перегорит через {self.service_life * 365 * 3} дней')


class Searchlight (Lamps):
    className = 'Searchlight'

    def __init__(self, name, power, energy_consumption, service_life, colour):
        super().__init__(name, power, energy_consumption, service_life)
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_colour(self, colour_len):
        if 540 > colour_len > 460:
            self.colour = 'нейтральный'
        elif colour_len > 540:
            self.colour = 'желтый'
        else:
            self.colour = "Белый"

    def info(self):
        super().info()
        print(f'Тип: {Searchlight.className}')
        print(f"Цвет: {self.height}")

     # через сколько дней лампа перегорит при работе 8 часов в сутки
    def Days(self):
        print(f'лампа перегорит через {self.service_life * 365 * 3} дней')
       

class Daylamp (Lamps):
    className = 'Daylamp'

    def __init__(self, name, power, energy_consumption, service_life, colour):
        super().__init__(name, power, energy_consumption, service_life)
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_colour(self, colour_len):
        if 540 > colour_len > 460:
            self.colour = 'нейтральный'
        elif colour_len > 540:
            self.colour = 'желтый'
        else:
            self.colour = "Белый"

    def info(self):
        super().info()
        print(f'Тип: {Daylamp.className}')
        print(f"Цвет: {self.height}")

    # cоотношение мощности излучения к энергопотреблению
    def ratio(self):
        print(f'Отношение мощности к энергопотреблению {self.power/self.consumption}')

a = Lamps( Lamps.className, 50, 60, 3)
a.info()
a.Days()

print('\n')

light = Searchlight(Searchlight.className, 140, 150, 4, 500 )
dayl = Daylamp(Daylamp.className, 70, 80, 2, 450)

light.Days()
dayl.ratio()
    
print(f'Objects count {Lamps.count}')