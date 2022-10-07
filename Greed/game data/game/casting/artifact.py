from game.casting.actor import Actor

class Artifact(Actor):

    def __init__(self):
        super().__init__()
        self._points = 0
        

    def get_points(self):
        if (self.get_text() == '+'):
            self._points = 1
        elif (self.get_text() == "[']"):
            self._points = 2
        elif (self.get_text() == '[,]'):
            self._points = -2
        else:
            self._points = -1
        
        return self._points