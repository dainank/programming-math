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
- **scalar multiplication:**
    - process of multiplying vector by number
    - ordinary numbers therefore called *scalars*
- **vector subtraction:**
    - subtracting a vector from another creates:
        - v - w => the position of v relative to w
            - v - w => the arrow from tip of w to tip of v
                - provides displacement vector

## Classes
| Class     | Example Constructor   | Description                                       |
| --------- | --------------------- | ------------------------------------------------- |
| Polygon   | `Polygon(*vectors)`     | Draws polygon through list of vectors             |
| Points    | `Points(*vectors)`      | Draws list of points                              |
| Arrow     | `Arrow(tip, tail)`      | Draws arrow, tail is optional (defaults origin)   |
| Segment   | `Segment(start,end)`    | Draw line segment with two points                 |

