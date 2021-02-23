class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

if __name__ == '__main__':
    pt1 = Point()
    pt3 = pt2 = pt1

    print(pt2.x, pt2.y)
    print(pt3.x, pt3.y)
    # print(id(pt1), id(pt2), id(pt3))  # prints the ids of the obejcts
    # del pt1, pt2, pt3
    # del pt2
    # del pt3
