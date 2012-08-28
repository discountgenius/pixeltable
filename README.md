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
	<td><strong>minified .HTML file size</strong></td>
  </tr>
  <tr>
    <td>50 pixels</td>
    <td>20 pixels</td>
    <td>1.39 KB</td>
    <td>34 KB</td>
	<td>26.8 KB</td>
  </tr>
  <tr>
    <td>100 pixels</td>
    <td>40 pixels</td>
    <td>3.1 KB</td>
    <td>134 KB</td>
	<td>106 KB</td>
  </tr>
  <tr>
    <td>400 pixels</td>
    <td>245 pixels</td>
    <td>59 KB</td>
    <td>3.18 MB</td>
	<td>2.52 MB</td>
  </tr>
</table>

Made by John Atkinson   
[http://discountgeni.us](http://discountgeni.us)  
[@discountgenius](http://twitter.com/discountgenius)  
