def GetWord():
    from deep_translator import GoogleTranslator

# считывние слов
    ready = open('ReadyWord.txt', 'w')
    eng = open('EngWord.txt', 'r')

# закидывание в массив
    EngWord = list(eng.read().split(","))
    RuWord = []

# перевод и запись в файл
    translator = GoogleTranslator(source='auto', target='ru')
    for i in range(len(EngWord)):
        RuWord.append(translator.translate(EngWord[i]))
        if i != len(EngWord):
            ready.write(str(EngWord[i]) + "-" + str(RuWord[i]) + ";")
        else:
            ready.write(str(EngWord[i]) + "-" + str(RuWord[i]))
    ready.close()
    eng.close()
