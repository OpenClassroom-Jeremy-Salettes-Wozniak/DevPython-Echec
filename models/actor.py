class Actor:

    def __init__(self, actor_id, name, description):
        self.actor_id = actor_id
        self.name = name
        self.description = description

    def __str__(self):
        message = "Actor: " + self.name + "\n"
        message += "Description: " + self.description + "\n"
        return message

    def __repr__(self):
        return f"{self.actor_id} {self.name} {self.description}"

    def __eq__(self, other):
        pass