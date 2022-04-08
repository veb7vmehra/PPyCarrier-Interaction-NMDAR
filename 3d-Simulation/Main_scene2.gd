extends Spatial
var membrane = load("res://membrane.tscn")
var gate = load("res://gate.tscn")
var ca = load("res://calcium.tscn")
var mg = load("res://mg.tscn")
var na = load("res://na.tscn")
var chl = load("res://cl.tscn")
var k = load("res://k.tscn")
var gl = load("res://gl.tscn")
var ur = load("res://ur.tscn")
var cell = load("res://cell.tscn")
var carrier = load("res://PolyPyrrole.tscn")

var rng = RandomNumberGenerator.new()

func setLength(obj, length):
	var l = obj.global_transform.basis.z.length()
	obj.scale.z = length/l

var time_now = 0
var time_start = 0

var speed = 5

# Called when the node enters the scene tree for the first time.
func _ready():
	time_start = OS.get_unix_time()
	rng.randomize()
	var screenX = $bg.global_transform.basis.x.length()*3
	var screenY = $bg.global_transform.basis.y.length()*3
	var screenZ = $bg.global_transform.basis.z.length()*3
	
	#var points = [Vector3(rng.randi_range(0, screenX), 0, -screenZ), Vector3(-screenX, 0, rng.randi_range(-screenZ, screenZ)), Vector3(rng.randi_range(0, screenX), 0, screenZ)]
	var vTemp = rng.randi_range(-screenZ, screenZ)
	
	var points1 = [Vector3(-screenX*4, 0, -screenZ), Vector3(-screenX*4, 0, 5), Vector3(-screenX*4, 0, screenZ)]
	var points2 = [Vector3(screenX*4, 0, -screenZ), Vector3(screenX*4, 0, 5), Vector3(screenX*4, 0, screenZ)]
	var midpoints = []
	var ca_no = 1
	var mg_no = 1
	var na_no = 145
	var chl_no = 120
	var k_no = 4
	var gl_no = 3
	var ur_no = 2
	
	for i in range(ca_no):
		var ca1 = ca.instance()
		ca1.global_transform.origin = Vector3(rng.randf_range(-screenX/2, screenX/2), rng.randf_range(-screenY/2, screenY/2), rng.randf_range(-screenZ/2, screenZ/2))
		$container.add_child(ca1)
	for i in range(mg_no):
		var mg1 = mg.instance()
		mg1.global_transform.origin = Vector3(rng.randf_range(-screenX/2, screenX/2), rng.randf_range(-screenY/2, screenY/2), rng.randf_range(-screenZ/2, screenZ/2))
		$container.add_child(mg1)
	for i in range(na_no):
		var na1 = na.instance()
		na1.global_transform.origin = Vector3(rng.randf_range(-screenX, screenX), rng.randf_range(-screenY, screenY), rng.randf_range(-screenZ, screenZ))
		$container.add_child(na1)
	for i in range(chl_no):
		var chl1 = chl.instance()
		chl1.global_transform.origin = Vector3(rng.randf_range(-screenX, screenX), rng.randf_range(-screenY, screenY), rng.randf_range(-screenZ, screenZ))
		$container.add_child(chl1)
	for i in range(k_no):
		var k1 = k.instance()
		k1.global_transform.origin = Vector3(rng.randf_range(-screenX/2, screenX/2), rng.randf_range(-screenY/2, screenY/2), rng.randf_range(-screenZ/2, screenZ/2))
		$container.add_child(k1)
	for i in range(gl_no):
		var gl1 = gl.instance()
		gl1.global_transform.origin = Vector3(rng.randf_range(-screenX, -screenX/2), rng.randf_range(-screenY, -screenY/2), rng.randf_range(-screenZ, -screenZ/2))
		$container.add_child(gl1)
	for i in range(ur_no):
		var ur1 = ur.instance()
		ur1.global_transform.origin = Vector3(rng.randf_range(screenX/2, screenX), rng.randf_range(screenY/2, screenY), rng.randf_range(screenZ/2, screenZ))
		$container.add_child(ur1)
	
	for i in range(3):
		"""
		var q = i+1
		if q >= 3:
			q = 0
		"""
		var mp = Vector3((points1[i].x+points2[i].x)/2, (points1[i].y+points2[i].y)/2, (points1[i].z+points2[i].z)/2)
		midpoints.append(mp)
		"""
		var poin = pointer.instance()
		poin.global_transform.origin = mp + Vector3(rng.randf_range(0, 1), 0, rng.randf_range(0, 1))
		add_child(poin)
		"""
		var mem1 = membrane.instance()
		var mem2 = membrane.instance()
		var gate1 = gate.instance()
		var gate2 = gate.instance()
		var diff = (points2[i] - points1[i])
		var p1 = points1[i] + (diff)*0.25 - diff.normalized()
		var p2 = points1[i] + (diff)*0.75 + diff.normalized()
		diff = Vector2(diff.x, diff.z)
		var angle = 90 - rad2deg(diff.angle())
		var length = points1[i].distance_to(points2[i])
		mem1.global_transform.origin = p1
		mem2.global_transform.origin = p2
		gate1.global_transform.origin = points1[i] + (points2[i] - points1[i])*0.5 - 2*(points2[i] - points1[i]).normalized()
		gate2.global_transform.origin = points1[i] + (points2[i] - points1[i])*0.5 + 2*(points2[i] - points1[i]).normalized()
		setLength(mem1, length * 0.25 - 1)
		setLength(mem2, length * 0.25 - 1)
		mem1.rotation_degrees.y = angle
		mem2.rotation_degrees.y = angle
		gate1.rotation_degrees.y = angle - 90
		gate2.rotation_degrees.y = angle - 90
		gate1.rotation_degrees.x = 90
		gate2.rotation_degrees.x = 90
		var cl = cell.instance()
		cl.global_transform.origin = points1[i] + (points2[i] - points1[i])*0.5 - Vector3(0, 3, 0)
		var l = cl.global_transform.basis.x.length()
		cl.scale.x = 0.25*length/l
		cl.rotation_degrees.x = 90
		cl.rotation_degrees.y = angle - 90
		add_child(cl)
		add_child(mem1)
		add_child(mem2)
		add_child(gate1)
		add_child(gate2)	
		
	var pyrrole = carrier.instance()
	pyrrole.global_transform.origin = Vector3(0, 0, 0)
	pyrrole.blocking(midpoints)
	$container.add_child(pyrrole)
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	time_now = OS.get_unix_time()
	var elapsed = time_now - time_start
	$timer.update_time(elapsed/60, elapsed%60)
	if Input.is_action_pressed("up"):
		$Camera2.translation.y += delta*speed
	if Input.is_action_pressed("down"):
		$Camera2.translation.y -= delta*speed
	if Input.is_action_pressed("right"):
		$Camera2.translation.x += delta*speed
	if Input.is_action_pressed("left"):
		$Camera2.translation.x -= delta*speed
	if Input.is_action_pressed("in"):
		$Camera2.translation.z -= delta*speed
	if Input.is_action_pressed("out"):
		$Camera2.translation.z += delta*speed
	if Input.is_action_pressed("rUp"):
		$Camera2.rotation_degrees.y = lerp(rotation_degrees.y, 0, 0.1)
	if Input.is_action_pressed("rDown"):
		$Camera2.rotation_degrees.y = lerp(rotation_degrees.y, 180, 0.1)
	if Input.is_action_pressed("rLeft"):
		$Camera2.rotation_degrees.y = lerp(rotation_degrees.y, -90, 0.1)
	if Input.is_action_pressed("rRight"):
		$Camera2.rotation_degrees.y = lerp(rotation_degrees.y, 180, 0.1)
