class Cat:
    
    def __init__(self):
        self.arm_len = 12.0
        self.leg_len = 14.0
        self.num_eyes = 2
        self.tail = True
        self.furry = True
        
    def member(self):
        print("The length of a cat's front leg is", self.arm_len, "inches.")
        print("The length of a cat's hind leg is", self.leg_len, "inches.")
        print("A cat has", self.num_eyes, "eyes.")
        print("A cat has a tail:", self.tail)
        print("A cat has fur:", self.furry)
def main():
    c = Cat()
    c.member()
    
if __name__ == "__main__":
    main()