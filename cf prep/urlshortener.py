
class URLShortener:
    def __init__(self):
        self.urls = {}
        self.id = 0

    def create(self, url):
        code = self.id
        self.urls[code] = url
        self.id += 1
        return code
    
    def resolver(self, code):
        if code in self.urls:
            return self.urls[code]
        else:
            return None
        
url = URLShortener()
code = url.create("https://mustaeen.dev")
print(url.resolver(code))
