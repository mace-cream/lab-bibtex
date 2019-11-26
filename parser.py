import os
from operator import itemgetter
import bibtexparser as bp
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode


def parse(dir, export_file):
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    bibs = []
    IDs = []

    for file in os.listdir('./' + dir):
        if file.endswith('.bib'):
            with open('./' + dir + '/' + file) as bib_file:
                bib_data = bp.load(bib_file, parser=parser)
                for entry in bib_data.entries:
                    # print(entry)
                    if entry['ID'] not in IDs:
                        IDs.append(entry['ID'])
                        bibs.append(entry)

    export_file = open(export_file, 'w')
    bibs = sorted(bibs, key=itemgetter('year'))
    index = 0
    for item in bibs:
        index += 1
        index_str = '[' + str(index) + '] '
        title = '**' + item['title'] + '**' + '<br>\n'
        author = item['author'] + '. '
        if 'booktitle' in item:
            book = 'In *' + item['booktitle'] + '*. '
        else:
            book = 'In *' + item['journal'] + '*. '
        year = item['year'] + '. '
        if 'url' in item:
            url = '[Link](' + item['url'] + ') '
        else:
            url = None
        if url:
            export_item = index_str + title + author + book + year + url
        else:
            export_item = index_str + title + author + book + year
        export_file.write(export_item + ' <br> ')
    export_file.close()


if __name__ == '__main__':
    parse('AI/AI_analytics', 'temp2/AI_analytics.md')
    parse('AI/AI_application', 'temp2/AI_application.md')
    parse('AI/AI_theory', 'temp2/AI_theory.md')
    parse('IoT/IoT_environment', 'temp2/IoT_environment.md')
    parse('IoT/IoT_smart_building', 'temp2/IoT_smart_building.md')

    all_bib = open('set/ai.md', 'w')
    all_bib.write('## Artificial Intelligence\n')
    all_bib.write('### AI Theory\n')
    bib1 = open('temp2/AI_theory.md', 'r').read()
    all_bib.write(bib1)
    all_bib.write('\n')

    all_bib.write('### AI Analytics\n')
    bib2 = open('temp2/AI_analytics.md', 'r').read()
    all_bib.write(bib2)
    all_bib.write('\n')

    all_bib.write('### AI Application\n')
    bib3 = open('temp2/AI_application.md', 'r').read()
    all_bib.write(bib3)
    all_bib.write('\n')
    all_bib.close()

    all_bib = open('set/ai.md', 'w')
    all_bib.write('## Internet of Things\n')
    all_bib.write('### IoT Environment\n')
    bib4 = open('temp2/IoT_environment.md', 'r').read()
    all_bib.write(bib4)
    all_bib.write('\n')

    all_bib.write('### IoT Smart Building\n')
    bib5 = open('temp2/IoT_smart_building.md', 'r').read()
    all_bib.write(bib5)
    all_bib.write('\n')

    all_bib.close()
