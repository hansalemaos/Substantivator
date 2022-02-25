from get_languages_codes import *
from check_if_nan import *
from get_filepath import *
from menudownload import *
from einfuehrung import *

sprachen = ['aa', 'af', 'ak', 'an', 'ar', 'ay', 'az', 'ba', 'be', 'bg', 'bh', 'bi', 'bm', 'br', 'bs', 'ca', 'ce', 'ch',
            'co', 'cr', 'cs', 'cv', 'cy', 'da', 'de', 'dv', 'ee', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'ff', 'fi',
            'fj', 'fo', 'fr', 'fy', 'ga', 'gd', 'gl', 'gn', 'gr', 'gv', 'ha', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'hz',
            'ia', 'id', 'ie', 'ig', 'ik', 'io', 'is', 'it', 'iu', 'ja', 'jv', 'ka', 'kg', 'ki', 'kj', 'kk', 'kl', 'kn',
            'ko', 'kr', 'ku', 'kw', 'ky', 'la', 'lb', 'lg', 'li', 'ln', 'lo', 'lt', 'lv', 'mg', 'mh', 'mi', 'mk', 'mn',
            'mo', 'mr', 'ms', 'mt', 'na', 'nb', 'nd', 'ne', 'ng', 'nl', 'nn', 'no', 'nr', 'nv', 'ny', 'oc', 'oj', 'om',
            'pa', 'pi', 'pl', 'pt', 'qu', 'rm', 'rn', 'ro', 'ru', 'rw', 'sc', 'sd', 'se', 'sg', 'sh', 'sk', 'sl', 'sm',
            'sn', 'so', 'sq', 'sr', 'ss', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'ti', 'tk', 'tl', 'tn', 'to',
            'tr', 'ts', 'tt', 'tw', 'ty', 'uk', 'ur', 'uz', 've', 'vi', 'vo', 'wa', 'wo', 'xh', 'yi', 'yo', 'za', 'zh',
            'zu']

einfuehrung(name='Subsantivator')
drucker = Farbprinter()
df = pd.read_pickle(get_file_path('B2substantiveuebungen.pkl')[0])
df = df.sample(len(df))
userpunkte = 0
gesamtpunkte = 0


def richtig(leerzeichen=5):
    global userpunkte
    global gesamtpunkte
    gesamtpunkte = gesamtpunkte + 1
    userpunkte = userpunkte + 1
    print(drucker.f.black.brightgreen.normal(
        f'\nDeine Antwort ist richtig!\nErreichte Punkte:    {userpunkte}\nMaximale Punktanzahl:    {gesamtpunkte}\n'))
    print('\n' * leerzeichen)


def falsch(leerzeichen=5):
    global userpunkte
    global gesamtpunkte
    gesamtpunkte = gesamtpunkte + 1
    print(drucker.f.black.brightred.normal(f'\nDeine Antwort ist falsch!\nErreichte Punkte:    ') +   drucker.f.black.brightred.negative(
        f'  {userpunkte}  ') + drucker.f.black.brightred.normal(f'\nMaximale Punktanzahl:    ') + drucker.f.black.brightred.negative(
        f'  {gesamtpunkte}  ') + drucker.f.black.brightred.normal(f'\n'))
    print('\n' * leerzeichen)


def get_bestimmter_artikel(genus, kasus):
    genus = str(genus).strip().lower()
    kasus = str(kasus).strip().lower()
    if genus == 'n' or genus == 'neutral' or genus == 'sachlich' or genus == 'sächlich' or genus == 'saechlich':
        if kasus == 'nom' or kasus == 'nominativ' or kasus == '1' or kasus == 'akk' or kasus == 'akkusativ' or kasus == '4':
            return 'das'
        if kasus == 'dat' or kasus == 'dativ' or kasus == '3':
            return 'dem'
        if kasus == 'gen' or kasus == 'genitiv' or kasus == '2':
            return 'des'
    if genus == 'm' or genus == 'maskulin' or genus == 'männlich' or genus == 'maennlich':
        if kasus == 'nom' or kasus == 'nominativ' or kasus == '1':
            return 'der'
        if kasus == 'akk' or kasus == 'akkusativ' or kasus == '4':
            return 'den'
        if kasus == 'dat' or kasus == 'dativ' or kasus == '3':
            return 'dem'
        if kasus == 'gen' or kasus == 'genitiv' or kasus == '2':
            return 'des'
    if genus == 'f' or genus == 'feminin' or genus == 'weiblich':
        if kasus == 'nom' or kasus == 'nominativ' or kasus == '1' or kasus == 'akk' or kasus == 'akkusativ' or kasus == '4':
            return 'die '
        if kasus == 'dat' or kasus == 'dativ' or kasus == '3' or kasus == 'gen' or kasus == 'genitiv' or kasus == '2':
            return 'der'
    if genus == 'pl' or genus == 'plural' or genus == 'mehrzahl':
        if kasus == 'nom' or kasus == 'nominativ' or kasus == '1' or kasus == 'akk' or kasus == 'akkusativ' or kasus == '4':
            return 'die '
        if kasus == 'dat' or kasus == 'dativ' or kasus == '3':
            return 'den'
        if kasus == 'gen' or kasus == 'genitiv' or kasus == '2':
            return 'der'
    return ''


