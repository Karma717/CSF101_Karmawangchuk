def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("BoB")

def calculate_rectangle_area(width, height):
    return width * height
area = calculate_rectangle_area(5, 3)
print(f"The area of rectangle is: {area}")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=20, city= "New york")

def min_max(numbers):
    return min(numbers), max(numbers)
results = min_max([5, 2, 8, 1, 9,])
print(f"Min: {results[0]}, max: {results[1]}")

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by Zero"
    return a/b
print(safe_divide(10, 2))
print(safe_divide(5, 0))

