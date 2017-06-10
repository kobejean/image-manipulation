# Example

### Original Images
![](docs/media/thumb-griffin.gif)
![](docs/media/thumb-jean.gif)
![](docs/media/thumb-totoro.gif)

### Favorites
![](docs/media/thumb-greyscale-totoro.gif)
![](docs/media/thumb-smart-border-totoro.gif)
![](docs/media/thumb-color-substitution-totoro.gif)

### Template
![](docs/media/thumb-template-griffin.gif)
![](docs/media/thumb-template-jean.gif)
![](docs/media/thumb-template-totoro.gif)
```python
template("griffin.gif")
template("jean.gif")
template("totoro.gif")
```
### Border
![](docs/media/thumb-border-griffin.gif)
![](docs/media/thumb-border-jean.gif)
![](docs/media/thumb-border-totoro.gif)
```python
border("griffin.gif", "#00FF00", 30)
border("jean.gif", "#FF0000", 30)
border("totoro.gif", "#0000FF", 100)
```
### Half
![](docs/media/thumb-half-griffin.gif)
![](docs/media/thumb-half-jean.gif)
![](docs/media/thumb-half-totoro.gif)
```python
half("griffin.gif")
half("jean.gif")
half("totoro.gif")
```
### Double
![](docs/media/thumb-double-griffin.gif)
![](docs/media/thumb-double-jean.gif)
![](docs/media/thumb-double-totoro.gif)
```python
double("griffin.gif")
double("jean.gif")
double("totoro.gif")
```
### Side Clone
![](docs/media/thumb-side-clone-griffin.gif)
![](docs/media/thumb-side-clone-jean.gif)
![](docs/media/thumb-side-clone-totoro.gif)
```python
sideClone("griffin.gif")
sideClone("jean.gif")
sideClone("totoro.gif")
```
### Down Clone
![](docs/media/thumb-down-clone-griffin.gif)
![](docs/media/thumb-down-clone-jean.gif)
![](docs/media/thumb-down-clone-totoro.gif)
```python
downClone("griffin.gif")
downClone("jean.gif")
downClone("totoro.gif")
```
### Greyscale
![](docs/media/thumb-greyscale-griffin.gif)
![](docs/media/thumb-greyscale-jean.gif)
![](docs/media/thumb-greyscale-totoro.gif)
```python

greyscale("griffin.gif")
greyscale("jean.gif")
greyscale("totoro.gif")
```
### Smart Border
![](docs/media/thumb-smart-border-griffin.gif)
![](docs/media/thumb-smart-border-jean.gif)
![](docs/media/thumb-smart-border-totoro.gif)
```python

smartBorder("griffin.gif",30)
smartBorder("jean.gif",30)
smartBorder("totoro.gif",100)
```
### Scale
![](docs/media/thumb-scale0.25x-griffin.gif)
![](docs/media/thumb-scale0.25x-jean.gif)
![](docs/media/thumb-scale0.25x-totoro.gif)
```python

# scale_factor = float(input("SCALE FACTOR:"))
scale_factor = 0.25
scale("griffin.gif", scale_factor)
scale("jean.gif", scale_factor)
scale("totoro.gif", scale_factor)
```
### Smart Clone
![](docs/media/thumb-smart-clone-griffin.gif)
![](docs/media/thumb-smart-clone-jean.gif)
![](docs/media/thumb-smart-clone-totoro.gif)
```python

smartClone("griffin.gif",3,2)
smartClone("jean.gif",3,2)
smartClone("totoro.gif",3,2)
```
### Tile
![](docs/media/thumb-tile-griffin.gif)
![](docs/media/thumb-tile-jean.gif)
![](docs/media/thumb-tile-totoro.gif)
```python
tile("griffin.gif",3,2)
tile("jean.gif",3,2)
tile("totoro.gif",3,2)
```
### Color Substitution
![](docs/media/thumb-color-substitution-griffin.gif)
![](docs/media/thumb-color-substitution-jean.gif)
![](docs/media/thumb-color-substitution-totoro.gif)
```python

colorSubstitution("griffin.gif", 0.55, 0.15, 1.0)
colorSubstitution("jean.gif", 0.5, 0.5, 1.0)
colorSubstitution("totoro.gif", 0.5, 0.5, 1.0)
```
### Contrast Border
![](docs/media/thumb-contrast-border-griffin.gif)
![](docs/media/thumb-contrast-border-jean.gif)
![](docs/media/thumb-contrast-border-totoro.gif)
```python
contrastBorder("griffin.gif",30)
contrastBorder("jean.gif",30)
contrastBorder("totoro.gif",100)
```
### Stretch
![](docs/media/thumb-stretch-griffin.gif)
![](docs/media/thumb-stretch-jean.gif)
![](docs/media/thumb-stretch-totoro.gif)
```python

stretch("griffin.gif",math.pi,1)
stretch("jean.gif", 0.5,1)
stretch("totoro.gif",0.5,0.75)
```
