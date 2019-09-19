import os
import bibtexparser as bp
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

from pybtex.database.format import format_database

def gather_bibs():
    db = BibDatabase()
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    bibs = {}
    for file in os.listdir('./'):
        if file.endswith('.bib'):
            with open(file) as bib_file:
                bib_data = bp.load(bib_file, parser=parser)
                for entry in bib_data.entries:
                    if entry['ID'] not in bibs:
                        bibs[entry['ID']] = entry

    for key in bibs:
        db.entries.append(bibs[key])
    writer = BibTexWriter()
    with open('set/allbibs.bib', 'w') as bibfile:
        bibfile.write(writer.write(db))

# 异常处理暂时无效，需要进一步解决
# 目前若是想生成正确的html，需要所有bib文件正确
def export_html():
    format_database('set/allbibs.bib', 'set/index.en.md', 'bibtex', 'md')
