extends Node2D

# A piece/plate that blocks screws and falls when its holding screws are removed

var piece_id: String = ""
var held_by: Array = []  # Screw IDs that hold this piece
var size: Vector2 = Vector2(100, 100)

@onready var sprite = $Sprite

func _ready():
	update_visual()

func update_visual() -> void:
	if sprite:
		sprite.size = size

func fall_away() -> void:
	# Animate the piece falling off screen
	var tween = create_tween()
	tween.set_parallel(true)

	# Random fall direction
	var fall_direction = Vector2(randf_range(-200, 200), 800)
	var fall_rotation = randf_range(-PI, PI)

	tween.tween_property(self, "position", position + fall_direction, 0.5).set_ease(Tween.EASE_IN)
	tween.tween_property(self, "rotation", fall_rotation, 0.5)
	tween.tween_property(self, "modulate:a", 0.0, 0.5)

	await tween.finished
	queue_free()
