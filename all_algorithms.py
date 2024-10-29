

## Her skal vi implimentere alle algoritmer i faget
# A + INF234

from collections import Counter

# 1. Dijkstra algorithm

import math 
import heapq
'''
Vil heapen automatisk holde elementene i riktig rekkefølge slik at når vi henter elementer fra den med heapq.heappop(), får vi alltid den minste avstanden først. I dette tilfellet ville heapen først returnere (2,'B'), deretter (5,'C'), (8,'C'), osv.
'''

def dijkstra_own(graph, start_node):
    '''
    Dijkstra's algoritme finner faktisk den korteste veien fra startnoden til alle andre noder i grafen. DEN FINNER IKKE FRA EN SPESEFIK NODE TIL ANNEN.

    Input: Graf G = (V, E), start_node # V=Node, E=Kant
    Output: Korteste avstand fra start node til alle noder i V, en dictionary

    '''
    # Initialiserer avstandene (d') for alle noder som uendelig, bortsett fra startnoden
    avstand = {node: math.inf for node in graph}  # {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
    avstand[start_node]=0 # Avstanden fra A til A er 0. 

    # Initialiserer forrige node (predecessor) for å spore veien
    forrige_node = {node:None for node in graph}  #{'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}

    # En prioritetskø (heap) for å velge node med minst avstand
    kø = [(0, start_node)] # (avstand, node)

    visited_nodes = []

    while kø:
        nåværende_avstand, nåværende_node = heapq.heappop(kø) # Velg node med minst avstand

        if nåværende_node in visited_nodes:
            continue   # Hopp over hvis vi allerede har besøkt denne noden

        visited_nodes.append(nåværende_node)

        # Gå gjennom alle naboene til den nåværende noden
        for nabo, vekt in graph[nåværende_node].items():
            if nabo in visited_nodes:
                continue # Hopp over allerede besøkte naboer

            # Hvis nabo noden ikke er visited, beregn nye vekt\avstand 
            ny_avstand = nåværende_avstand + vekt 

            # Hvis vi finner en kortere vei til naboen, oppdater avstanden
            if ny_avstand < avstand[nabo]:
                avstand[nabo] = ny_avstand
                forrige_node[nabo] = nåværende_node # Vi oppdaterer også forrige_node[nabo] = nåværende_node for å kunne spore hvilken node vi kom fra. Dette er nødvendig for å rekonstruere den korteste veien senere.
                heapq.heappush(kø, (ny_avstand, nabo))

    return avstand, forrige_node, visited_nodes


# Eksempel på bruk
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

start_node = 'A'
distances, predecessors, visited_nodes= dijkstra_own(graph, start_node)

# print(distances, predecessors)
# print(visited_nodes)




# -------------------------------------------------------------------------------------------

## Interval Scheduling Problem Algorithm Implimentation

def interval_scheduling(intervals: list) -> list:
    '''
    input: set of tupel intervals {(s_1,t_1),(s_2,t_2)} - en aktivitet som starter på tid s og slutter på tid t
    output: en set med aktivitets tupler vi kan gjennomføre utenom overlap mellom intervals 
    '''

    # Sorter listen basert på FINISH-tid først 
    sort_by_end_time = sorted(intervals, key=lambda tupel_interval: tupel_interval[1]) # (start, slutt) tuple_interval[1] - sorterer basert på slutt tid

    valid_intervals = []
    last_end_time = -1 # Aha, istedet for å bruke en O(n log n) på å sammenligne tid i tuplene gjennom lengen n i arrayen, kan vi bare oppdatere denne variabelen til å inneholde end time for hver iterasjon. 

    # Gå gjennom aktivitetene i sortert rekkefølge
    for activity_interval in sort_by_end_time:
        start_time, end_time = activity_interval  # unpack eller pakk ut verdiene i tupel, altså del opp tuppel-verdier (a,b) mellom start_time, end_time. start_time får a og end_time får b. 
        
        # Hvis aktiviteten starter etter at forrige aktivitet er ferdig, velg den
        if start_time >= last_end_time:
            valid_intervals.append(activity_interval)
            last_end_time = end_time # Oppdater slutttiden til den valgte aktiviteten


    return valid_intervals




scheduling_intervals_ = [ 
    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (8, 9),
    (5, 9),
    (6, 10),
    (2, 14),
    (12, 16)
]


scheduling_intervals = [ 
    (0, 3),
    (1, 3),
    (0, 5),
    (3, 6),
    (4, 7),
    (3, 9),
    (5, 10),
    (8, 10),
]


