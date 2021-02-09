########################## Minecraft: Python Editon (pycraft) ##########################
import os
try:
    from ursina import *
    from ursina.prefabs.first_person_controller import FirstPersonController
except:
    os.system('pip install ursina')

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
roo_texture = load_texture('assets/roo_texture.png')
house_texture = load_texture('assets/house_texture.png')

punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)

# window.fps_counter.enabled = False
window.exit_button.visible = False

sayı=1

def update():
    global sayı

    if held_keys['left mouse'] or held_keys['right mouse']:hand.active()
    else:hand.passive()

    if held_keys['1']:sayı=1
    if held_keys['2']:sayı=2
    if held_keys['3']:sayı=3
    if held_keys['4']:sayı=4
    if held_keys['5']:sayı=5
    if held_keys['6']:sayı=6
    if held_keys['7']:sayı=7


class Voxel(Button):
    def __init__(self, position = (0,0,0),voxelColor = color.white, Texture = grass_texture):
        super().__init__(
            parent= scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5, 
            texture = Texture,
            color = voxelColor,
            scale = 0.5
        )

    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                punch_sound.play()
                if sayı == 1: voxel = Voxel(position = self.position + mouse.normal, voxelColor = color.white, Texture= grass_texture)
                if sayı == 2: voxel = Voxel(position = self.position + mouse.normal, voxelColor = color.white, Texture= stone_texture)
                if sayı == 3: voxel = Voxel(position = self.position + mouse.normal, voxelColor = color.white, Texture= brick_texture)
                if sayı == 4: voxel = Voxel(position = self.position + mouse.normal, voxelColor = color.white, Texture= dirt_texture)
                if sayı == 5: voxel = Voxel(position = self.position + mouse.normal, voxelColor = color.white, Texture= sky_texture)
                if sayı == 6: voxel = Voxel(position = self.position + mouse.normal, voxelColor = color.white, Texture= arm_texture)
                if sayı == 7: voxel = Voxel(position = self.position + mouse.normal, voxelColor = color.orange, Texture= brick_texture)
            if key == "right mouse down":
                punch_sound.play()
                destroy(self)

class Küre(Button):
    def __init__(self, position = (0,0,0), voxelColor = color.white):
        super().__init__(
            parent = scene,
            position = position,
            model = "sphere",
            origin_y = 0.5, 
            texture = "white_sphere",
            color = voxelColor,
            scale = 1
        )
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                punch_sound.play()
                if sayı == 1: voxel = Küre(position = self.position + mouse.normal, voxelColor = color.red)
                if sayı == 2: voxel = Küre(position = self.position + mouse.normal, voxelColor = color.blue)
                if sayı == 3: voxel = Küre(position = self.position + mouse.normal, voxelColor = color.yellow)
                if sayı == 4: voxel = Küre(position = self.position + mouse.normal, voxelColor = color.green)
                if sayı == 5: voxel = Küre(position = self.position + mouse.normal, voxelColor = color.black)
                if sayı == 6: voxel = Küre(position = self.position + mouse.normal, voxelColor = color.white)
                if sayı == 7: voxel = Küre(position = self.position + mouse.normal, voxelColor = color.pink)
            if key == "right mouse down":
                punch_sound.play()
                destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Player(FirstPersonController):
    def __init__(self , position=(10,5,10)):
        super().__init__(
            position=position
        )
    
    

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)


for z in range(30):
    for x in range(30):
        for y in range(4):
            voxel = Voxel(position = (x,y,z), voxelColor=color.color(0,0,random.uniform(0.9,1)))
küre = Küre(position=(5,5,5),voxelColor=color.red)

player = Player()
sky = Sky()
hand = Hand()

app.run()