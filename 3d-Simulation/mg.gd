extends KinematicBody

var rng = RandomNumberGenerator.new()

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var vel = Vector3.ZERO

# Called when the node enters the scene tree for the first time.
func _ready():
	rng.randomize()
	scale = Vector3(0.15, 0.15, 0.15)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	vel.x = rng.randf_range(-3, 3)
	vel.z = rng.randf_range(-3, 3)
	vel.y = rng.randf_range(-3, 3)
	vel = move_and_slide(vel, Vector3.UP)