# print(interval_scheduling(scheduling_intervals))

# LETT OG RETT. Helt forsått!



# -------------------------------------------------------------------------------------------

## Gale Shapely Algorithm Implimentation for Stable Matching problem. 

def stable_matching(pair1:dict, pair2:dict) -> list:

    # Pair under behandling 
    pair_under_behandling = []
    # Her skal det brukes til while løkken, while det er menn som ikke har noen pair
    så_lenge_det_er_menn = [menn for menn in pair1.keys()]

    # Kjør så lenge det er menn som ikke har pair, eller så lenge det ikke er stable (se definisjonen på stable)
    ## At alle må ha uansett pair for å kalle systemet stable

    while så_lenge_det_er_menn:
        for mann in så_lenge_det_er_menn:

            # Sjekke om kvinnen mann har som sit valg, er single ller ikke
            for woman in pair1[mann]:
                check_if_woman_taken = [pair for pair in pair_under_behandling if woman in pair]
                
                # Hvis jenten er single 
                if len(check_if_woman_taken)==0:
                    pair_under_behandling.append((mann, woman))
                    så_lenge_det_er_menn.remove(mann)
                    print('Gratulerer %a, %a er single og dere er et par nå.' % (mann,woman))
                    break

                # Men hvis jenten mannen vil ikke er ledig
                elif len(check_if_woman_taken)>0:
                    pågående_mann = pair2[woman].index(check_if_woman_taken[0][0]) # [('blake', 'sarah')] , da betyr det at de eksisterer et tilfelle der mannen jente valg er ikke single og ser sånn ut. [0][0] gir derfor oss blake som vi skal sammenligne og se om jenten vil bytte eller ikke. 

                    potensiell_menn = pair2[woman].index(mann)
                    print('{} er allerede i et par, {} er derfor fortsatt single.'.format(woman,mann))

                    # Ojaa, skal sjekke om current menn er bedre en potensiell mann 
                    if pågående_mann < potensiell_menn:  # [blake, noe, noe], jo mindre index jo bedre valg har jenten 
                         print(f'{woman} vil ikke bytte {pair2[woman][pågående_mann]} med {pair2[woman][potensiell_menn]}..')

                    else: # [bedre valg, bedre valg, blake], bedre for jenten med bytting, da det finnes bedre valg, større index verdi. 
                        # Hvis hun vil bytte til et bedre mann
                        så_lenge_det_er_menn.remove(mann) # Fjerne pågående mann fra stable_matching listen, da jenten valgte en annen enn han, og han ble single igjen og må finne seg annen. 
                        så_lenge_det_er_menn.append(check_if_woman_taken[0][0]) # Legg den bedre potensiell mann som et nytt par med jenten.i stable matching listen.  

                        check_if_woman_taken[0][0] = mann
                        print(f'{woman} vil bytte {pair2[woman][potensiell_menn]} med {pair2[woman][pågående_mann]}. Gratulerer, {woman} og {pair2[woman][potensiell_menn]} er par nå.')
                        break

    return pair_under_behandling 




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

# print(stable_matching(preferred_rankings_men, preferred_rankings_women))



# -------------------------------------------------------------------------------------------

## Check after Directed Acyclic Graph (DAG) algorithm implimentation - Kahn's Algorithm  
### For å finne topological list --> så må grafen være DAG --> som vil si at den ikke ha noen sykluser i seg.
### A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph (DAG).

from collections import deque

def find_cycel_or_topological_list(graph:list, antall_noder:int) -> list:
    topological_orderd_list = []
    in_degree = {node:0 for node in range(antall_noder)}

    graph_tuple = {}
    for node in graph:
        in_degree[node[1]] += 1
        if node[0] not in graph_tuple:graph_tuple[node[0]] = [node[1]]
        else:graph_tuple[node[0]].append(node[1])

    # queue = [key for key in in_degree if in_degree.get(key) == 0] 
    queue = deque([node for node in in_degree if in_degree.get(node) == 0])

    print('Start graph Degree: ',in_degree)
    while queue:
        node = queue.popleft()
    
        if node in graph_tuple:
            print('node:', node)
            for nabo in graph_tuple[node]:
                in_degree[nabo] -= 1   
                if in_degree[nabo] == 0:
                    queue.append(nabo)

        topological_orderd_list.append(node)
        in_degree.pop(node)
        print('topological_orderd_list', topological_orderd_list)
        print('in_degree:', in_degree)


    if len(topological_orderd_list) == antall_noder:
        return f'Topological list = {topological_orderd_list}'  # Topologisk sortering
    else:
        return 'Cycle detected, this graph are not DAG and has not topological list.'   # Det er en sykel



