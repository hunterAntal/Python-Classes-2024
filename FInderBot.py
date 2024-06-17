class FinderBot:
    word = ''
    myList = []
    def __init__(self, string, word):
        myList = []
        self.word = word
        
        self.string = string.replace('.','').replace('!','').replace('?','').replace(',','')
        self.string.lower()
        myList = self.string.split(' ')

        #print('test01')
        self.countWord(myList)
        #print('test02')

    def countWord(self, myList):
        stringDic = {}

        for key in myList:
            stringDic[key] = myList.count(key)

        #print(stringDic)
        print(self.word,'shows up exactly', stringDic[self.word],'times in your text')
