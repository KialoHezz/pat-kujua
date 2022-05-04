class Sources:
    '''
    Sources  class to define Source objects
    '''
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description
        


class Articles:
    '''
    Articles  class to define Articles objects
    '''
    def __init__(self,author,title,urlToImage,description,publishedAt):
        self.author = author
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt
