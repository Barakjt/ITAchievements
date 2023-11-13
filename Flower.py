# Charde Poole
# 11/12/23
# the code shows a class was created and named Flower. A constructor was used to create the instance of the class flower. Next the attribute and attribute functions were created. The method then starts the execution. Flower1, 2, and 3 are created as well as the class functions. All of the code is then executed.
class Flower:
    def __init__(self, name):
        self.name = name

    def grow(self):
        print("The " +self.name + " is growing.")

    def bloom(self):
        print("The " + self.name + " is blooming.")

def main():
    flower1 = Flower("Rose")
    flower1.grow()
    flower1.bloom()
    flower2 = Flower("Daisy")
    flower2.grow()
    flower2.bloom()
    flower3 = Flower("Carnation")
    flower3.grow()
    flower3.bloom()

if __name__ == "__main__":
  main()