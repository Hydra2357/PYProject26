# from collections import deque
# from typing import Any, Optional, List, Set, Callable
#
# # -------------------------------------------------------------------------
# # Node class (used by both tree-search and graph-search)
# # -------------------------------------------------------------------------
# class Node:
#     def __init__(self, state: Any, parent: Optional['Node'] = None,
#                  action: Any = None, path_cost: float = 0.0):
#         self.state = state
#         self.parent = parent
#         self.action = action          # action that led to this node from parent
#         self.path_cost = path_cost    # g(n) - cost from start to this node
#
#     def __repr__(self):
#         return f"<Node state={self.state}, path_cost={self.path_cost}>"
#
#     # Reconstruct path from start to this node
#     def path(self) -> List['Node']:
#         node, path = self, []
#         while node is not None:
#             path.append(node)
#             node = node.parent
#         return path[::-1]  # reverse to get start → goal
#
#     def solution(self) -> List[Any]:
#         """Returns sequence of actions from start to this node"""
#         return [node.action for node in self.path()[1:]]
#
#
# # -------------------------------------------------------------------------
# # Problem abstract class (you need to implement this for your domain)
# # -------------------------------------------------------------------------
# class Problem:
#     def __init__(self, initial_state: Any, goal_test: Callable[[Any], bool]):
#         self.initial_state = initial_state
#         self.goal_test = goal_test
#
#     def actions(self, state: Any) -> List[Any]:
#         """Return list of possible actions from this state"""
#         raise NotImplementedError
#
#     def result(self, state: Any, action: Any) -> Any:
#         """Return the state that results from doing action in state"""
#         raise NotImplementedError
#
#     def step_cost(self, state: Any, action: Any, next_state: Any) -> float:
#         """Cost of taking action in state to reach next_state (default=1)"""
#         return 1.0
#
#
# # -------------------------------------------------------------------------
# # TREE-SEARCH  (allows revisiting states → can loop forever in cycles)
# # -------------------------------------------------------------------------
# def tree_search(problem: Problem, frontier_type=deque) -> Optional[Node]:
#     """
#     TREE-SEARCH version (no explored set → can have cycles/loops)
#     Uses FIFO queue by default (BFS), but you can pass stack (list) for DFS
#     """
#     # Initialize frontier with initial state
#     initial_node = Node(state=problem.initial_state, path_cost=0.0)
#     frontier = frontier_type([initial_node])
#
#     while frontier:
#         # Remove leaf node
#         node = frontier.popleft() if isinstance(frontier, deque) else frontier.pop()
#
#         # Goal test
#         if problem.goal_test(node.state):
#             return node
#
#         # Expand
#         for action in problem.actions(node.state):
#             next_state = problem.result(node.state, action)
#             path_cost = node.path_cost + problem.step_cost(node.state, action, next_state)
#             child = Node(
#                 state=next_state,
#                 parent=node,
#                 action=action,
#                 path_cost=path_cost
#             )
#             frontier.append(child)
#
#     return None  # failure
#
#
# # -------------------------------------------------------------------------
# # GRAPH-SEARCH  (avoids revisiting states using explored set)
# # -------------------------------------------------------------------------
# def graph_search(problem: Problem, frontier_type=deque) -> Optional[Node]:
#     """
#     GRAPH-SEARCH version (uses explored set to avoid cycles)
#     Default: BFS (using deque)
#     """
#     initial_node = Node(state=problem.initial_state, path_cost=0.0)
#
#     frontier = frontier_type([initial_node])
#     explored: Set[Any] = set()          # stores states, not nodes
#
#     while frontier:
#         node = frontier.popleft() if isinstance(frontier, deque) else frontier.pop()
#
#         if problem.goal_test(node.state):
#             return node
#
#         explored.add(node.state)
#
#         for action in problem.actions(node.state):
#             next_state = problem.result(node.state, action)
#
#             # Only add if not visited before (neither in frontier nor explored)
#             if next_state not in explored and not any(n.state == next_state for n in frontier):
#                 path_cost = node.path_cost + problem.step_cost(node.state, action, next_state)
#                 child = Node(
#                     state=next_state,
#                     parent=node,
#                     action=action,
#                     path_cost=path_cost
#                 )
#                 frontier.append(child)
#
#     return None  # failure
#
#
# # -------------------------------------------------------------------------
# # Quick example usage (8-puzzle style)
# # -------------------------------------------------------------------------
# if __name__ == "__main__":
#     # Just a dummy problem to show structure
#     class DummyProblem(Problem):
#         def actions(self, state):
#             return ["left", "right", "up", "down"] if state < 10 else []
#
#         def result(self, state, action):
#             if action == "right": return state + 1
#             if action == "left":  return state - 1
#             return state
#
#     def goal_test(state):
#         return state == 9
#
#     problem = DummyProblem(initial_state=0, goal_test=goal_test)
#
#     print("Running TREE-SEARCH (BFS style)...")
#     result = tree_search(problem)
#     if result:
#         print("Solution path:", result.solution())
#         print("Final state:", result.state)
#     else:
#         print("No solution found")
#
#     print("\nRunning GRAPH-SEARCH (BFS style)...")
#     result = graph_search(problem)
#     if result:
#         print("Solution path:", result.solution())
#         print("Final state:", result.state)