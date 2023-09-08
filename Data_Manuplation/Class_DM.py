class Model:
    title=[]
    subtitle=[]
    subtitlelinks=[]


    def __init__(self,topic):
        self.topic=topic

    def Heading(self, title):
        self.title.append(title)

    def Subheading(self, subtitle):
            self.subtitle.append(subtitle)

    def SubheadingLink(self, subtitlelinks):
        self.subtitlelinks.append(subtitlelinks)

