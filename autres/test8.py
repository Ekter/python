# import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import GeomNode

from panda3d.core import LVector3
import numpy as np


class World(DirectObject):
    def __init__(self,base):
        base.setBackgroundColor(1, 1, 1)
        base.disableMouse()
        # self.environmentModel = loader.loadModel("models/environment")
        # self.environmentModel.reparentTo(render)
        # self.environmentModel.setPos(0, 20, -10)
        self.makeCube(np.array([3, 3, 3]), np.array([0,0,0]),trans=False)
        self.cameraModel = loader.loadModel("models/camera")
        self.cameraModel.reparentTo(render)
        self.cameraModel.hide()
        self.cameraModel.setPos(0, 15, 0)
        
        base.camera.reparentTo(self.cameraModel)
        base.camera.setY(base.camera, 5)
        
        self.keyMap = {"w" : False, "s" : False, "a" : False, "d" : False, "space" : False, "shift" : False}
        def setKey(key, value):
            self.keyMap[key] = value
        self.accept("w", setKey, ["w", True])
        self.accept("s", setKey, ["s", True])
        self.accept("a", setKey, ["a", True])
        self.accept("d", setKey, ["d", True])
        # self.accept("escape", sys.exit)
        self.accept("space", setKey, ["space", True])
        self.accept("shift", setKey, ["shift", True])
        self.accept("w-up", setKey, ["w", False])
        self.accept("s-up", setKey, ["s", False])
        self.accept("a-up", setKey, ["a", False])
        self.accept("d-up", setKey, ["d", False])
        self.accept("space-up", setKey, ["space", False])
        self.accept("shift-up", setKey, ["shift", False])
        
        taskMgr.add(self.cameraControl, "Camera Control")
        
    # def setKey(self, key, value):
    #     self.keyMap[key] = value
    
    def cameraControl(self, task):
        dt = globalClock.getDt()
        if(dt > .20):
            return task.cont
            
        if(base.mouseWatcherNode.hasMouse() == True):
            mpos = base.mouseWatcherNode.getMouse()
            base.camera.setP(mpos.getY() * 30)
            base.camera.setH(mpos.getX() * -50)
            if (mpos.getX() < 0.1 and mpos.getX() > -0.1 ):
                self.cameraModel.setH(self.cameraModel.getH())
            else:
                self.cameraModel.setH(self.cameraModel.getH() + mpos.getX() * -1)
            
        if(self.keyMap["w"] == True):
            self.cameraModel.setY(self.cameraModel, 150 * dt)
            print("camera moving forward")
            return task.cont
        elif(self.keyMap["s"] == True):
            self.cameraModel.setY(self.cameraModel, -150 * dt)
            print("camera moving backwards")
            return task.cont
        elif(self.keyMap["a"] == True):
            self.cameraModel.setX(self.cameraModel, -100 * dt)
            print("camera moving left")
            return task.cont
        elif(self.keyMap["d"] == True):
            self.cameraModel.setX(self.cameraModel, 100 * dt)
            print("camera moving right")
            return task.cont
        elif(self.keyMap["space"] == True):
            self.cameraModel.setZ(self.cameraModel, 100 * dt)
            print("camera moving up")
            return task.cont
        elif(self.keyMap["shift"] == True):
            self.cameraModel.setZ(self.cameraModel, -100 * dt)
            print("camera moving down")
            return task.cont
        else:
            return task.cont
    
    def makeCube(self,dimension,position,color_array_ugly=[[1,0,0,0.5],[1,0,0,0.5],[1,0,0,0.5],[1,0,0,0.5]],trans=False):
        # You can't normalize inline so this is a helper function
        def normalized(*args):
            myVec = LVector3(*args)
            myVec.normalize()
            return myVec


        # helper function to make a square given the Lower-Left-Hand and
        # Upper-Right-Hand corners

        def makeSquare(x1, y1, z1, x2, y2, z2):
            format = GeomVertexFormat.getV3n3cpt2()
            vdata = GeomVertexData('square', format, Geom.UHDynamic)

            vertex = GeomVertexWriter(vdata, 'vertex')
            normal = GeomVertexWriter(vdata, 'normal')
            color = GeomVertexWriter(vdata, 'color')
            texcoord = GeomVertexWriter(vdata, 'texcoord')

            # make sure we draw the sqaure in the right plane
            if x1 != x2:
                vertex.addData3(x1, y1, z1)
                vertex.addData3(x2, y1, z1)
                vertex.addData3(x2, y2, z2)
                vertex.addData3(x1, y2, z2)

                normal.addData3(normalized(2 * x1 - 1, 2 * y1 - 1, 2 * z1 - 1))
                normal.addData3(normalized(2 * x2 - 1, 2 * y1 - 1, 2 * z1 - 1))
                normal.addData3(normalized(2 * x2 - 1, 2 * y2 - 1, 2 * z2 - 1))
                normal.addData3(normalized(2 * x1 - 1, 2 * y2 - 1, 2 * z2 - 1))

            else:
                vertex.addData3(x1, y1, z1)
                vertex.addData3(x2, y2, z1)
                vertex.addData3(x2, y2, z2)
                vertex.addData3(x1, y1, z2)

                normal.addData3(normalized(2 * x1 - 1, 2 * y1 - 1, 2 * z1 - 1))
                normal.addData3(normalized(2 * x2 - 1, 2 * y2 - 1, 2 * z1 - 1))
                normal.addData3(normalized(2 * x2 - 1, 2 * y2 - 1, 2 * z2 - 1))
                normal.addData3(normalized(2 * x1 - 1, 2 * y1 - 1, 2 * z2 - 1))

            # adding different colors to the vertex for visibility
            [color.addData4f(*l) for l in color_array_ugly]

            # Quads aren't directly supported by the Geom interface
            # you might be interested in the CardMaker class if you are
            # interested in rectangle though
            tris = GeomTriangles(Geom.UHDynamic)#Geom.UHDynamic)UHStatic
            tris.addVertices(0, 1, 3)
            tris.addVertices(1, 2, 3)

            square = Geom(vdata)
            square.addPrimitive(tris)
            # square.setDepthWrite(1)
            return square


        # Note: it isn't particularly efficient to make every face as a separate Geom.
        # instead, it would be better to create one Geom holding all of the faces. TODO change this
        square0 = makeSquare(position[0], position[1], position[2], position[0]+dimension[0], position[1], position[2]+dimension[2])
        square1 = makeSquare(position[0], position[1]+dimension[1], position[2], position[0]+dimension[0], position[1]+dimension[1], position[2]+dimension[2])
        square2 = makeSquare(position[0], position[1]+dimension[1], position[2]+dimension[2], position[0]+dimension[0], position[1], position[2]+dimension[2])
        square3 = makeSquare(position[0], position[1]+dimension[1], position[2], position[0]+dimension[0], position[1], position[2])
        square4 = makeSquare(position[0], position[1], position[2], position[0], position[1]+dimension[1], position[2]+dimension[2])
        square5 = makeSquare(position[0]+dimension[0], position[1], position[2], position[0]+dimension[0], position[1]+dimension[1], position[2]+dimension[2])
        snode = GeomNode('square')
        snode.addGeom(square0)
        snode.addGeom(square1)
        snode.addGeom(square2)
        snode.addGeom(square3)
        snode.addGeom(square4)
        snode.addGeom(square5)

        cube = render.attachNewNode(snode)
        cube.hprInterval(1.5, (360, 1, 1)).loop()

        # OpenGl by default only draws "front faces" (polygons whose vertices are
        # specified CCW).
        cube.setTwoSided(True)
        cube.setTransparency(True)
        if trans:
            cube.setRenderModeWireframe()

        t = DirectObject()

base = ShowBase()
base.disableMouse()
base.camera.setPos(0, -10, 0)
w = World(base)
base.run()