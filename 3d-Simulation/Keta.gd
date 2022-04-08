extends KinematicBody

var rng = RandomNumberGenerator.new()
var flag = true

func blocking(pos, num):
	for i in range(pos.size()):
		if pos[i].distance_to(global_transform.origin) < 2 and num[i] != 4:
			print("blocking ", i)
			global_transform.origin = pos[i] 
			flag = false
			num[i] = num[i] + 1
				
	if flag == true:
		vel.x = rng.randf_range(-10, 10)
		vel.z = rng.randf_range(-10, 10)
		vel.y = rng.randf_range(-10, 10)
		vel = move_and_slide(vel, Vector3.UP)
		
	return num

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var vel = Vector3.ZERO

# Called when the node enters the scene tree for the first time.
func _ready():
	rng.randomize()
	scale = Vector3(0.8, 0.8, 0.8)

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
	
