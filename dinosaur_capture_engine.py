
def capture_trigger(player, dinosaur):

    if dinosaur.get_health() < 0:
        player.add_dino(dinosaur)
        print(player.get_name() + " has successfully captured " + dinosaur.get_custom_name())
        return player.get_dino_team()
    else:
        print(player.get_name() + " failed to capture " + dinosaur.get_custom_name())
