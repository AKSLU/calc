from core import calc

def test():
    assert calc("3 + 5") == 8
    assert calc("10 - 2") == 8
    assert calc("4 * 2") == 8
    assert calc("16 / 2") == 8
    assert calc("2 / 0") == "no / 0"
    print("no problem")

if __name__ == "__main__":
    test()
