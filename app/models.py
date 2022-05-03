class Sources:
    '''
    Sources  class to define Source objects
    '''
    def __init__(self,id, name,urlToImage,description,publishedAt):
        self.id = id
        self.name = name
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt


class Articles:
    '''
    Articles  class to define Articles objects
    '''
    def __init__(self,name,author,title,urlToImage,description,publishedAt):
        self.name = name
        self.author = author
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt
