# Example

### Original Images
![](griffin.gif)
![](jean.gif)
![](totoro.gif)

### Favorites
![](output/greyscale-totoro.gif)
![](output/smart-border-totoro.gif)
![](output/color-substitution-totoro.gif)

### Template
![](output/template-griffin.gif)
![](output/template-jean.gif)
![](output/template-totoro.gif)
```python
template("griffin.gif")
template("jean.gif")
template("totoro.gif")
```
### Border
![](output/border-griffin.gif)
![](output/border-jean.gif)
![](output/border-totoro.gif)
```python
border("griffin.gif", "#00FF00", 30)
border("jean.gif", "#FF0000", 30)
border("totoro.gif", "#0000FF", 100)
```
### Half
![](output/half-griffin.gif)
![](output/half-jean.gif)
![](output/half-totoro.gif)
```python
half("griffin.gif")
half("jean.gif")
half("totoro.gif")
```
### Double
![](output/double-griffin.gif)
![](output/double-jean.gif)
![](output/double-totoro.gif)
```python
double("griffin.gif")
double("jean.gif")
double("totoro.gif")
```
### Side Clone
![](output/side-clone-griffin.gif)
![](output/side-clone-jean.gif)
![](output/side-clone-totoro.gif)
```python
sideClone("griffin.gif")
sideClone("jean.gif")
sideClone("totoro.gif")
```
### Down Clone
![](output/down-clone-griffin.gif)
![](output/down-clone-jean.gif)
![](output/down-clone-totoro.gif)
```python
downClone("griffin.gif")
downClone("jean.gif")
downClone("totoro.gif")
```
### Greyscale
![](output/greyscale-griffin.gif)
![](output/greyscale-jean.gif)
![](output/greyscale-totoro.gif)
```python

greyscale("griffin.gif")
greyscale("jean.gif")
greyscale("totoro.gif")
```
### Smart Border
![](output/smart-border-griffin.gif)
![](output/smart-border-jean.gif)
![](output/smart-border-totoro.gif)
```python

smartBorder("griffin.gif",30)
smartBorder("jean.gif",30)
smartBorder("totoro.gif",100)
```
### Scale
![](output/scale0.25x-griffin.gif)
![](output/scale0.25x-jean.gif)
![](output/scale0.25x-totoro.gif)
```python

# scale_factor = float(input("SCALE FACTOR:"))
scale_factor = 0.25
scale("griffin.gif", scale_factor)
scale("jean.gif", scale_factor)
scale("totoro.gif", scale_factor)
```
### Smart Clone
![](output/smart-clone-griffin.gif)
![](output/smart-clone-jean.gif)
![](output/smart-clone-totoro.gif)
```python

smartClone("griffin.gif",3,2)
smartClone("jean.gif",3,2)
smartClone("totoro.gif",3,2)
```
### Tile
![](output/tile-griffin.gif)
![](output/tile-jean.gif)
![](output/tile-totoro.gif)
```python
tile("griffin.gif",3,2)
tile("jean.gif",3,2)
tile("totoro.gif",3,2)
```
### Color Substitution
![](output/color-substitution-griffin.gif)
![](output/color-substitution-jean.gif)
![](output/color-substitution-totoro.gif)
```python

colorSubstitution("griffin.gif", 0.55, 0.15, 1.0)
colorSubstitution("jean.gif", 0.5, 0.5, 1.0)
colorSubstitution("totoro.gif", 0.5, 0.5, 1.0)
```
### Contrast Border
![](output/contrast-border-griffin.gif)
![](output/contrast-border-jean.gif)
![](output/contrast-border-totoro.gif)
```python
contrastBorder("griffin.gif",30)
contrastBorder("jean.gif",30)
contrastBorder("totoro.gif",100)
```
### Stretch
![](output/stretch-griffin.gif)
![](output/stretch-jean.gif)
![](output/stretch-totoro.gif)
```python

stretch("griffin.gif",math.pi,1)
stretch("jean.gif", 0.5,1)
stretch("totoro.gif",0.5,0.75)
```
