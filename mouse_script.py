from safety_config import movement_threshold, shutdown_on_movement
from safety_utils import get_pos, mouse_tracker

initial = get_pos()
mouse_tracker(initial, shutdown_on_movement, movement_threshold)