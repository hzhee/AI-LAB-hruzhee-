def vacuum_cleaner(environment):

    for room in environment:

        print("Vacuum is at Room", room)

        if environment[room] == "dirty":

            print("Cleaning Room", room)

            environment[room] = "clean"

        else:

            print("Room", room, "is already clean")

    print("\nAll rooms are clean!")


environment = {
    "A": "dirty",
    "B": "dirty"
}


vacuum_cleaner(environment)