"""
a conversation takes place between two partners

a conversation ends when one of the partners reaches zero health OR chooses to leave
when a partner reaches zero health, they are unable to continue
the first partner to reach zero health *loses*, the other partner wins


A conversation is broken into a series of turns.

The conversation class will expose a play_turn method that takes as parameters
    a move for player 1 and a move for player 2

    a move can be an attack, an item, or 'QUIT'

play_turn will then play out the logic of the turn
    including damage and effects in full to the
    character objects contained in the conversation
    
    as it does this, it will keep a list of the events as they occur in sequence
    this is called the turn
    
    each turn event contains instructions for the battle UI to display
    
    the notion is that we will calculate all the effects of the turn in the background,
    and then give the UI its instructions to display what happened

    turn events will be described in more detail below

anatomy of a turn:
    
    play_turn(player moves)
    turn = []
    
    
    for each player in _get_turn_order():
        if player move is QUIT
            turn <- player quits
            return turn
        
        if move is an attack
            turn <- player attacks other player with attack
            damage = calculate_damage
            turn <- other player takes {damage}
            if attack.effects
                if effect happens
                    turn <- player confers condition onto other player
            if other player is out of health
                turn <- player wins
                return turn

        else if move is item
            handle items . . . (under construction)
            
        if player.condition
            if condition.has_recurring_effect
                result = apply_recurring_effect
                turn.append(result)
            if player is out of health
                turn <- other player wins
                return turn
    return turn

"""