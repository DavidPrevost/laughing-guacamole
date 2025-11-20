extends Area2D

# Individual screw that can be removed by tap-and-hold

signal screw_removed(screw_id)

@export var removal_time: float = 0.5  # Seconds to hold to remove

var screw_id: String = ""
var blocked_by: Array = []  # Piece IDs that block this screw
var is_blocked: bool = false
var is_being_removed: bool = false
var removal_progress: float = 0.0

@onready var sprite = $Sprite
@onready var progress_indicator = $ProgressIndicator
@onready var blocked_indicator = $BlockedIndicator

func _ready():
	input_event.connect(_on_input_event)
	progress_indicator.hide()
	blocked_indicator.hide()

func _process(delta):
	if is_being_removed and not is_blocked:
		removal_progress += delta / removal_time
		update_progress_visual()

		if removal_progress >= 1.0:
			remove_screw()

func set_blocked(blocked: bool) -> void:
	is_blocked = blocked
	if blocked:
		blocked_indicator.show()
		sprite.modulate = Color(0.6, 0.6, 0.6)
	else:
		blocked_indicator.hide()
		sprite.modulate = Color.WHITE

func _on_input_event(_viewport, event, _shape_idx):
	if event is InputEventScreenTouch or event is InputEventMouseButton:
		if event.pressed:
			start_removal()
		else:
			cancel_removal()

func start_removal() -> void:
	if is_blocked:
		# Visual feedback that it's blocked
		var tween = create_tween()
		tween.tween_property(sprite, "modulate", Color.RED, 0.1)
		tween.tween_property(sprite, "modulate", Color(0.6, 0.6, 0.6), 0.1)
		return

	is_being_removed = true
	removal_progress = 0.0
	progress_indicator.show()

func cancel_removal() -> void:
	is_being_removed = false
	removal_progress = 0.0
	progress_indicator.hide()
	update_progress_visual()

func update_progress_visual() -> void:
	# Update progress indicator using scale (simple approach without shader)
	if progress_indicator:
		var scale_val = removal_progress
		progress_indicator.scale = Vector2(scale_val, scale_val)
		progress_indicator.modulate.a = 0.5 + (removal_progress * 0.5)

func remove_screw() -> void:
	is_being_removed = false

	# Animate removal
	var tween = create_tween()
	tween.set_parallel(true)
	tween.tween_property(self, "scale", Vector2.ZERO, 0.2)
	tween.tween_property(self, "rotation", rotation + PI, 0.2)
	tween.tween_property(self, "modulate:a", 0.0, 0.2)

	await tween.finished

	screw_removed.emit(screw_id)
	queue_free()
