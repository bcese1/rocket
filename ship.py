class Ship:  # creates a new object class (general object)
    def __init__(self, x, y, health=100):  # initializes the object with the following parameters
        self.x = x  # ship movement on x-axis
        self.y = y  # ship movement on y-axis
        self.health = health  # health of ship
        self.ship_img = None  # image of ship, defined as none so other classes can add different pictures
        self.bullets_img = None  # image of bullets, defined as none so other classes can add different pictures
        self.bullets = []  # creates a list for bullets
        self.bullet_cd = 0  # cooldown on shooting bullets

    def draw(self, window):  # defines a function draw which will draw the ship on the window
        window.blit(self.ship_img, (self.x, self.y))  # draws ship_img on the window at x,y position

    def get_width(self):  # defines a function get_width which will return the width
        return self.ship_img.get_width()  # returns ship_img width in pixels

    def get_height(self):  # defines a function get_height which will return the height
        return self.ship_img.get_height()  # returns ship_img height in pixels

