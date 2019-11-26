from parser import parse
import shutil
import os

if __name__ == '__main__':
    parse('AI/AI_analytics', 'temp/AI_analytics.md')
    parse('AI/AI_application', 'temp/AI_application.md')
    parse('AI/AI_theory', 'temp/AI_theory.md')
    parse('IoT/IoT_environment', 'temp/IoT_environment.md')
    parse('IoT/IoT_smart_building', 'temp/IoT_smart_building.md')

    all_bib = open('set/ai.md', 'w')
    all_bib.write('## Artificial Intelligence\n')
    all_bib.write('### AI Theory\n')
    bib1 = open('temp/AI_theory.md', 'r').read()
    all_bib.write(bib1)
    all_bib.write('\n')

    all_bib.write('### AI Analytics\n')
    bib2 = open('temp/AI_analytics.md', 'r').read()
    all_bib.write(bib2)
    all_bib.write('\n')

    all_bib.write('### AI Application\n')
    bib3 = open('temp/AI_application.md', 'r').read()
    all_bib.write(bib3)
    all_bib.write('\n')
    all_bib.close()

    all_bib2 = open('set/iot.md', 'w')
    all_bib2.write('## Internet of Things\n')
    all_bib2.write('### IoT Environment\n')
    bib4 = open('temp/IoT_environment.md', 'r').read()
    all_bib2.write(bib4)
    all_bib2.write('\n')

    all_bib2.write('### IoT Smart Building\n')
    bib5 = open('temp/IoT_smart_building.md', 'r').read()
    all_bib2.write(bib5)
    all_bib2.write('\n')
    all_bib2.close()

