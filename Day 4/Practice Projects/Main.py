class Bank:
    def __init__(self,name,balance,account_number):
        self.name=name
        self.balance=balance
        self.account_number=account_number
        
    def get_info(self):
        print(f"Name: {self.name}\nAccount Number: {self.account_number}\nBalance: {self.balance}")
    
bank1=Bank("Shayan",100_000,"PK0001")
bank1.get_info()

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        print("\nBook Title :", self.title)
        print("Author :", self.author)
        print("\nReviews:")

        if len(self.reviews) == 0:
            print("No reviews available.")
        else:
            for i, review in enumerate(self.reviews, start=1):
                print(f"{i}. {review}")


# Create Object
book1 = Book("Python Programming", "Shayan Hassan")

# Add Reviews
book1.add_review("Excellent Book")
book1.add_review("Easy to Understand")
book1.add_review("Best for Beginners")

# Display Reviews
book1.display_reviews()

# Count Reviews
print("\nTotal Reviews:", book1.count_reviews())

class Shape:

    def area(self):
        print("Area method of Shape")


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle:", self.length * self.width)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle:", 3.14 * self.radius * self.radius)


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Area of Triangle:", 0.5 * self.base * self.height)


# Objects
rectangle = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(8, 6)

# Call area() method
rectangle.area()
circle.area()
triangle.area()