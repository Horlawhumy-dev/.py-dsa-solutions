
#works for increasing inputs
def locate_target(inputs: list, target: int) -> int:
    low, high = 0, len(inputs)-1
    
    while low <= high:
        mid = (low + high) // 2

        #print("lo:", low, ", hi:", high, ", mid:", mid, ", mid_number:", inputs[mid])

        if inputs[mid] == target:
            return mid
        elif inputs[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1
    return -1


# this works for decreasing cards
def find_position(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        potion = find_position(cards, query, mid)
        if potion == 'found':
            return mid
        elif potion == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1