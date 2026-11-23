def force(mass, acceleration):
    return mass * acceleration

def velocity(distance, time):
    return distance / time

def momentum(mass, velocity):
    return mass * velocity

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def work_done(force, distance):
    return force * distance


# Using while loop
choice = 1

while choice <= 5:
    if choice == 1:
        print("Force =", force(10, 5), "N")

    elif choice == 2:
        print("Velocity =", velocity(100, 20), "m/s")

    elif choice == 3:
        print("Momentum =", momentum(10, 5), "kg m/s")

    elif choice == 4:
        print("Kinetic Energy =", kinetic_energy(10, 5), "J")

    elif choice == 5:
        print("Work Done =", work_done(20, 10), "J")

    choice += 1