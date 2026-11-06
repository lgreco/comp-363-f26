# Week 11 Assignment — Ford–Fulkerson: Maximum Flow and Minimum Cut

Due Friday, November 13. Deliverable is a single file, `ford_fulkerson.py`. Start from the starter file in this folder, [`ford_fulkerson.py`](./ford_fulkerson.py).

## Reading

- [maximum flows and minimum cuts](https://jeffe.cs.illinois.edu/teaching/algorithms/book/10-maxflow.pdf) (Erickson, Chapter 10). The augmenting-path search we use is about half a page of it. The chapter also opens with the Cold War rail network we talked about on 11/4.
- ["Maximal Flow Through a Network" (Ford and Fulkerson, 1956)](https://www.cs.yale.edu/homes/lans/readings/routing/ford-max_flow-1956.pdf) — the original paper by L. R. Ford, Jr. and D. R. Fulkerson. It is a scanned journal article, so expect dense 1950s notation; read the introduction and the statement of the main theorem, and compare its language with our "augmenting path" and "cut."
- [Python `copy` module, shallow versus deep](https://docs.python.org/3/library/copy.html) — what the 11/6 class did by hand, and what production code would use.

## The task

Implement the Ford–Fulkerson method exactly as we traced it on the whiteboard on 11/6. The graph is a directed acyclic graph stored as an **adjacency matrix**: `graph[u][v]` is the capacity of the edge from `u` to `v`, and `0` means there is no edge. Given a source and a target, your program finds the **maximum flow** and the **minimum cut**.

The method, in five lines:

1. Make a **deep copy** of the matrix: the residual graph. The original is the map; never touch it.
2. While the residual graph has a path from source to target (an **augmenting path**), find the weakest edge on the path and **saturate** the path by that amount: forward capacities go down, back edges go up. An edge whose capacity reaches 0 is gone.
3. Add up the flow you sent on each path.
4. When no augmenting path remains, find the set **S** of vertices still reachable from the source.
5. The edges of the **original** graph that go from a vertex in S to a vertex not in S are the minimum cut. Their capacities add up to the maximum flow.

### Part A — the algorithm

The starter file breaks the work into small functions, each with a docstring and a hint:

| Function | Job |
|---|---|
| `deep_copy(matrix)` | A copy that shares no memory with the original, written by hand with two nested loops |
| `find_augmenting_path(residual, current, target, path_so_far)` | Recursive; returns a list of vertices, or `None` |
| `bottleneck(residual, path)` | The weakest edge on a path |
| `saturate(residual, path, flow)` | Updates the residual graph in place |
| `reachable(residual, source)` | The set S |
| `cut_edges(graph, reachable_set)` | The edges crossing from S to everything else |
| `ford_fulkerson(graph, source, target)` | Puts it together; returns `(max_flow, cut)` |

Two details to get right:

- **Back edges create two-vertex loops.** Once you saturate an edge from `u` to `v`, the residual graph has `v` to `u` as well. A recursive path search that does not remember which vertices are already on the path can bounce between `u` and `v` forever. The given tests check this.
- **The input must come back unchanged.** Also given as a test.
- **Warning: the search can get very slow on large graphs.** A correct `find_augmenting_path` can still take minutes on a graph with over 100 vertices (the large test graph will show it). The cause is that a vertex can be reached by many different routes. If your search remembers only the vertices on its *current* path, then every time it reaches a dead end it forgets what it learned, and the next route tries the same dead ends again. The number of routes grows exponentially with the size of the graph, which small graphs hide. When your code is correct but your run will not finish, ask what your search forgets, and fix it.

The starter has two small graphs. `CLASS_GRAPH` is built like the one from 11/4 and 11/6: two edges leave the source with capacity 40 each, but the maximum flow is 20. `DIAMOND` is small enough to solve in your head. Two much larger acyclic graphs, `GRAPH_A` (120 vertices) and `GRAPH_B` (150 vertices), are in [`test_graphs.py`](./test_graphs.py). They come without answers: a correct maximum flow and cut must pass your own checks, such as the cut's capacities summing to the flow, and the flow being the same however you find your paths.

### Part B — is the graph really acyclic?

Everything above works because the input is acyclic, and the loop is guaranteed to end. But what if someone hands you a graph that only *claims* to be a DAG, by malice or by mistake?

1. Write `is_acyclic(graph)`, returning `True` or `False`. On 10/30 we saw Kahn's algorithm, which repeatedly removes a vertex with in-degree 0; if it gets stuck with vertices left over, there is a cycle. Any correct method is welcome.
2. `ford_fulkerson` must call it first and raise `ValueError` for a cyclic graph. A given test checks this.
3. Write `test_is_acyclic()` yourself, with asserts. The starter lists what your tests must cover: more than one acyclic graph, a reciprocal pair, a longer cycle such as `0 → 2 → 4 → 1 → 0`, and a cycle that does not pass through the source. For each, say in a comment what bug the test would catch.

## Questions to answer

In a comment block at the end of your file:

1. **Ezra's question.** On `CLASS_GRAPH` your program saturates more edges than end up in the cut. List the saturated edges and the cut edges. Explain why summing the bottlenecks of the augmenting paths still gives the right maximum flow, and show that the sum of the cut's capacities in the **original** matrix gives the same number.
2. **Shallow versus deep.** Replace your `deep_copy` temporarily with `residual = graph`. Which given tests fail, and why? Put it back.
3. **Is the cut unique?** Find a graph (it can be tiny) in which two different sets of edges form minimum cuts, or explain why you could not.
4. **How long?** Roughly how many times can your `while` loop run on a graph whose capacities are whole numbers and whose maximum flow is $F$? What does that say about huge capacities?

## How to work, and AI

I would encourage you to **hand-code this one.** I want to see imperfect, in-progress code. If I see perfect code on a problem like this one, I will know something is off. Show me what you need, not what you already have.

If you do use an AI agent or chatbot (web, command line, or inside your editor alike), submit your **prompts and its responses** along with your code, in a separate text file. What I want to see is how you directed it and how you checked what it gave you. Agents will do this problem in seconds, since every implementation is on GitHub; that is exactly why verifying the result by hand is the skill that counts. Make this your last hand-coded assignment of the course.

## Constraints

- Every function that returns a value has exactly one `return`.
- Do not use `copy`, `networkx`, or any other library for the algorithm itself.
- Keep the docstrings in the starter file. Do not change the given tests.
- Nothing runs automatically when your file is imported, except what is under `if __name__ == "__main__":`.

## Thanksgiving week: tell me what you prefer

We do not meet on Wednesday or Friday of Thanksgiving week. The Monday before, **November 23**, is up to you: in person, on Zoom, or asynchronous (no meeting). Please answer the one-question survey:

[Thanksgiving Monday survey: in person, Zoom, or asynchronous](https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=408fApwrJEiDeLvPnsWsy7I196tvCVFAgylhP23oZuNUMVFFT1BHNlAwRTROOVBFUUU1TTFLUENGVy4u)

If I hear nothing, we meet in person as usual.

## Turning it in

Upload `ford_fulkerson.py` to Sakai, containing your functions, the given tests, your `test_is_acyclic`, and your answers in a comment block at the end. If you used an AI tool, upload the prompts-and-responses file too. Run the file before you upload and aim for every given test to say `ok`.
