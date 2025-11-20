extends Control

# Level selection grid

const BUTTON_SCENE = preload("res://scenes/level_button.tscn")

@onready var grid = $ScrollContainer/GridContainer

func _ready():
	refresh_levels()

func refresh_levels() -> void:
	# Clear existing buttons
	for child in grid.get_children():
		child.queue_free()

	# Create button for each level
	for i in range(1, GameState.total_levels + 1):
		var button = BUTTON_SCENE.instantiate()
		button.level_number = i
		button.is_unlocked = GameState.is_level_unlocked(i)
		button.is_completed = GameState.is_level_completed(i)
		button.level_selected.connect(_on_level_selected)
		grid.add_child(button)

func _on_level_selected(level_num: int) -> void:
	get_parent().start_level(level_num)
