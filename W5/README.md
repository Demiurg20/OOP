# Electronic Device Shopping Cart

## About the Project

This project is a simple electronic store system written in Python using Object-Oriented Programming (OOP).

In this program, customers can:
- See available electronic devices
- Add devices to the shopping cart
- Remove devices from the cart
- Checkout and buy devices

The system also manages device stock and reduces the stock after purchase.

---

## OOP Concepts Used

This project demonstrates:

- Inheritance
- Polymorphism
- Classes and Objects
- Method overriding
- Encapsulation

---

## Classes in the Project

### 1. Device (Base Class)

This is the parent class for all devices.

Common attributes:
- name
- price
- stock
- warranty_period

Common methods:
- display_info()
- apply_discount()
- is_available()
- reduce_stock()

---

### 2. Smartphone (Child Class)

Extra attributes:
- screen_size
- battery_life

Extra methods:
- make_call()
- install_app()

---

### 3. Laptop (Child Class)

Extra attributes:
- ram_size
- processor_speed

Extra methods:
- run_program()
- use_keyboard()

---

### 4. Tablet (Child Class)

Extra attributes:
- screen_resolution
- weight

Extra methods:
- browse_internet()
- use_touchscreen()

---

### 5. Cart Class

This class manages the shopping cart.

Functions:
- Add devices to cart
- Remove devices from cart
- Show total price
- Checkout and reduce stock

---

## How to Run the Program

1. Make sure Python 3 is installed.
2. Open terminal in the project folder.
3. Run:
    ***python main.py***
4. Use the menu to interact with the store.

---

## Menu Options

1. Show Devices  
2. Add Device to Cart  
3. Show Cart  
4. Remove from Cart  
5. Checkout  
6. Exit  

---

## Sample Run

Show Devices

Add Device to Cart

Show Cart

Remove from Cart

Checkout

Exit

Choose option: 1
iPhone 14 | $999.00 | Stock: 10 | Warranty: 24 months | Screen: 6.1" | Battery: 20h
...


---

## UML Diagram

The UML diagram is included in the file:

W5.drawio.png

It shows:
- Base class (Device)
- Child classes (Smartphone, Laptop, Tablet)
- Cart class
- Relationships between classes

---

## Author

Islambek Asylbekov