# Antall noder
n = 6

# Kantene i grafen som par (from_node, to_node)
edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

# print(find_cycel_or_topological_list(edges, n))






# -------------------------------------------------------------------------------------------

## Prim's Algorithm for Minimum Spanning Tree 

### Konseptet er å begynne fra en node også expande det med greedy algoritme til å velge det minste kanten og velge alt som ikke vil skape en cycle. 

def prims_algorithm(graph):

   # Start fra en vilkårlig node
    start_node = next(iter(graph))
    visited_nodes = set([start_node])

    # Opprett en kø med alle kantene fra startnoden
    # queue = deque([(start_node, neighbor, edge_cost) for neighbor, edge_cost in graph[start_node].items()])
    queue = None

    mst = []  # Minimum Spanning Tree
    total_mst_cost = 0  # Total kostnad for MST

    while queue:
        # Fjern kanten med lavest kostnad
        s_node, e_node, edge_cost = queue.popleft()
        
        # Hvis destinasjonsnoden ikke er besøke
        if e_node not in visited_nodes:
            visited_nodes.add(e_node)  # Marker noden som besøkt            
            mst.append((s_node, e_node, edge_cost))  # Legg til kanten til MST
            total_mst_cost += edge_cost  # Legg til kostnaden til totalen

            # Legg til alle kanter fra den nye noden som ikke leder til besøkte noder
            for neighbor, cost in graph[e_node].items():
                if neighbor not in visited_nodes:
                    queue.append((e_node, neighbor, cost))
    
    return mst, total_mst_cost
    

def prims_algorithm_v2(graph, start_node):

    # Her skal vi legge til alle node vi har besøkt
    visited = set([start_node])

    # Her lager vi en deque som alltid vil velge sortere fra minst til størst. Merk at vi starter med å legge til start_node i deque.
    queue = deque([(start_node, neighbor, edge_cost) for neighbor, edge_cost in graph[start_node].items()])
    mst=[]
    totalt_cost = 0

    while queue:
        s_node, neighbor, edge_cost = queue.popleft()

        if neighbor not in visited:
            visited.add(neighbor)
            mst.append((s_node, neighbor, edge_cost))
            totalt_cost += edge_cost

            for next_neighbor, cost in graph[neighbor].items():
                if next_neighbor not in visited:
                    queue.append((neighbor, next_neighbor, cost))
    return mst, totalt_cost

# Egentlig ganske lett og intuitivt. 

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
#
# mst, mst_cost = prims_algorithm(graph, 'A')
# print('MST: {} | MST-cost: {}'.format(mst, mst_cost))



# -------------------------------------------------------------------------------------------

## Kruskal Algorithm for Minimum Spanning Tree 


def kruskal_algorithm_(graph):

    # Først sorter alle kantene basert på minst til størst 
    sorted_graph = deque(sorted(graph, key= lambda edge: edge[2]))
    
    # Et liste til å inneholde alle kanter som ikke skaper en syklus 
    visited_nodes = []
    MST:list = []

    while sorted_graph:
        node1, node2, edge = sorted_graph.popleft()
        if node2 not in visited_nodes:
            MST.append((node1, node2, edge))
            visited_nodes.append(node1)
            visited_nodes.append(node2)
           

    return MST

# Dette er aller riktigst algoritme. 
def kruskal_algorithm(graph, num_nodes):
    # Sorter kantene basert på vekt
    graph.sort(key=lambda edge: edge[2])
    
    parent = list(range(num_nodes))
    
    def find(u):
        if parent[u] != u: # Sjekker om u er sin egen forelder. Hvis ikke, finner den roten til u rekursivt
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_v] = root_u
    
    MST = []

    # Sjekker etter syklus 
    for u, v, weight in graph:
        if find(u) != find(v):
            MST.append((u, v, weight))
            union(u, v)
    
    return MST



edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]


# Eksempel på graf representert som en liste av kanter
graph_ = [
    (0, 1, 2),  # Kant fra node 0 til node 1 med vekt 2
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (2, 3, 5)
]
#
# print("Kantene i Minimum Spanning Tree er:")
# print(kruskal_algorithm(edges, len(edges)))




# -------------------------------------------------------------------------------------------

## Huffman's Algorithm - Huffman code 

### AABCBCABDAKH --> Konvertere til en binary representasjon med minst mulig antall bits. Se video for full mening. 

import heapq

