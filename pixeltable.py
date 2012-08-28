import os, sys
import Image
import argparse

parser = argparse.ArgumentParser(description='Convert an image to a HTML table')
parser.add_argument("-m", "--min", help="create minified HTML code", action="store_false")
parser.add_argument("file", help="filename of the image to convert")
args = parser.parse_args()

if (args.min):
  newline = "\n"
  tab = "  "
else:
  newline = ""
  tab = ""

imagefile = args.file
f, e = os.path.splitext(imagefile)
outfile = open(f + ".html", 'w')
i = Image.open(imagefile)

pixels = i.load()
width, height = i.size

def triplet(rgb):
  return format((rgb[0]<<16)|(rgb[1]<<8)|rgb[2], '06x')

colors = [[triplet(pixels[x,y]) for y in range(height)] for x in range(width)]

outfile = open(f + ".html", 'w')
outfile.write("<html>")
outfile.write(tab + "<head>" + newline)
outfile.write(tab * 2 + "<style type=\"text/css\">" + newline)
outfile.write(tab * 3 + "table.pixeltable" + newline)
outfile.write(tab * 3 + "{" + newline)
outfile.write(tab * 3 + "border-spacing: 0;" + newline)
outfile.write(tab * 3 + "border-collapse: collapse;" + newline)
outfile.write(tab * 3 + "width: ")
outfile.write(str(width))
outfile.write("px;" + newline)
outfile.write(tab * 3 + "height: ")
outfile.write(str(height))
outfile.write("px;" + newline)
outfile.write(tab * 2 + "}" + newline)
outfile.write(tab * 2 + ".pixeltable td" + newline)
outfile.write(tab * 2 + "{" + newline)
outfile.write(tab * 3 + "width: 1px;" + newline)
outfile.write(tab * 3 + "height: 1px;" + newline)
outfile.write(tab * 3 + "border: 0;" + newline)
outfile.write(tab * 3 + "padding: 0;" + newline)
outfile.write(tab * 2 + "}" + newline)
outfile.write(tab * 2 + "</style>" + newline)
outfile.write(tab + "</head>" + newline)
