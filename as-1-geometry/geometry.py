#we import all the libraries that our functions need here too
import random as r
import rhino3dm as rg

def createRandomPoints(count,rX, rY, radius):

    randomPts = []
    for i in range(count):

        #in each itereation generate some random points
        random_x = r.uniform(-rX, rX)
        random_y = r.uniform(-rY, rY)

        #create a point with rhino3dm
        random_pt = rg.Point3d(random_x, random_y, 0)

        Spheres = rg.Sphere(random_pt, radius)
        Spheres1 = Spheres.ToNurbsSurface()
        
        #add point to the list
        randomPts.append(Spheres1)

        


    return randomPts

    