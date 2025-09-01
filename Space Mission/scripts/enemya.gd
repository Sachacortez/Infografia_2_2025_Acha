extends Node2D

@onready var animation_player: AnimationPlayer = $AnimationPlayer

@export var speed: float = 150.0
@export var max_distance: float = 200.0

var start_position: Vector2
var direction: int = 1

func _ready() -> void:
	animation_player.play("Active")
	start_position = global_position

func death():
	queue_free()
