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
