
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPoint(self):
        print(self.x, self.y)


def main():
    points = []

    points.append(Point(2, 3))
    points.append(Point(12, 30))
    points.append(Point(40, 50))
    points.append(Point(5, 1))
    points.append(Point(12, 10))
    points.append(Point(3, 4))

    for point in points:
        point.printPoint()

if __name__ == "__main__":
    main()
    

