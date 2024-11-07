from collections import defaultdict, Counter
from typing import Dict

def merge_with_defaultdict(*dicts: Dict[str, int]) -> Dict[str, int]:
    """
    Merge multiple dictionaries of word frequencies using defaultdict.
    Returns a dictionary sorted by frequency in descending order.
    
    Args:
        *dicts: Variable number of dictionaries containing word frequencies
        
    Returns:
        Dict[str, int]: Merged dictionary sorted by frequency in descending order
    """
    if not dicts:
        return {}
    
    # Initialize defaultdict to store merged frequencies
    merged = defaultdict(int)
    
    # Sum frequencies across all dictionaries
    for d in dicts:
        for word, freq in d.items():
            merged[word] += freq
    
    # Convert defaultdict to regular dict and sort by frequency
    # For equal frequencies, sort alphabetically by word
    sorted_items = sorted(merged.items(), key=lambda x: (-x[1], x[0]))
    
    # Convert back to dictionary while maintaining sorted order
    return dict(sorted_items)

def merge_with_counter(*dicts: Dict[str, int]) -> Dict[str, int]:
    """
    Merge multiple dictionaries of word frequencies using Counter.
    Returns a dictionary sorted by frequency in descending order.
    
    Args:
        *dicts: Variable number of dictionaries containing word frequencies
        
    Returns:
        Dict[str, int]: Merged dictionary sorted by frequency in descending order
    """
    if not dicts:
        return {}
    
    # Sum all counters
    merged = Counter()
    for d in dicts:
        merged.update(d)
    
    # Sort by frequency and then alphabetically
    sorted_items = sorted(merged.items(), key=lambda x: (-x[1], x[0]))
    
    # Convert back to dictionary while maintaining sorted order
    return dict(sorted_items)
