extends Node

# Persistent game state - autoloaded

signal level_unlocked(level_number)
signal level_completed(level_number)

const SAVE_PATH = "user://save_data.json"

var current_level: int = 1
var unlocked_levels: Array = [1]
var completed_levels: Array = []
var total_levels: int = 20

func _ready():
	load_game()

func unlock_level(level_num: int) -> void:
	if level_num not in unlocked_levels:
		unlocked_levels.append(level_num)
		unlocked_levels.sort()
		level_unlocked.emit(level_num)
		save_game()

func complete_level(level_num: int) -> void:
	if level_num not in completed_levels:
		completed_levels.append(level_num)
		completed_levels.sort()
		level_completed.emit(level_num)

	# Unlock next level
	if level_num < total_levels:
		unlock_level(level_num + 1)

	save_game()

func is_level_unlocked(level_num: int) -> bool:
	return level_num in unlocked_levels

func is_level_completed(level_num: int) -> bool:
	return level_num in completed_levels

func save_game() -> void:
	var save_data = {
		"current_level": current_level,
		"unlocked_levels": unlocked_levels,
		"completed_levels": completed_levels
	}

	var file = FileAccess.open(SAVE_PATH, FileAccess.WRITE)
	if file:
		file.store_string(JSON.stringify(save_data))
		file.close()

func load_game() -> void:
	if not FileAccess.file_exists(SAVE_PATH):
		return

	var file = FileAccess.open(SAVE_PATH, FileAccess.READ)
	if file:
		var json = JSON.new()
		var error = json.parse(file.get_as_text())
		file.close()

		if error == OK:
			var data = json.data
			current_level = data.get("current_level", 1)
			unlocked_levels = data.get("unlocked_levels", [1])
			completed_levels = data.get("completed_levels", [])

func reset_progress() -> void:
	current_level = 1
	unlocked_levels = [1]
	completed_levels = []
	save_game()
