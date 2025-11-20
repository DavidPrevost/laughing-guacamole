extends Button

signal level_selected(level_number)

var level_number: int = 1
var is_unlocked: bool = false
var is_completed: bool = false

func _ready():
	update_display()
	pressed.connect(_on_pressed)

func update_display() -> void:
	text = str(level_number)

	if not is_unlocked:
		disabled = true
		modulate = Color(0.5, 0.5, 0.5)
	elif is_completed:
		modulate = Color(0.5, 1.0, 0.5)  # Green tint for completed
	else:
		modulate = Color.WHITE

func _on_pressed() -> void:
	if is_unlocked:
		level_selected.emit(level_number)
