class Colour:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\x1b[37m'

    def getHeader(self):
        return self.HEADER

    def getOkBlue(self):
        return self.OKBLUE

    def getOkGreen(self):
        return self.OKGREEN

    def getWarning(self):
        return self.WARNING

    def getFail(self):
        return self.FAIL

    def getEnd(self):
        return self.ENDC

    def getBold(self):
        return self.BOLD

    def getUnderline(self):
        return self.UNDERLINE

    def getWhite(self):
        return self.WHITE
