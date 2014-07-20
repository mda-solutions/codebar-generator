
 # 
 #     repo:   https://github.com/mda-solutions
 #     author: moises.rangel@gmail.com
 #
 # Licensed under the MIT License (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #     http://opensource.org/licenses/MIT
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.
 #
  

import string
import random

from reportlab.graphics.barcode import code39
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

class barcodes(object):
    
    """Genera codigos de barras """
    def __init__(self):
        super(barcodes, self).__init__()

    def chars(self, type_chars):
        return {
            'digits': string.digits, 
            'chars': string.ascii_uppercase, 
            'mixed': string.ascii_uppercase + string.digits }.get(type_chars)

    # http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    # type: digits | string | mixed
    def generateStringcode(self, size = 9, type = "mixed"):
        chars = self.chars(type)
        return ''.join(random.choice(chars) for _ in range(size))

    def createPDF(self):
        
        c = canvas.Canvas("barcodes.pdf", pagesize=letter)
        x = 15 * mm
        y = 285 * mm
        x1 = 6.4 * mm

        for code in self.codelist:
            barcode = code39.Extended39(code)
            barcode.drawOn(c, x, y)
            x1 = x + 6.4 * mm
            y = y - 5 * mm
            c.drawString(x1, y, code)
            x = x
            y = y - 10 * mm

            if int(y) == 0:
                x = x + 50 * mm
                y = 285 * mm

        c.showPage()
        c.save()                

    def generateCodeList(self, length = 76):
        self.codelist = []
        for i in range(length):
            codebar = self.generateStringcode()
            if codebar not in self.codelist:
                self.codelist.append(codebar)
                print "generate codebar: " + codebar                
        

if __name__ == '__main__':
    codes = barcodes()
    codes.generateCodeList()
    codes.createPDF()