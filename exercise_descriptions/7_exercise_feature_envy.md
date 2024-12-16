# Feature Envy

> Exercise branch: **solution_primitive_obsession**
>
> Solution branch: **solution_feature_envy**

## Exercise

### Solve the feature envies for validating radius and formatting points and radius

## Exercise part 1: Radius value validation

> Move radius value validation to the ```Radius``` constructor.

## Exercise part 2: format Circle & Radius

> ```Circle::format()``` formats both ```(x, y)``` and ```Radius``` as a string.
> However, in this case, ```Point``` and ```Radius```
> could actually provide own ```format()``` method
> to separate these concerns from ```Circle```.
> To do so, follow these steps:
>
>    Extract a variable for the part of the string that formats a ```Point``` “```(x, y)```”
> within ```Circle::format()```
>    * Move classes Point and Radius to their own files
>    * Wrap the right side of the variable in an own “```format_point()```” method
>    * Move this method to the ```Point``` and rename it to ```format()```.
>    * Clean up any unused parameters and variables
>    * Do the same with ```Radius``` formatting

## Exercise part 3: introduce distance_to(Point) method

> There is another feature envy in the contains method.
> The calculation of the distance between the center point of the circle and the passed point
> can actually be rewritten, such that the final result reads
> ```self.center.distance_to(point) <= self.radius```. That way, ```Point``` can provide a ```distance_to()``` a
> reasonable functionality others would expect on a point.
> To do so:
>   * Introduce a variable ```point = Point(x_coords[i], y_coords[i])```
>   * Use point.x and point.y where x_coords[i] and y_coords[i] were used
>   * Use math.sqrt(square(delta_x) + square(delta_y)) to calculate the distance between the two points
>   * wrap and move the calculation to the ```Point``` class as a ```distance_to(point:Point)``` method.