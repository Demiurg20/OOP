import random
from shape3d import Sphere, Cylinder, Cube


def generate_random_shape():
    shape_type = random.choice(["sphere", "cylinder", "cube"])

    if shape_type == "sphere":
        radius = random.randint(1, 10)
        return Sphere(radius)

    elif shape_type == "cylinder":
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        return Cylinder(radius, height)

    else:
        side = random.randint(1, 10)
        return Cube(side)


def main():
    shapes = []

    # Generate 10 random shapes
    for _ in range(10):
        shapes.append(generate_random_shape())

    # Display information
    print("=== 3D Shapes Information ===\n")

    for shape in shapes:
        print(shape)
        print(f"Surface Area: {shape.surface_area():.2f}")
        print(f"Volume: {shape.volume():.2f}")
        print("-" * 30)


if __name__ == "__main__":
    main()