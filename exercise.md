# Long Method / Function and Loop Split 

> Exercise branch: **solution_feature_envy**
>
> Solution branch: **solution_loop_split**

## Exercise

### Split the method ```count_points_within_circle``` into their separate concerns!

## Exercise part 1
> ```contains``` still uses the primitive ```x_coords```, ```y_coords```, and ```i``` parameters.
> 
> * Introduce a ```Point``` as an input parameter of ```contains```.

## Exercise part 2
> The ```count_points_within_circle``` method now has two separate concerns:
> * Concern 1: creation of points (including validation of inputs)
> * Concern 2: counting the number of points contained within the circle.
> 
> To solve this, split the loop into two separate loops:
>  * Loop 1 creates a list of ```Point```s with a ```Point``` for each ```xCoords[i]``` and ```yCoords[i]``` pair.
>  * Loop 2 iterates over this list of points and counts points contained within the circle.
