﻿import os, re, codecs

tr = ''
dic = ''
dictionary = []
f = []
fnames = []
for root, dirs, files in os.walk(u'.'):
    for l in files:
        f.append(l)
for k in f:
    trtext = []
    t = re.findall(u'.*\.txt', k)
    for y in t:
        fnames.append(y)
for name in fnames:
    print name
    r = codecs.open(name, 'r', 'utf-8')
    for line in r:
        line = line.lower()
        line = re.sub(u'/',u' /',line, flags = re.U)
        line = re.sub(u'-',u'',line, flags = re.U)
        line = re.sub(u'»',u'',line, flags = re.U)
        line = re.sub(u'«',u'',line, flags = re.U)
        
        line = re.sub(u'нн',u'н',line, flags = re.U)
        line = re.sub(u'пп',u'п',line, flags = re.U)
        line = re.sub(u'рр',u'р',line, flags = re.U)
        line = re.sub(u'мм',u'м',line, flags = re.U)
        line = re.sub(u'сс',u'с',line, flags = re.U)
        line = re.sub(u'лл',u'л',line, flags = re.U)
        line = re.sub(u'кк',u'к',line, flags = re.U)
        line = re.sub(u'оо',u'о',line, flags = re.U)

        line = re.sub(u'(\\s)что',u'\\1што',line, flags = re.U)
        
        
        
        line = re.sub(u'([^\ẃ]из)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]у)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]со?)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]в)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]на)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]к)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]по)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]перед(о)?)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]под(о)?)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]над(о)?)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]за)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]до)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]при)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]от)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]для)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]про)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]о)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]без)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]не)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]ни)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]и)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]а)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'\s(ли\s)',u'\\1',line, flags = re.U)
        line = re.sub(u'\s(же\s)',u'\\1',line, flags = re.U)
        line = re.sub(u'\s(бы\s)',u'\\1',line, flags = re.U)
        line = re.sub(u'-(таки\s)',u'\\1',line, flags = re.U)
        line = re.sub(u'-(то\s)',u'\\1',line, flags = re.U)
        line = re.sub(u'-(ка\s)',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]и)\s',u'\\1',line, flags = re.U)
        line = re.sub(u'([^\ẃ]но)\s',u'\\1',line, flags = re.U)

        
        
        
        
        
        for word in line.split():
            
            orphw = word.strip('\"')
            orphw = orphw.strip('/')
            orphw = orphw.strip(u'“”?')
            orphw = orphw.strip(u'.”",')
            word = word.strip(u'-')
            
            word = re.sub(u'\"',u'',word)
            word = re.sub(u'ё',u'ё́',word)
            word = re.sub(u'\.',u' // ',word)
            word = re.sub(u',',u' / ',word)
            word = re.sub(u'([ое]́?)го$',u'\\1во',word, flags = re.U)
            word = re.sub(u'([ое]́?)го́$',u'\\1во́',word, flags = re.U)
            word = re.sub(u'т(ь)?ся',u'ца',word, flags = re.U)
            
            
            
            word = re.sub(u'[тд]c([йцкнгшщзхфвпрлджчсмтбj])',u'ц\\1',word, flags=re.U)
            word = re.sub(u'[сз]ш',u'шш',word, flags=re.U)
            word = re.sub(u'зж',u'жж',word, flags=re.U)
            word = re.sub(u'([тд])ц',u'цц',word, flags=re.U)
            word = re.sub(u'([тд]ь?)ч',u'чч',word, flags=re.U)
            word = re.sub(u'с[тд]ч',u'щ',word, flags=re.U)
            word = re.sub(u'гк',u'хк',word, flags=re.U)
            word = re.sub(u'гч',u'хч',word, flags=re.U)
            word = re.sub(u'с[тд]н',u'сн',word, flags = re.U)
            word = re.sub(u'лнц',u'нц',word, flags = re.U)
            word = re.sub(u'здн',u'зн',word, flags = re.U)
            word = re.sub(u'стл',u'сл',word, flags = re.U)
            word = re.sub(u'рдц',u'рц',word, flags = re.U)
            word = re.sub(u'рдч',u'рч',word, flags = re.U)
            word = re.sub(u'нтск',u'нск',word, flags = re.U)
            word = re.sub(u'с[тд]ск',u'сск',word, flags = re.U)
            word = re.sub(u'[дт]ст',u'цт',word, flags = re.U)
            word = re.sub(u'гк',u'хк',word, flags = re.U)
            word = re.sub(u'гч',u'хч',word, flags = re.U)
            
            word = re.sub(u'(^|ъ)я',u'jа',word, flags = re.U)
            word = re.sub(u'(о|у|е|ы|а|э|я|и|ю|́)я',u'\\1jа',word, flags = re.U)
            word = re.sub(u'ья',u'\'jа',word, flags = re.U)
            
            word = re.sub(u'(^|ъ)ю',u'jу',word, flags = re.U)
            word = re.sub(u'(о|у|е|ы|а|э|я|и|ю|́)ю',u'\\1jу',word, flags = re.U)
            word = re.sub(u'ью',u'\'jу',word, flags = re.U)
            
            word = re.sub(u'(^|ъ)ё',u'jо',word, flags = re.U)
            word = re.sub(u'(о|у|е|ы|а|э|я|и|ю|́)ё',u'\\1jо',word, flags = re.U)
            word = re.sub(u'ьё',u'\'jо',word, flags = re.U)
            
            word = re.sub(u'(^|ъ)е',u'jе',word, flags = re.U)
            word = re.sub(u'(о|у|е|ы|а|э|я|и|ю|́)е',u'\\1jе',word, flags = re.U)
            word = re.sub(u'ье',u'\'jе',word, flags = re.U)
            
            word = re.sub(u'ьи',u'\'jи',word, flags = re.U)
            word = re.sub(u'ь',u'\'',word, flags = re.U)


            word = re.sub(u'к((в\'?)?[гбдзж])',u'г\\1',word, flags = re.U)
            word = re.sub(u'х((в\'?)?[гбдзж])',u'ɣ\\1',word, flags = re.U)
            word = re.sub(u'с((в\'?)?[гбдзж])',u'з\\1',word, flags = re.U)
            word = re.sub(u'ф((в\'?)?[гбдзж])',u'в\\1',word, flags = re.U)
            word = re.sub(u'т((в\'?)?[гбдзж])',u'д\\1',word, flags = re.U)
            word = re.sub(u'ш((в\'?)?[гбдзж])',u'ж\\1',word, flags = re.U)
            word = re.sub(u'п((в\'?)?[гбдзж])',u'б\\1',word, flags = re.U)
            word = re.sub(u'г((в\'?)?[хцшфпчстщ])',u'к\\1',word, flags = re.U)
            word = re.sub(u'з((в\'?)?[хкцшфпчтщ])',u'с\\1',word, flags = re.U)
            word = re.sub(u'в((в\'?)?[хкцшпчстщ])',u'ф\\1',word, flags = re.U)
            word = re.sub(u'в((в\'?)?[хкцшпчстщ])',u'ф\\1',word, flags = re.U)
            word = re.sub(u'д((в\'?)?[хкцшфпчсщ])',u'т\\1',word, flags = re.U)
            word = re.sub(u'ж((в\'?)?[хкцфпчстщ])',u'ш\\1',word, flags = re.U)
            word = re.sub(u'б((в\'?)?[хкцшфчстщ])',u'п\\1',word, flags = re.U)
            word = re.sub(u'к\'((в\'?)?[гбдзж])',u'г\'\\1',word, flags = re.U)
            word = re.sub(u'с\'((в\'?)?[гбдзж])',u'з\'\\1',word, flags = re.U)
            word = re.sub(u'ф\'((в\'?)?[гбдзж])',u'в\'\\1',word, flags = re.U)
            word = re.sub(u'т\'((в\'?)?[гбдзж])',u'д\'\\1',word, flags = re.U)
            word = re.sub(u'п\'((в\'?)?[гбдзж])',u'б\'\\1',word, flags = re.U)
            word = re.sub(u'г\'((в\'?)?[хцшфпчстщ])',u'к\'\\1',word, flags = re.U)
            word = re.sub(u'з\'((в\'?)?[хкцшфпчтщ])',u'с\'\\1',word, flags = re.U)
            word = re.sub(u'в\'((в\'?)?[хкцшпчстщ])',u'ф\'\\1',word, flags = re.U)
            word = re.sub(u'в\'((в\'?)?[хкцшпчстщ])',u'ф\'\\1',word, flags = re.U)
            word = re.sub(u'д\'((в\'?)?[хкцшфпчсщ])',u'т\'\\1',word, flags = re.U)
            word = re.sub(u'б\'((в\'?)?[хцшфчстщ])',u'п\\1',word, flags = re.U)
            word = re.sub(u'г$',u'к',word, flags = re.U)
            word = re.sub(u'з$',u'с',word, flags = re.U)
            word = re.sub(u'в$',u'ф',word, flags = re.U)
            word = re.sub(u'д$',u'т',word, flags = re.U)
            word = re.sub(u'ж$',u'ш',word, flags = re.U)
            word = re.sub(u'б$',u'п',word, flags = re.U)
            word = re.sub(u'з\'$',u'с\'',word, flags = re.U)
            word = re.sub(u'в\'$',u'ф\'',word, flags = re.U)
            word = re.sub(u'д\'$',u'т\'',word, flags = re.U)
            word = re.sub(u'ж\'$',u'ш\'',word, flags = re.U)
            word = re.sub(u'б\'$',u'п\'',word, flags = re.U)

            word = re.sub(u'([кнгзхфвпрлдсмтб])([ие])',u'\\1\'\\2',word, flags = re.U)
            word = re.sub(u'([кнгзхфвпрлдсмтб])я',u'\\1\'а',word, flags = re.U)
            word = re.sub(u'([кнгзхфвпрлдсмтб])ю',u'\\1\'у',word, flags = re.U)
            word = re.sub(u'([кнгзхфвпрлдсмтб])ё',u'\\1\'о',word, flags = re.U)
            word = re.sub(u'([цжш])([и])',u'\\1ы',word, flags = re.U)
            word = re.sub(u'([йцjшщжч])я',u'\\1\'а',word, flags = re.U)
            word = re.sub(u'([йцjшщжч])ю',u'\\1\'у',word, flags = re.U)
            word = re.sub(u'([йцjшщжч])ё',u'\\1\'о',word, flags = re.U)

            word = re.sub(u'э',u'е',word, flags = re.U)
            word = re.sub(u'([шжц])е',u'\\1э',word, flags = re.U)
            word = re.sub(u'^э',u'е',word, flags = re.U)
            
            word = re.sub(u'([кгх])([кгх]\')',u'\\1\'\\2',word, flags = re.U)
            word = re.sub(u'([вфбпм])([вфбпм]\')',u'\\1\'\\2',word, flags = re.U)
            word = re.sub(u'([вфзслдтн])([лзсдтн]\')',u'\\1\'\\2',word, flags = re.U)

            word = re.sub(u'й',u'j',word, flags = re.U)

            word = re.sub(u'([оуеыаэяию]([йцкнгшщзхфвпрлджчсмтбj]\'?)*(е́|ы́|а́|о́|э́|я́́|и́|ю́|у́))',u'☺\\1',word, flags=re.U)
            word = re.sub(u'^([оыаеиэ][^́])',u'☺\\1',word, flags=re.U)

            word = re.sub(u'([^☺]\'|j|ч|щ|о|ы|а|е|и|э|ъ|ь|́)[оыаеиэ]([^́]|$)',u'\\1ь\\2',word, flags=re.U)
            word = re.sub(u'([^☺]\'|j|ч|щ|о|ы|а|е|и|э|ъ|ь|́)[оыаеиэ]([^́]|$)',u'\\1ь\\2',word, flags=re.U)
            
            word = re.sub(u'([^☺])[оыаеиэ]([^́]|$)',u'\\1ъ\\2',word, flags=re.U)
            word = re.sub(u'([^☺])[оыаеиэ]([^́]|$)',u'\\1ъ\\2',word, flags=re.U)
            word = re.sub(u'([^☺]\'|j|ч|щ|о|ы|а|е|и|э|ъ|ь)у([^́]|$)',u'\\1ь°\\2',word, flags=re.U)
            word = re.sub(u'([^☺]\'|j|ч|щ|о|ы|а|е|и|э|ъ|ь)у([^́]|$)',u'\\1ь°\\2',word, flags=re.U)
            word = re.sub(u'([^☺])у([^́]|$)',u'\\1ъ°\\2',word, flags=re.U)
            word = re.sub(u'([^☺])у([^́]|$)',u'\\1ъ°\\2',word, flags=re.U)

            word = re.sub(u'☺',u'',word, flags=re.U)

            word = re.sub(u'(\w|\')е([^́])',u'\\1и\\2',word, flags=re.U)
            word = re.sub(u'(\'|ч|щ|j)а([^́])',u'\\1и\\2',word, flags=re.U)
            
            word = re.sub(u'([жшц])о([^́])',u'\\1ы\\2',word, flags=re.U)
            word = re.sub(u'о([^́])',u'а\\1',word, flags=re.U)

            
            
            trtext.append(word)
    text = ''
    for w in trtext:
       text = text + w + ' '
    text = re.sub(u'т( (в\'?)?[гбдзж])',u'д\\1', text, flags = re.U)
    text = re.sub(u'к( (в\'?)?[гбдзж])',u'г\\1', text, flags = re.U)
    text = re.sub(u'х( (в\'?)?[гбдзж])',u'ɣ\\1', text, flags = re.U)
    text = re.sub(u'ф( (в\'?)?[гбдзж])',u'в\\1', text, flags = re.U)
    text = re.sub(u'ф( (в\'?)?[гбдзж])',u'б\\1', text, flags = re.U)
    text = re.sub(u'с( (в\'?)?[гбдзж])',u'з\\1', text, flags = re.U)
    text = re.sub(u'т(\' (в\'?)?[гбдзж])',u'д\\1', text, flags = re.U)
    text = re.sub(u'к(\' (в\'?)?[гбдзж])',u'г\\1', text, flags = re.U)
    text = re.sub(u'х(\' (в\'?)?[гбдзж])',u'ɣ\\1', text, flags = re.U)
    text = re.sub(u'ф(\' (в\'?)?[гбдзж])',u'в\\1', text, flags = re.U)
    text = re.sub(u'ф(\' (в\'?)?[гбдзж])',u'б\\1', text, flags = re.U)
    text = re.sub(u'с(\' (в\'?)?[гбдзж])',u'з\\1', text, flags = re.U)

    
    z = codecs.open(u'transcription_'+name+'.txt', 'w', 'utf-8')
    z.write('['+text+']')
    z.close()

    r.close()
