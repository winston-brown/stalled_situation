# Rules
#
# Maximum distance to nearest occupied stall
# If all stalls are empty, defer to the left (0)
# Tie-Breaker: defer to the left
#
# Using an Argmax solution

def choose_stall(stall_status: str) -> int | None:
    """
    Given a stall layout string (e.g. 'X__X_X_XX_'),
    where 'X' = occupied, '_' = empty, return the index
    of the stall a man should choose, following these rules:
      - Maximize distance to nearest occupied stall.
      - Break ties by choosing the leftmost stall.
      - If all stalls empty, choose index 0.
      - If no empty stalls, return None.
    """
    
    if len(stall_status) == 0:
        return None

    # Collect indices of occupied stalls
    occupied_indices = [i for i, c in enumerate(stall_status) if c.lower() == "x"]

    # no occupied stalls: pick the leftmost empty if any
    if not occupied_indices:
        for i, c in enumerate(stall_status):
            if c == "_":
                return i
        return None

    best_index = None
    best_distance = -1

    for i, c in enumerate(stall_status):
        if c != "_":
            continue

        # Distance to nearest occupied stall
        nearest_dist = min(abs(i - occ) for occ in occupied_indices)

        # Choose the stall with the max nearest distance
        # tie goes to leftmost
        if nearest_dist > best_distance:
            best_distance = nearest_dist
            best_index = i

    return best_index
