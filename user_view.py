# View
class UserView:
    def display_user(self, user):
        print(f"User: {user.get_name()}")

    def get_input(self, prompt):
        return input(prompt)