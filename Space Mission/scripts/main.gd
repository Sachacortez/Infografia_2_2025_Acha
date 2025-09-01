extends Node2D

@onready var door: Area2D = $Door
@onready var enemyA: Node2D = $EnemyA
@onready var hp_label: Label = $HpLabel
@onready var score_label: Label = $ScoreLabel

var score: int = 0

func _ready() -> void:
	$Key.key_collected.connect(on_key_collected)
	$Player.player_hurt.connect(on_player_hurt)
	$Gem.gem_collected.connect(on_gem_colected)
	$Door.player_entered.connect(on_finish)
	update_hp_label()
	
	get_tree().paused = false
	
func on_finish():
	get_tree().paused = true

func on_gem_colected():
	enemyA.death()

func on_key_collected():
	door.open()

func on_player_hurt():
	update_hp_label()

func update_hp_label():
	hp_label.text = "HP: " + str($Player.hp)
	
