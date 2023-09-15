class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if endGene not in bank:
            return -1
    
        def create_graph(bank):
            graph = defaultdict(list)
            for i in range(len(bank)):
                for j in range(i+1, len(bank)):
                    if is_mutation(bank[i], bank[j]):
                        graph[bank[i]].append(bank[j])
                        graph[bank[j]].append(bank[i])
            return graph

        def is_mutation(gene1, gene2):
            numberMutations = sum([gene1[i]!=gene2[i] for i in range(8)])
            return (numberMutations == 1)

        bank.append(startGene)
        graph = create_graph(bank)
        visited, queue = set(), deque([(startGene,0)]) 
        visited.add(startGene)

        while queue:
            node, lvl = queue.popleft()
            if node == endGene:
                return lvl
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, lvl+1))
                    visited.add(neighbor)
        
        return -1