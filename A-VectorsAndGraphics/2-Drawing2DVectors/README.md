# 2 - Drawing 2D Vectors
## Key Concepts
- coordinates are often ordered as *ordered pair (tuple)*
- **vector addition:**
    - given two input vectors, add respective x and y coordinates
- **components of vector:**
    - e.g. (4, 3) => (4, 0) & (0, 3)
- **Pythagorean theorem:**
    - provides distance of diagonal with components
    -  a^2 + b^2 = c^2
- **scalar multiplication:**c
    - process of multiplying vector by number
    - ordinary numbers therefore called *scalars*
- **vector subtraction:**
    - subtracting a vector from another creates:
        - v - w => the position of v relative to w
            - v - w => the arrow from tip of w to tip of v
                - provides displacement vector
- **coordinate types:**
    - *Cartesian coordinates*   : (1, 1)
    - *polar coordinates*       : (5, 37°) | measure 37° anticlockwise from x axis.
        - every angle gives constant ratio; e.g. 1:1 (also known as the tangent)
        - π radians = 180° or 2π radians = 180°
        - asisn, csin, atan can all be used to directly find angle

## Classes
| Class     | Example Constructor   | Description                                       |
| --------- | --------------------- | ------------------------------------------------- |
| Polygon   | `Polygon(*vectors)`     | Draws polygon through list of vectors             |
| Points    | `Points(*vectors)`      | Draws list of points                              |
| Arrow     | `Arrow(tip, tail)`      | Draws arrow, tail is optional (defaults origin)   |
| Segment   | `Segment(start,end)`    | Draw line segment with two points                 |

