def which_prize(points):
    """
    Returns the prize-winning message, given a number of points
    """
    if points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"