#!/usr/bin/python3

def canUnlockAll(boxes):
    opened_boxes = {0}
    key_queue = boxes[0]
    while key_queue:
        key = key_queue.pop(0)
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            key_queue.extend(boxes[key])
    return len(opened_boxes) == len(boxes)
