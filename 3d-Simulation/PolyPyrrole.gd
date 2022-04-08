extends KinematicBody
var pyrrole = load("res://pyrrole.tscn")
var keta = load("res://keta.tscn")
var r = 6.0
var rng = RandomNumberGenerator.new()
# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var blocked = [0, 0, 0]
var vec = Vector3(0.5, 0.5, 0.5)
# Called when the node enters the scene tree for the first time.
var pyrroles = []
var ketas = []
var broken = []
var vel = Vector3.ZERO

var time_now = 0
var time_start = 0

var brkTime = 0
var pos = []

var speed = 5

func blocking(points):
	pos = points

func _ready():
	time_start = OS.get_unix_time()
	rng.randomize()
	brkTime = rng.randi_range(20, 60)
	scale = Vector3(0.4, 0.4, 0.4)
	for x in range(-r, r):
		var ry = sqrt(r*r - (x*x))
		for y in range(-ry, ry):
			var z = sqrt(r*r - (x*x + y*y))
			var angleX = rad2deg(Vector2(y, z).angle())
			var angleY = rad2deg(Vector2(x, z).angle())
			var angleZ = rad2deg(Vector2(x, y).angle())
			var pyr1 = pyrrole.instance()
			pyr1.global_transform.origin = Vector3(x, y, z)
			pyr1.rotation_degrees = Vector3(angleX, angleY, angleZ)
			pyr1.scale = vec*2
			#pyr1.set_collision_mask(2)
			add_child(pyr1)
			pyrroles.append(pyr1)
			angleX = rad2deg(Vector2(y, -z).angle())
			angleY = rad2deg(Vector2(x, -z).angle())
			var pyr2 = pyrrole.instance()
			pyr2.global_transform.origin = Vector3(x, y, -z)
			pyr2.rotation_degrees = Vector3(angleX, angleY, angleZ)
			pyr2.scale = vec*2
			#pyr1.set_collision_mask(2)
			add_child(pyr2)
			pyrroles.append(pyr2)
	
# Called every frame. 'delta' is the elapsed time since the previous frame.

func _process(delta):
	time_now = OS.get_unix_time()
	var elapsed = time_now - time_start
	if elapsed < brkTime:
		vel.x = rng.randf_range(-3, 3)
		vel.z = rng.randf_range(-3, 3)
		vel.y = rng.randf_range(-3, 3)
		vel = move_and_slide(vel, Vector3.UP)
		rotate(Vector3(1, 0, 0), PI)
	else:
		if pyrroles.size() != 0:
			vel.x = rng.randf_range(-3, 3)
			vel.z = rng.randf_range(-3, 3)
			vel.y = rng.randf_range(-3, 3)
			vel = move_and_slide(vel, Vector3.UP)
			rotate(Vector3(1, 0, 0), PI)
			
			var temp = randi()%pyrroles.size()
			if broken.size() < 52:
				broken.append(pyrroles[temp])
			else:
				pyrroles[temp].queue_free()
			pyrroles.remove(temp)
			if ketas.size() < 21:
				var ket = keta.instance()
				ket.global_transform.origin = global_transform.origin
				#ket.scale = Vector3(16, 16, 160)
				#print(vec*16)
				add_child(ket)
				ketas.append(ket)
		
		if broken.size() != 0:
			if pyrroles.size() == 0:
				for i in range(broken.size()):
					var temp = Vector3.ZERO
					temp.x = rng.randf_range(-5, 5)
					temp.y = rng.randf_range(-5, 5)
					temp.z = rng.randf_range(-5, 5)
					temp = broken[i].move_and_slide(temp, Vector3.UP)
					broken[i].rotate(Vector3(1, 0, 0), PI)
			else:
				for i in range(broken.size()):
					var temp = Vector3.ZERO
					temp.x = rng.randf_range(-3, 3)
					temp.y = rng.randf_range(-3, 3)
					temp.z = rng.randf_range(-3, 3)
					temp = broken[i].move_and_slide(temp, Vector3.UP)
					broken[i].rotate(Vector3(1, 0, 0), PI)

				
		if ketas.size() != 0:
			for i in range(ketas.size()):
				blocked = ketas[i].blocking(pos, blocked)

