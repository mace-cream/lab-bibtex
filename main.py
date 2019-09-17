from parser import gather_bibs, export_html

# 将所有bib文件集合到一个文件中并去掉重复项
gather_bibs()

# 将生成的集合bib文件到处为html文件
# 如果对其中错误进行异常处理，则会导致html文件无法生成，需解决
export_html()
