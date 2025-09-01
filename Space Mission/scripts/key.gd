extends Area2D

signal key_collected

func _on_body_entered(body: Node2D) -> void:
	key_collected.emit()
	queue_free()
