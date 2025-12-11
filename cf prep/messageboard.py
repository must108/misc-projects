
class MessageBoard:
    def __init__(self):
        self.messages = []
        self.time = 1

    def post(self, author, message):
        self.messages.append((self.time, author, message))
        self.time += 1

    def list(self):
        for item in self.messages:
            time, author, message = item
            print(f"{author} sent at {time}: {message}")

    def listK(self, k):
        start = max(0, self.time-1-k)
        for i in range(start, self.time-1):
            time, author, message = self.messages[i]
            print(f"{author} sent at {time}: {message}")

msg = MessageBoard()

msg.post("Mustaeen", "hello world") 
msg.post("Mustaeen", "LMFAO") 

msg.post("Caitlin", "yooo") 
msg.post("Jon", "Wassup") 

msg.post("Abram", "I'm going to call the RA.") 
msg.post("Mustaeen", "nah") 

msg.post("Caitlin", "lmaooooo") 
msg.post("Jon", "LMAOOO")

msg.list()
print("\n")
msg.listK(3)