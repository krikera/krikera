#!/usr/bin/env python3
"""
Test script to verify that the quote selection mechanism can access all quotes.
This script simulates multiple iterations of the update_quote.py script to check
if all quotes in the list can be selected.
"""

import random
from quotes_list import quotes
from collections import Counter

def test_quote_iteration():
    """Test if the random.choice() can select from all quotes in the list"""
    
    # Get unique quotes
    unique_quotes = set(quotes)
    total_quotes = len(quotes)
    unique_count = len(unique_quotes)
    
    print("=" * 80)
    print("Quote Iteration Test")
    print("=" * 80)
    print(f"Total quotes in list: {total_quotes}")
    print(f"Unique quotes: {unique_count}")
    print(f"Duplicate count: {total_quotes - unique_count}")
    print()
    
    # Simulate random selection many times
    num_iterations = 10000
    print(f"Running {num_iterations} iterations of random.choice()...")
    print()
    
    selected_quotes = []
    for _ in range(num_iterations):
        selected_quotes.append(random.choice(quotes))
    
    # Count how many times each unique quote was selected
    selection_counts = Counter(selected_quotes)
    unique_selected = len(selection_counts)
    
    print(f"Unique quotes selected: {unique_selected} out of {unique_count}")
    print()
    
    # Check if all unique quotes were selected at least once
    missing_quotes = unique_quotes - set(selection_counts.keys())
    
    if missing_quotes:
        print(f"❌ FAIL: {len(missing_quotes)} unique quotes were NEVER selected:")
        for i, quote in enumerate(sorted(missing_quotes), 1):
            print(f"  {i}. {quote}")
    else:
        print("✓ SUCCESS: All unique quotes were selected at least once!")
    
    print()
    print("-" * 80)
    print("Selection frequency analysis:")
    print("-" * 80)
    
    # Show top 10 most and least frequently selected quotes
    most_common = selection_counts.most_common(10)
    least_common = selection_counts.most_common()[-10:]
    
    print("\nTop 10 most frequently selected quotes:")
    for i, (quote, count) in enumerate(most_common, 1):
        occurrences_in_list = quotes.count(quote)
        print(f"  {i}. Selected {count} times (appears {occurrences_in_list}x in list)")
        print(f"     {quote[:70]}...")
    
    print("\nTop 10 least frequently selected quotes:")
    for i, (quote, count) in enumerate(least_common, 1):
        occurrences_in_list = quotes.count(quote)
        print(f"  {i}. Selected {count} times (appears {occurrences_in_list}x in list)")
        print(f"     {quote[:70]}...")
    
    print()
    print("=" * 80)
    print("Conclusion:")
    print("=" * 80)
    print("The update_quote.py script uses random.choice() which CAN select from")
    print("ALL quotes in the list. However, quotes that appear more frequently")
    print("in the list have a higher probability of being selected.")
    print()
    print(f"With {total_quotes} total quotes and {unique_count} unique quotes,")
    print("each quote's selection probability is proportional to how many times")
    print("it appears in the list.")
    print("=" * 80)

if __name__ == "__main__":
    test_quote_iteration()
