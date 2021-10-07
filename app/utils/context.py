
class Context():

    def __init__( self, activatemenu ):
        self.__ctx = {
            "activemenu": activatemenu
        }

    def setBackward( self, page ):
        self.__ctx["backward"] = page

    def generate( self ):
        return self.__ctx