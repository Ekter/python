from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import GeomNode

from panda3d.core import LVector3
import numpy as np
base = ShowBase()
base.disableMouse()
base.camera.setPos(0, -10, 0)
def makeCube(base,dimension,position,color_array_ugly=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]):
    # title = OnscreenText(text="Panda3D: Tutorial - Making a Cube Procedurally",
    #                      style=1, fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.07,
    #                      parent=base.a2dBottomRight, align=TextNode.ARight)
    # escapeEvent = OnscreenText(text="1: Set a Texture onto the Cube",
    #                            style=1, fg=(1, 1, 1, 1), pos=(0.06, -0.08),
    #                            align=TextNode.ALeft, scale=.05,
    #                            parent=base.a2dTopLeft)
    # spaceEvent = OnscreenText(text="2: Toggle Light from the front On/Off",
    #                           style=1, fg=(1, 1, 1, 1), pos=(0.06, -0.14),
    #                           align=TextNode.ALeft, scale=.05,
    #                           parent=base.a2dTopLeft)
    # upDownEvent = OnscreenText(text="3: Toggle Light from on top On/Off",
    #                            style=1, fg=(1, 1, 1, 1), pos=(0.06, -0.20),
    #                            align=TextNode.ALeft, scale=.05,
    #                            parent=base.a2dTopLeft)


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

        # texcoord.addData2f(0.0, 1.0)
        # texcoord.addData2f(0.0, 0.0)
        # texcoord.addData2f(1.0, 0.0)
        # texcoord.addData2f(1.0, 1.0)

        # Quads aren't directly supported by the Geom interface
        # you might be interested in the CardMaker class if you are
        # interested in rectangle though
        tris = GeomTriangles(Geom.UHDynamic)
        tris.addVertices(0, 1, 3)
        tris.addVertices(1, 2, 3)

        square = Geom(vdata)
        square.addPrimitive(tris)
        return square


    # Note: it isn't particularly efficient to make every face as a separate Geom.
    # instead, it would be better to create one Geom holding all of the faces.
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


    class MyTapper(DirectObject):

        def __init__(self):
            pass
            # self.testTexture = loader.loadTexture("maps/envir-reeds.png")
            # self.accept("1", self.toggleTex)
            # self.accept("2", self.toggleLightsSide)
            # self.accept("3", self.toggleLightsUp)

            # self.LightsOn = False
            # self.LightsOn1 = False
            # slight = Spotlight('slight')
            # slight.setColor((1, 1, 1, 1))
            # lens = PerspectiveLens()
            # slight.setLens(lens)
            # self.slnp = render.attachNewNode(slight)
            # self.slnp1 = render.attachNewNode(slight)

        # def toggleTex(self):
        #     global cube
        #     if cube.hasTexture():
        #         cube.setTextureOff(1)
        #     else:
        #         cube.setTexture(self.testTexture)

        # def toggleLightsSide(self):
        #     global cube
        #     self.LightsOn = not self.LightsOn

        #     if self.LightsOn:
        #         render.setLight(self.slnp)
        #         self.slnp.setPos(cube, 10, -400, 0)
        #         self.slnp.lookAt(10, 0, 0)
        #     else:
        #         render.setLightOff(self.slnp)

        # def toggleLightsUp(self):
        #     global cube
        #     self.LightsOn1 = not self.LightsOn1

        #     if self.LightsOn1:
        #         render.setLight(self.slnp1)
        #         self.slnp1.setPos(cube, 10, 0, 400)
        #         self.slnp1.lookAt(10, 0, 0)
        #     else:
        #         render.setLightOff(self.slnp1)


    t = MyTapper()
    base.run()

makeCube(base, np.array([3, 3, 3]), np.array([-1.5, -1.5, -1.5]))