

def CreateText(eng):
    from GetWord import GetWord


    #считывание нужных слов с клавы

    engword=open('EngWord.txt','w')
    engword.write(eng)
    engword.close()

    #переделывание в шпору
    GetWord()

    #создание файла
    re=open('ReadyWord.txt','r')


