#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened or not.

    Args:
        boxes (list of lists): A list of boxes, each containing keys to other boxes.

    Returns:
        True if all boxes can be opened, False otherwise.
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
