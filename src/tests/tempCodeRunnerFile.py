\nYou: ")

    if command.lower() == "exit":
        break

    result = route_command(command)

    print("\nRouter:")
    print(result)