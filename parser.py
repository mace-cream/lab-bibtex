import os
import bibtexparser as bp
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

from pybtex.database.format import format_database


def gather_bibs(dir, export_file):
    db = BibDatabase()
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    bibs = {}
    for file in os.listdir('./' + dir):
        if file.endswith('.bib'):
            with open('./' + dir + '/' + file) as bib_file:
                bib_data = bp.load(bib_file, parser=parser)
                for entry in bib_data.entries:
                    if entry['ID'] not in bibs:
                        bibs[entry['ID']] = entry

    for key in bibs:
        db.entries.append(bibs[key])
    writer = BibTexWriter()
    with open('set/' + export_file, 'w') as bibfile:
        bibfile.write(writer.write(db))


# 异常处理暂时无效，需要进一步解决
# 目前若是想生成正确的html，需要所有bib文件正确
def export_html():
    format_database('set/ai.bib', 'set/ai.md', 'bibtex', 'md')
    format_database('set/iot.bib', 'set/iot.md', 'bibtex', 'md')
    all_bib = open('set/_index.en.md', 'w')
    all_bib.write('###Artificial Intelligence\n')
    ai_bib = open('set/ai.md', 'r').read()
    iot_bib = open('set/iot.md', 'r').read()
    all_bib.write(ai_bib)
    all_bib.write('***\n')
    all_bib.write('###Internet of Things\n')
    all_bib.write(iot_bib)
    os.remove('set/ai.bib')
    os.remove('set/ai.md')
    os.remove('set/iot.bib')
    os.remove('set/iot.md')