def wie_viele_aufgaben_erstellen(farbe='brightblue', text="Wie viele Aufgaben erstellen?"):
    wievieleaufgaben = 0
    while wievieleaufgaben == 0:
        try:
            wievieleaufgaben_eingeben = input(drucker.f.black[farbe].normal(f'\n{text}\n'))
            wievieleaufgaben_eingeben = str(wievieleaufgaben_eingeben).strip()
            wievieleaufgaben_eingeben = int(wievieleaufgaben_eingeben)
            wievieleaufgaben = wievieleaufgaben_eingeben
        except:
            print(drucker.f.black.brightred.normal('\nFehler bei der Eingabe!\n'))
            continue
    return wievieleaufgaben



anzahlaufgaben = wie_viele_aufgaben_erstellen()
mit_gen_dat = auswahlmenu_erstellen(optionen=['Nur Genus und Plural', 'Genus, Plural, Dativ und Genitiv'], uberschrift='Möchtest du nur das Genus und den Plural trainieren oder auch Dativ und Genitiv?\n',
                                          color='brightmagenta', unterdemtext='\nDeine Eingabe:\n')
durchgang = 0
for key, row in df.iterrows():
    durchgang = durchgang+1
    for sprache in sprachen:
        if isnan(row[sprache]) is False:
            spracheverfuegbar = get_language(sprache)[0]
            allewoerter = ' | '.join(row[sprache])
            print(drucker.f.brightyellow.black.italic(f'{spracheverfuegbar.ljust(20)}    : {allewoerter.ljust(80)}'))
    nominativsingular = row['Nominativ Singular'][0]
    akkusativ_plural = row['Akkusativ Plural']
    akkusativ_singular = row['Akkusativ Singular']
    dativ_plural = row['Dativ Plural']
    dativ_singular = row['Dativ Singular']
    genitiv_plural = row['Genitiv Plural']
    genitiv_singular = row['Genitiv Singular']
    genus = row['Genus']
    nominativ_plural = row['Nominativ Plural']
    print(drucker.f.black.brightmagenta.underline(f'\n   Substantiv:  \n') + drucker.f.brightmagenta.black.normal (f'                       {nominativsingular}                       '), end='')
    genusgewaehlt = auswahlmenu_erstellen(optionen=['der', 'die', 'das'], uberschrift='Welches Genus hat das Wort?\n',
                                          color='brightcyan', unterdemtext='\nDeine Eingabe:\n')
    echtesgenus = ''
    if genusgewaehlt == '1':
        genusgewaehlt = 'm'
    if genusgewaehlt == '2':
        genusgewaehlt = 'f'

    if genusgewaehlt == '3':
        genusgewaehlt = 'n'

    if genusgewaehlt in genus:
        richtig()
    elif genusgewaehlt not in genus:
        falsch()
    pluraldativanzeigen = True
    nominativplural_user = input(drucker.f.black.brightgreen.normal(f'Bitte ') + drucker.f.brightgreen.black.normal (' Plural ') + drucker.f.black.brightgreen.normal (' von ')   + drucker.f.brightgreen.black.normal  (f' {nominativsingular} ') +  drucker.f.black.brightgreen.normal (' eingeben:\n')  +  drucker.f.black.brightgreen.underline ('Wenn es kein Plural gibt, X eingeben (beispielsweise beim Wort "Mist")!\n')+  drucker.f.black.brightgreen.normal ('die __________\n '))
    if len(nominativplural_user) == 1:
        if len(nominativplural_user) == len(nominativ_plural[0]):
            richtig()
            pluraldativanzeigen = False
        elif len(nominativplural_user) != len(nominativ_plural[0]):
            falsch()
            pluraldativanzeigen = True

    if len(nominativplural_user) != 1:
        if nominativplural_user in nominativ_plural:
            richtig()
            pluraldativanzeigen = True

        elif nominativplural_user not in nominativ_plural:
            falsch()
            if len(nominativ_plural[0]) > 1:
                pluraldativanzeigen = True
    if mit_gen_dat == '2':
        if pluraldativanzeigen:
            if '-' not in dativ_plural and '–' not in dativ_plural and isnan(dativ_plural) is False and '—' not in genitiv_singular:
                dativplural_user = input(drucker.f.black.brightmagenta.normal(
                    f'Bitte ') + drucker.f.brightmagenta.black.normal(f' Plural Dativ ')  + drucker.f.black.brightmagenta.normal(f' von ') +  drucker.f.brightmagenta.black.normal(f' {nominativsingular} ') + drucker.f.black.brightmagenta.normal(f' eingeben: \n mit den __________\n '))
                if dativplural_user.strip() in dativ_plural:
                    richtig()
                elif dativplural_user.strip() not in dativ_plural:
                    falsch()

        if '-' not in genitiv_singular and '–' not in genitiv_singular and isnan(genitiv_singular) is False and '—' not in genitiv_singular:

            genitiv_singular_user = input(drucker.f.black.brightcyan.normal(f'Bitte ') + drucker.f.brightcyan.black.normal(' Singular Genitiv ') + drucker.f.black.brightcyan.normal(' von ') + drucker.f.brightcyan.black.normal (f' {nominativsingular} ') + drucker.f.black.brightcyan.normal(f'eingeben: \n wegen {get_bestimmter_artikel(genus[0], "gen")} __________\n '))
            if genitiv_singular_user.strip() in genitiv_singular:
                richtig()
            elif genitiv_singular_user.strip() not in genitiv_singular:
                falsch()
        if durchgang ==anzahlaufgaben:
            break

fertig = input(f'\nDu hast insgesamt {userpunkte} von {gesamtpunkte} erreicht\n')