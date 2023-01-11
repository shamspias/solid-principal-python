class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]


class PersistenceManager:
    def save_to_file(self, journal, filename):
        file = open(filename, "w")
        file.write("\n".join(journal.entries))
        file.close()


# Client code
j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")

p = PersistenceManager()
filename = "journal.txt"
p.save_to_file(j, filename)

print(f"Journal entries saved to {filename}.")
