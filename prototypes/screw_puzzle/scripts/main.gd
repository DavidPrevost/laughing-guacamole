extends Node

# Main scene controller - manages screen transitions

enum Screen { MENU, LEVEL_SELECT, GAME, WIN, AD }

@onready var menu_screen = $MenuScreen
@onready var level_select_screen = $LevelSelectScreen
@onready var game_screen = $GameScreen
@onready var win_screen = $WinScreen
@onready var ad_screen = $AdScreen

var current_screen: Screen = Screen.MENU
var levels_since_ad: int = 0
const AD_FREQUENCY: int = 3  # Show ad placeholder every N levels

func _ready():
	# Connect signals
	game_screen.get_node("Game").level_won.connect(_on_level_won)

	show_screen(Screen.MENU)

func show_screen(screen: Screen) -> void:
	menu_screen.hide()
	level_select_screen.hide()
	game_screen.hide()
	win_screen.hide()
	ad_screen.hide()

	current_screen = screen

	match screen:
		Screen.MENU:
			menu_screen.show()
		Screen.LEVEL_SELECT:
			level_select_screen.show()
			level_select_screen.refresh_levels()
		Screen.GAME:
			game_screen.show()
		Screen.WIN:
			win_screen.show()
			win_screen.setup(GameState.current_level)
		Screen.AD:
			ad_screen.show()

func start_level(level_num: int) -> void:
	show_screen(Screen.GAME)
	game_screen.get_node("Game").start_level(level_num)

func _on_level_won() -> void:
	levels_since_ad += 1

	# Check if we should show ad placeholder
	if levels_since_ad >= AD_FREQUENCY:
		levels_since_ad = 0
		show_screen(Screen.AD)
	else:
		show_screen(Screen.WIN)

# Button handlers (connected in scene)
func _on_play_pressed() -> void:
	show_screen(Screen.LEVEL_SELECT)

func _on_back_to_menu_pressed() -> void:
	show_screen(Screen.MENU)

func _on_next_level_pressed() -> void:
	var next_level = GameState.current_level + 1
	if next_level <= GameState.total_levels:
		start_level(next_level)
	else:
		show_screen(Screen.LEVEL_SELECT)

func _on_replay_level_pressed() -> void:
	start_level(GameState.current_level)

func _on_level_select_pressed() -> void:
	show_screen(Screen.LEVEL_SELECT)

func _on_ad_continue_pressed() -> void:
	show_screen(Screen.WIN)