class Node:
    def __init__(self, bokstav, frequency) -> None:
        self.bokstav = bokstav
        self.frequency = frequency
        self.left = None 
        self.right = None 
    
    def __lt__ (self, other):
        return self.frequency < other.frequency
        



def huffmans_code(string_input:str) -> dict:


    # 1. Finne bokstav frequency (hvor mange ganger et bokstav er nevnt). 
    frequency = Counter(string_input)


    # 2. Lag en heap (prioritetskø) med noder for hvert tegn. Merk at heapq er organisert slik at foreldreelementet alltid er mindre enn sine barn.
    heap = [Node(char,freq) for char,freq in frequency.items()]    
    heapq.heapify(heap)

    # 3. Bygg Huffman-treet
    while len(heap) > 1:
        node1 = heapq.heappop(heap) 
        node2 = heapq.heappop(heap) 
        # print('Node 1: {} | Node 2: {}'.format(node1, node2))
        
        # Opprett en ny foreledre node med de to minste nodene som barn, og legge foreldre nodens verdi som summer av 2 to barna verdi. 
        merged = Node(None, node1.frequency + node2.frequency)
        merged.left = node1
        merged.right = node2

        # Legg den nye noden tilbake i heapen
        heapq.heappush(heap, merged)


    # Huffman-treet er nå bygget, og roten er den eneste noden i heapen
    huffman_tree_root = heap[0]

    # 4. Generer Huffman-koder fra treet
    huffmans_result = {}

    def generate_code(node, current_node):
        if node is None: return
        
        # Hvis vi har nådd et bladnode
        if node.bokstav is not None: 
            huffmans_result[node.bokstav] = current_node
            return 

        # Gå til venstre barn med "0" og høyre barn med "1"
        generate_code(node.left, current_node + '0')
        generate_code(node.right, current_node + '1')

    generate_code(huffman_tree_root, '')


    return huffmans_result



    
# test_input = 'Hei, dette er en test versjon av Huffmans algoritme.'
#
# test_input = 'Khalil'
# huffman_encoder = huffmans_code(test_input)
# print(''.join(huffman_encoder.keys()), ''.join(huffman_encoder.values()))
#








# -------------------------------------------------------------------------------------------

## Merge Sort Algorithm - Divide & Conquer 




# -------------------------------------------------------------------------------------------

## Karatsuba Algorithm 



# -------------------------------------------------------------------------------------------

## Dynamic Programming - Robot Path 

def robot_path(i,j):
    if i <= 1 or j <= 1:
        return 1 
    return robot_path(i-1,j) + robot_path(i, j-1)


# -------------------------------------------------------------------------------------------

## Interval Scheduling Problem - Solved with Dynamic Programming 

## First, vi må lage en array av schedulings elementer som ikke er overlappende med hverandre, og liste dem sammen på hvem som er etter hvem 

def find_previous_intervals(intervals:list[tuple[int, int]], weights:list[int]) -> list[int]:
    pass



weights = [8, 7, 12, 15, 11, 18, 16, 4, 12, 17]
intervals = [(0, 3), (2, 5), (4, 6), (6, 9), (5, 8), (8, 11), (9, 12), (11, 13), (10, 14), (12, 15)]

print(find_previous_intervals(intervals, weights))




# -------------------------------------------------------------------------------------------

## Coins problem - Oblig 1 - Greedy Algorithm
### The code should returns coins that sum up to a certain value, with the requirement that you return as few coins as possible.

def change(coins:dict, value:int) -> dict:
    results = {} # Lagre resultatene (hvilke mynter som brukes)
    current_sum = 0

    # Plukke det st√∏rste coint
    for coin in sorted(coins.keys(), reverse=True):
        now_coin_available = coins[coin]

        while now_coin_available > 0 and coin + current_sum <= value:
            if coin not in results:
                results[coin] = 0 # Hvis mynten ikke finnes i results, start med 0 mynter for denne myntverdien

            # Hvis coin er i result 
            results[coin] += 1 # Adder og legg til en mynt
            current_sum += coin # Oppdater cuurent_sum til √• ikke overstride value verdien
            now_coin_available -= 1 # Reduser antall tilgjengelige mynter

        if current_sum == value:
            break

    return results


coins = {1: 3, 5: 0, 10: 3, 20: 1}
value = 42

# output:  {20: 1, 10: 2, 1: 2}

print(change(coins, value))


# -------------------------------------------------------------------------------------------

## Segmentet Least Squares - Dynamic Programming 



# -------------------------------------------------------------------------------------------

## Levenshtein-avstand (SpellChecking problem) - Dynamic Programming 




