def make_division_by(n):
    def division(x: int) -> float:
        assert n > 0, "El valor ingresado en el divisor debe ser mayor a cero"
        return round(x/n, 2)
    return division

def run():
    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    division_by_18 = make_division_by(18)
    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))
    print(division_by_3(division_by_5(200)))

if __name__ == "__main__":
    run()