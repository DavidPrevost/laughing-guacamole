extends Node2D

# Main game controller

signal screw_removed(screw_id)
signal piece_removed(piece_id)
signal level_won

const SCREW_SCENE = preload("res://scenes/screw.tscn")
const PIECE_SCENE = preload("res://scenes/piece.tscn")

@onready var screws_container = $ScrewsContainer
@onready var pieces_container = $PiecesContainer
@onready var hint_label = $UI/HintLabel
@onready var level_label = $UI/LevelLabel

var levels_data: Array = []
var current_level_data: Dictionary = {}
var screws: Dictionary = {}  # id -> Screw node
var pieces: Dictionary = {}  # id -> Piece node
var removed_screws: Array = []

func _ready():
	load_levels_data()

func load_levels_data() -> void:
	var file = FileAccess.open("res://levels/levels.json", FileAccess.READ)
	if file:
		var json = JSON.new()
		json.parse(file.get_as_text())
		levels_data = json.data.get("levels", [])
		file.close()

func start_level(level_num: int) -> void:
	clear_level()

	# Find level data
	for level in levels_data:
		if level.get("number") == level_num:
			current_level_data = level
			break

	if current_level_data.is_empty():
		push_error("Level not found: ", level_num)
		return

	GameState.current_level = level_num

	# Update UI
	level_label.text = "Level " + str(level_num)

	if current_level_data.get("tutorial", false) and current_level_data.has("hint"):
		hint_label.text = current_level_data.get("hint", "")
		hint_label.show()
	else:
		hint_label.hide()

	# Create pieces first (they need to exist for blocking checks)
	for piece_data in current_level_data.get("pieces", []):
		create_piece(piece_data)

	# Create screws
	for screw_data in current_level_data.get("screws", []):
		create_screw(screw_data)

	# Update initial blocking states
	update_all_blocking_states()

func clear_level() -> void:
	for child in screws_container.get_children():
		child.queue_free()
	for child in pieces_container.get_children():
		child.queue_free()

	screws.clear()
	pieces.clear()
	removed_screws.clear()
	current_level_data = {}

func create_screw(data: Dictionary) -> void:
	var screw = SCREW_SCENE.instantiate()
	screw.screw_id = data.get("id", "")
	screw.position = Vector2(data.get("x", 0), data.get("y", 0))
	screw.blocked_by = data.get("blocked_by", [])

	screw.screw_removed.connect(_on_screw_removed)

	screws_container.add_child(screw)
	screws[screw.screw_id] = screw

func create_piece(data: Dictionary) -> void:
	var piece = PIECE_SCENE.instantiate()
	piece.piece_id = data.get("id", "")
	piece.position = Vector2(data.get("x", 0), data.get("y", 0))
	piece.size = Vector2(data.get("width", 100), data.get("height", 100))
	piece.held_by = data.get("held_by", [])

	pieces_container.add_child(piece)
	pieces[piece.piece_id] = piece

func update_all_blocking_states() -> void:
	# Update which screws are blocked
	for screw_id in screws:
		var screw = screws[screw_id]
		var is_blocked = false

		for blocker_id in screw.blocked_by:
			if blocker_id in pieces:
				is_blocked = true
				break

		screw.set_blocked(is_blocked)

func _on_screw_removed(screw_id: String) -> void:
	removed_screws.append(screw_id)
	screws.erase(screw_id)
	screw_removed.emit(screw_id)

	# Check if any pieces should fall
	check_pieces_to_remove()

	# Update blocking states
	update_all_blocking_states()

	# Check win condition
	if screws.is_empty():
		_on_level_won()

func check_pieces_to_remove() -> void:
	var pieces_to_remove = []

	for piece_id in pieces:
		var piece = pieces[piece_id]
		var all_screws_removed = true

		for holder_id in piece.held_by:
			if holder_id in screws:
				all_screws_removed = false
				break

		if all_screws_removed:
			pieces_to_remove.append(piece_id)

	# Remove pieces that are no longer held
	for piece_id in pieces_to_remove:
		var piece = pieces[piece_id]
		piece.fall_away()
		pieces.erase(piece_id)
		piece_removed.emit(piece_id)

func _on_level_won() -> void:
	await get_tree().create_timer(0.5).timeout
	level_won.emit()
	GameState.complete_level(GameState.current_level)
