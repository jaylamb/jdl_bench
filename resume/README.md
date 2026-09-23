Copyright 2020 Jay D. Lamb 

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author  : Jay D. Lamb

License : MIT

File        : README.md

Description : Project README.

# Resume
My resume.

## Usage
The main document file, `resume.tex` contains all of the high-level document
information (packages used, margin information) and includes for other sections
of the document. All other included files are located within the `section`
directory.

The following packages are required to generate the document:

* texlive
* texlive-latex-extra
* texlive-fonts-extra

Build the .pdf using the following command:

`pdflatex resume.tex`

## Helper Sections

### Defines

The `defines.tex` file contains definitions used throughout the document. These
include:

* Header type (single or double column) 
* Entry spacing
* Bullet styling
* Colors used
* Header information (name, phone number, email address, LinkedIn information,
 GitHub information)

### Commands

The `commands.tex` file contains each of the custom commands used to produce and
format sections of the document.

## Document Sections
The document contains three document sections:

* Education
* Experience
* Skills

Each of these sections exist within their own `.tex` file, located within the
`section` directory.

## Credits

Inspiration for this document is
[here](https://www.overleaf.com/latex/templates/software-engineering-resume/mcvwcrmddsyw)

Original template from [here](https://github.com/sb2nov/resume).

Template text from [here](https://resumake.io/).
