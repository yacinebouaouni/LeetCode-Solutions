# LeetCode-Solutions

## Sliding Window
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Description          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/description/) |[Code](./Sliding-Window/max_average_subarray_1.py) | O(N) | O(1) | Easy | [Approach](https://leetcode.com/problems/maximum-average-subarray-i/solutions/3913554/sliding-window-python-easy/) | Fixed Window, Array
1004 | [Max Consicutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/description/) | [Code](./Sliding-Window/max_consecutive_ones_3.py) | O(N) | O(1) | Medium | [Approach](https://leetcode.com/problems/max-consecutive-ones-iii/solutions/3914086/sliding-window-optimal-linear-python/) | Sliding Window, Array
## Hashmap
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Description          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
1679 | [Max Number of K-Sum Pair](https://leetcode.com/problems/max-number-of-k-sum-pairs/description/) | [Code](./Hashmap/max_number_k_sum_pairs.py) | O(N) | O(N) | Medium | [Approach](https://leetcode.com/problems/max-number-of-k-sum-pairs/solutions/3909166/hashmap-on-beats-98-python/) |Hashmap, Array

## Two Pointers
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Description          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
283 | [Move Zeros](https://leetcode.com/problems/move-zeroes/description/) | [Code](./Two-Pointers/move_zeroes.py) | O(n) | O(1) | Easy | [Approach](https://leetcode.com/problems/move-zeroes/solutions/3908894/two-pointers-optimal-python/) | Two Pointers, Array
392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | [Code](./Two-Pointers/is_subsequence.py) | O(n) | O(1) | Easy | [Approach](https://leetcode.com/problems/is-subsequence/solutions/3908976/two-pointers-optimal-python/) | Two Pointers, Array
1679 | [Max Number of K-Sum Pair](https://leetcode.com/problems/max-number-of-k-sum-pairs/description/) | [Code](./Two-Pointers/max_number_k_sum_pairs.py) | O(N log N) | O(1) | Medium | [Approach](https://leetcode.com/problems/max-number-of-k-sum-pairs/solutions/3909073/two-pointers-o-n-log-n-python/) |Two Pointers, Array

## Binary Search
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Description          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
374 | [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/description/) |[Code](./Binary-Search/guess_number.py) | O(log n) | O(1) | Easy | [Approach](https://leetcode.com/problems/guess-number-higher-or-lower/solutions/3904135/binary-search-beats-97-easy-python/) |Binary Search, Array
162 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/description/)| [Code](./Binary-Search/find_peak_element.py)| O(log n) | O(1) | Medium | [Approach](https://leetcode.com/problems/find-peak-element/solutions/3904317/binary-search-beats-94-o-log-n-python/) |Binary Search, Array
875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/) | [Code](./Binary-Search/koko_eating_bananas.py) | O(N log M) | O(1) | Medium | [Approach](https://leetcode.com/problems/koko-eating-bananas/solutions/3904582/binary-search-beats-90-easy/) | Binary Search, Array
2300 | [Successful Pairs of Spells](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/) | [Code](./Binary-Search/successful_pairs.py) | O((M+N) log M) | O(N) | Medium | [Approach](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/solutions/3904876/binary-search-python-intuitive/) |Binary Search, Array
## Breadth-first search
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Description          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/) | [Code](./BFS/rotting_oranges.py) | O(N*M) | O(N*M) | Medium | [Description]( https://leetcode.com/problems/rotting-oranges/solutions/3890537/bfs-iterative-beats-99-8-python/)| BFS, Matrix
695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/description/) | [Code](./BFS/max_area_of_island.py) | O(N*M) | O(N*M) | Medium | [Decription](https://leetcode.com/problems/max-area-of-island/solutions/3890683/bfs-beats-99/) | BFS, Matrix
1926 | [Nearest Exit From Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/) | [Code](./BFS/nearest_exit_from_entrance.py) | O(N*M) | O(N*M) | Medium | [Approach](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/solutions/3890960/bfs-beats-99-python-explained/)| BFS, Matrix


## Depth-first search
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Description          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
841 | [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/description/)| [Code](./DFS/keys_and_rooms.py) | O(V+E) | O(V) | Medium |[Approach](https://leetcode.com/problems/keys-and-rooms/solutions/3894850/dfs-set-beats-98-python/) | DFS, Adjacency List
547 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)| [Code](./DFS/number_of_provinces.py) | O(N^2) | O(N) | Medium | [Approach](https://leetcode.com/problems/number-of-provinces/solutions/3895128/dfs-beats-99-python/) |DFS, Adjacency Matrix
1466 | [Reorder Routes](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75) | [Code](./DFS/reorder_routes.py) | O(N) | O(N) | Medium | [Approach](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/solutions/3899849/dfs-beats-98-recursive/) | DFS, Connection List
399 | [Evaluate Division](https://leetcode.com/problems/evaluate-division/description/) | [Code](./DFS/evaluate_division.py) | O(Q*(E+V)) | O(Q+E+V) | Medium | [Approach](https://leetcode.com/problems/evaluate-division/solutions/3900139/dfs-recursive-beats-97/) |DFS, Connection List




-------
# Ideas

## Sliding Window
* In a fixed length setting, try to update the quantity of interest (currentSum, Product ...) by adding and substracting. Don't compute the quantity from zero.
* In a fixed length setting, only one pointer is enough
* In a sliding window, try using one pointer that is incremented +1 in a for loop and the second incremented when a condition is reached (e.g., max consicutive ones problem). Then stop incrementation when the condition is satisfied again.

