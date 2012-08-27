import os, sys
import Image

imagefile = sys.argv[1]
f, e = os.path.splitext(imagefile)
outfile = open(f + ".html", 'w')
i = Image.open(imagefile)

pixels = i.load()
width, height = i.size

def triplet(rgb):
  return format((rgb[0]<<16)|(rgb[1]<<8)|rgb[2], '06x')

colors = [[triplet(pixels[x,y]) for y in range(height)] for x in range(width)]

outfile = open(f + ".html", 'w')
outfile.write("<html>\n")
outfile.write("  <head>\n")
outfile.write("    <style type=\"text/css\">\n")
outfile.write("      table.pixeltable\n")
outfile.write("      {\n")
outfile.write("        border-spacing: 0;\n")
outfile.write("        border-collapse: collapse;\n")
outfile.write("      }\n")
outfile.write("      td.p\n")
outfile.write("      {\n")
outfile.write("        width: 1px;\n")
outfile.write("        height: 1px;\n")
outfile.write("        border: 0;\n")
outfile.write("        padding: 0;\n")
outfile.write("      }\n")
outfile.write("    </style>\n")
outfile.write("  </head>\n")
outfile.write("  <body bgcolor=\"#ffffff\">\n")
outfile.write("    <table class=\"pixeltable\">\n")
for y in range(height):
  outfile.write("      <tr>\n")
  for x in range(width):
    outfile.write("        <td class=\"p\" bgcolor=\"#")
    outfile.write(colors[x][y])
    outfile.write("\"></td>\n")
  outfile.write("      </tr>\n")
outfile.write("    </table>\n")
outfile.write("  </body>\n")
outfile.write("</html>\n")
outfile.close()

