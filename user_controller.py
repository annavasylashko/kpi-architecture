# Controller
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_user_name(self, name):
        self.model.set_name(name)

    def handle_user_input(self):
        while True:
            command = self.view.get_input("Enter a command (update, display, exit): ")
            if command == "update":
                name = self.view.get_input("Enter the new name: ")
                self.update_user_name(name)
            elif command == "display":
                self.view.display_user(self.model)
            elif command == "exit":
                break
            else:
                print("Invalid command. Please try again.")
