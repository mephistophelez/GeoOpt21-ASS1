from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/RANDOM_SPHERES",
    name = "More Random Points",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("add a radius","R", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       hs.HopsSurface("Spheres", "SP","cool spheres", hs.HopsParamAccess.LIST)
    ]
)
def moreRandomPoints(count,rX, rY,radius):

    randomPts = geo.createRandomPoints(count, rX, rY,radius)
    return randomPts





if __name__== "__main__":
    app.run(debug=True)