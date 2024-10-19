import math

def distance(point1, point2):
    try:
        if len(point1) != 3 or len(point2) != 3:
            raise ValueError("Each point must have exactly 3 coordinates.")
        
        dist = math.sqrt((point2[0] - point1[0])**2 + 
                         (point2[1] - point1[1])**2 + 
                         (point2[2] - point1[2])**2)
        return dist
    except TypeError:
        raise TypeError("The coordinates must be numbers.")

def main():
    try:
        x1, y1, z1 = map(float, input("Enter the first coordinate (x1, y1, z1): ").split(','))
        x2, y2, z2 = map(float, input("Enter the second coordinate (x2, y2, z2): ").split(','))
        
        point1 = (x1, y1, z1)
        point2 = (x2, y2, z2)
        
        dist = distance(point1, point2)
        
        print(f"The distance between {point1} and {point2} is: {dist}")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except TypeError as e:
        print(f"Type error: {e}")

if __name__ == "__main__":
    main()

