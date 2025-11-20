extends Control

# Win screen shown after completing a level

@onready var level_label = $VBoxContainer/LevelLabel
@onready var next_button = $VBoxContainer/NextButton

func setup(completed_level: int) -> void:
	level_label.text = "Level " + str(completed_level) + " Complete!"

	# Hide next button if this was the last level
	if completed_level >= GameState.total_levels:
		next_button.hide()
	else:
		next_button.show()
