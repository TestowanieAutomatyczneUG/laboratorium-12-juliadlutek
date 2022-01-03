class Subscriber:
    def __init__(self, names=''):
        self.people = names

    def add_person(self, name):
        if name in self.people:
            raise Exception("This person already exist!")
        self.people.append(name)
        return f"Person {name} added to list!"

    def delete_person(self, name):
        if name not in self.people:
            raise Exception("This person doesn't exist!")
        self.people.remove(name)
        return f"Person ${name} deleted from list!"

    def send_message(self, name, message):
        if name not in self.people:
            raise Exception("This person doesn't exist!")
        for person in self.people:
            if person == name:
                return f"Message \"${message}\" sent to ${name}"
