# TODO

## Feature: Encounter backend
Goal: provide a back end interface for all the computation involved in running an encounter from
beginning to end

    [ ] support for moving between conversations

### Sub feature: Conversation backend
Goal: provide back end interface for all the computations involved in running a conversation.

    [x] provide a way to run turns one at a time with player moves as input
    [ ] provide a set of standard 'turn events' sufficient to encode all the information
        the UI needs to display the sequence of events in a turn
        [ ] determine what information the UI needs to display all possible events
        [ ] encode a standard
    [ ] define a standard list of 'effects' and 'conditions' to use as reference when 
        implementing the effect/condition handlers
        