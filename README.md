# Publications
[![Build Status](https://travis-ci.com/mace-cream/lab-bibtex.svg?branch=master)](https://travis-ci.com/mace-cream/lab-bibtex)
Our lab needs to collect published paper of students. To make the information collection easier
to manage,
for those students who publish a new paper, it is required to submit the information by yourself.

## Instructions for students
### Accepted Email Received
On our server at `/data/public/bibtex` directory there are two subdirectories `AI` and `IOT`. If there is no file with your name under the two directories,
please create a corresponding bibtex file , for example "AI/AI_theory/xiangxiangxu.bib".

For bibtex key，it's better to follow Google scholar style，ie last name + year +first title word （except for common words eg ‘a,the,on,towards ). 
For example: guo2019mobility.

Please finish it as soon as possible once your paper is accepted.

Your paper will soon be indexed by our lab website [publication page](http://10.8.4.170/lab2cnew/en/publication/).

### Paper Link is Available

You should update the bibtex key using that provided by Google scholar.

You also need to add url={official website}. See AI/AI_analytics/lichen.bib for an example.


## Instructions for Maintainer
If you have push access to [lab-bibtex](https://github.com/mace-cream/lab-bibtex) repository, you should
update `/data/public/bibtex` (which is also a git repo) directly using `git push`. The mechanism of synchronization of lab-bibtex to our lab website is through copying the generated markdown file to 
[website repo](https://github.com/mace-cream/mace-cream.github.io/tree/dev/content/publication).