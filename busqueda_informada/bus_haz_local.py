import math

def beam_search(start, transition_fn, score_fn, beam_width, max_len):
    # `start`: the initial state
    # `transition_fn`: a function that takes a state and returns a list of (action, next_state) pairs
    # `score_fn`: a function that takes an action and returns a score
    # `beam_width`: the number of candidates to keep at each step
    # `max_len`: the maximum length of the output sequence
    
    # Initialize the beam with the start state
    beam = [(start, [], 0)]
    
    # Iterate until we reach the maximum length or run out of candidates
    for i in range(max_len):
        candidates = []
        
        # Generate new candidates by expanding each current candidate
        for state, seq, score in beam:
            for action, next_state in transition_fn(state):
                new_seq = seq + [action]
                new_score = score + score_fn(action)
                candidates.append((next_state, new_seq, new_score))
                
        # Select the top `beam_width` candidates based on their scores
        beam = sorted(candidates, key=lambda x: x[2], reverse=True)[:beam_width]
        
    # Return the sequence with the highest score
    return max(beam, key=lambda x: x[2])[1]
    # Define the set of possible choices at each step
choices = ['a', 'b', 'c']

# Define the transition function
def transition_fn(state):
    return [(c, state+c) for c in choices]

# Define the score function
def score_fn(action):
    return -math.log(0.5) if action == 'a' else -math.log(0.25)
# Define the start state
start = ''
# Run beam search
seq = beam_search(start, transition_fn, score_fn, beam_width=2, max_len=4)
# Print the resulting sequence
print(seq)