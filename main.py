from pet import Pet

def main():
    print("🐾 Welcome to the Digital Pet Simulator! 🐾")
    name = input("What's your pet's name? ")
    my_pet = Pet(name)

    while True:
        print("\nWhat would you like to do?")
        print("1. 🦴 Feed your pet")
        print("2. 😴 Let your pet sleep")
        print("3. 🎾 Play with your pet")
        print("4. 🎓 Teach your pet a trick")
        print("5. 📋 Show pet's tricks")
        print("6. 📶 Check pet's status")
        print("7. ➡️ Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            my_pet.eat()
            print(f"You fed {my_pet.name}.")
        elif choice == "2":
            my_pet.sleep()
            print(f"{my_pet.name} had a good rest.")
        elif choice == "3":
            my_pet.play()
            print(f"You played with {my_pet.name}.")
        elif choice == "4":
            trick = input("What trick would you like to teach your pet? ")
            my_pet.train(trick)
        elif choice == "5":
            my_pet.show_tricks()
        elif choice == "6":
            my_pet.get_status()
        elif choice == "7":
            print(f"Goodbye! {my_pet.name} will miss you! 🐶")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 7.")

        input("Press Enter to continue...") 

if __name__ == "__main__":
    main()