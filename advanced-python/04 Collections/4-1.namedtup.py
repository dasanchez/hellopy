# Demonstrate the usage of namdtuple objects

import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")
    Point3D = collections.namedtuple("Point3D", "x y z")

    p2d = Point(10, 20)
    p3d = Point3D(10, 20, 30)
    print(p2d)
    print(p3d)
    print(p3d.z)

    # use _replace to create a new instance
    p2d_b = p2d._replace(x=40)
    print(p2d_b)

if __name__ == "__main__":
    main()
