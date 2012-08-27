pixeltable
==========

*pixeltable* is a python script that takes an image file and encodes it as an HTML table of one-pixel-sized cells.  Each individual cell has a bgcolor attribute that replicates the color of the corresponding pixel.

### Usage ###

**python pixeltable.py [path]/[name].jpg** will create **[path]/[name].html**; a properly formatted HTML file that replicates the image with CSS and an HTML table.  This should only be used for small images (100x100 at the biggest).

#### File size results from initial tests ####
<table>
  <tr>
    <td><strong>image width</strong></td>
    <td><strong>image height</strong></td>
    <td><strong>.JPG file size</strong></td>
    <td><strong>.HTML file size</strong></td>
  </tr>
  <tr>
    <td>50 pixels</td>
    <td>20 pixels</td>
    <td>4.9 kB</td>
    <td>46.9 kB</td>
  </tr>
  <tr>
    <td>100 pixels</td>
    <td>40 pixels</td>
    <td>6.8 kB</td>
    <td>185.3 kB</td>
  </tr>
  <tr>
    <td>400 pixels</td>
    <td>245 pixels</td>
    <td>52.7 kB</td>
    <td>4.5 MB</td>
  </tr>
</table>

Made by John Atkinson   
[http://discountgeni.us](http://discountgeni.us)  
[@discountgenius](http://twitter.com/discountgenius)  
