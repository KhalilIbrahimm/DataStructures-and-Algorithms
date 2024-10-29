
def stable_matching(pair1: dict, pair2: dict) -> list:
    """
    Solves the Stable Matching Problem using the Gale-Shapley algorithm.
    
    This is a Greedy Algorithm designed to find a stable match between two sets (in this case, men and women),
    where each person ranks members of the opposite set based on preference.
    
    Parameters:
    - pair1 (dict): Dictionary representing men's preference rankings of women.
    - pair2 (dict): Dictionary representing women's preference rankings of men.
    
    Returns:
    - list: A list of stable pairs (man, woman) where no two people would prefer to be with each other 
            over their current partners.
    """
    
    # List to keep track of the stable pairs (men, women)
    pair_under_behandling = []
    
    # A list of men who are not yet paired (i.e., still free)
    s_a_lenge_det_er_menn = [menn for menn in pair1.keys()]

    # Continue the algorithm while there are still free men
    while s_a_lenge_det_er_menn:
        for mann in s_a_lenge_det_er_menn:

            # Check the man's preferred women in order of preference
            for woman in pair1[mann]:
                
                # Check if the woman is already paired
                check_if_woman_taken = [pair for pair in pair_under_behandling if woman in pair]
                
                # If the woman is not paired, form a pair
                if len(check_if_woman_taken) == 0:
                    pair_under_behandling.append((mann, woman))
                    s_a_lenge_det_er_menn.remove(mann)
                    print(f'Congratulations {mann}, {woman} is single, and now you are a pair.')
                    break

                # If the woman is already paired
                elif len(check_if_woman_taken) > 0:
                    # Identify the current man the woman is paired with
                    current_man_index = pair2[woman].index(check_if_woman_taken[0][0])
                    
                    # Find where the current man and the new man rank in the woman's preference list
                    potential_man_index = pair2[woman].index(mann)
                    print(f'{woman} is already paired, {mann} remains single for now.')

                    # If the woman prefers her current partner, she doesn't switch
                    if current_man_index < potential_man_index:
                        print(f'{woman} does not want to switch {pair2[woman][current_man_index]} with {pair2[woman][potential_man_index]}.')
                    
                    # If the woman prefers the new man, she switches partners
                    else:
                        print(f'{woman} wants to switch {pair2[woman][potential_man_index]} with {pair2[woman][current_man_index]}.')
                        
                        # The current partner becomes free again
                        s_a_lenge_det_er_menn.remove(mann)  # The new man is no longer free
                        s_a_lenge_det_er_menn.append(check_if_woman_taken[0][0])  # The old partner becomes free

                        # Update the pair list with the new partner
                        check_if_woman_taken[0][0] = mann
                        print(f'{woman} is now paired with {pair2[woman][potential_man_index]}. Congratulations, {mann} and {woman} are now a pair.')
                        break

    return pair_under_behandling


# Define the preference rankings for men and women
preferred_rankings_men = {
    'ryan':    ['lizzy', 'sarah', 'zoey', 'daniella'],
    'josh':    ['sarah', 'lizzy', 'daniella', 'zoey'],
    'blake':   ['sarah', 'daniella', 'zoey', 'lizzy'],
    'connor':  ['lizzy', 'sarah', 'zoey', 'daniella']
}

preferred_rankings_women = {
    'lizzy':    ['ryan', 'blake', 'josh', 'connor'],
    'sarah':    ['ryan', 'blake', 'connor', 'josh'],
    'zoey':     ['connor', 'josh', 'ryan', 'blake'],
    'daniella': ['ryan', 'josh', 'connor', 'blake']
}

# Example usage
if __name__ == "__main__":
    # Print the resulting stable pairs
    print(stable_matching(preferred_rankings_men, preferred_rankings_women))
