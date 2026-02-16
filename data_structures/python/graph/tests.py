import unittest

from simple_graph import SimpleGraph, Vertex


class TestSimpleGraph(unittest.TestCase):

    def setUp(cls) -> None:
        cls.graph = SimpleGraph(3)
        cls.graph.AddVertex(1)
        cls.graph.AddVertex(2)
        cls.graph.AddEdge(0, 1)

    def test_add_vertex(self):
        self.graph.AddVertex(3)
        self.assertIsInstance(self.graph.vertex[2], Vertex)
        self.assertEqual(self.graph.vertex[2].Value, 3)
        self.assertNotIn(None, self.graph.vertex)
        self.assertFalse(self.graph.IsEdge(0, 2))
        self.assertFalse(self.graph.IsEdge(1, 2))
        vertex_list = self.graph.vertex
        self.graph.AddVertex(3)  # попытка добавить вершину в заполненный граф
        self.assertEqual(
            self.graph.vertex, vertex_list)  # список вершин не изменился

    def test_remove_vertex(self):
        self.assertTrue(self.graph.IsEdge(0, 1))
        self.graph.RemoveVertex(0)
        self.assertFalse(self.graph.IsEdge(1, 0))
        self.graph.RemoveVertex(1)
        self.assertFalse(self.graph.IsEdge(1, 0))
        for vertex in self.graph.vertex:
            self.assertIsNone(vertex)
        for i in range(self.graph.max_vertex):
            for j in range(self.graph.max_vertex):
                self.assertEqual(self.graph.m_adjacency[i][j], 0)

    def test_is_edge(self):
        self.assertTrue(self.graph.IsEdge(0, 1))
        self.assertTrue(self.graph.IsEdge(1, 0))
        self.assertFalse(self.graph.IsEdge(0, 2))
        self.assertFalse(self.graph.IsEdge(2, 0))
        self.assertFalse(self.graph.IsEdge(1, 2))
        self.assertFalse(self.graph.IsEdge(2, 1))

    def test_remove_edge(self):
        self.assertTrue(self.graph.IsEdge(0, 1))
        self.assertTrue(self.graph.IsEdge(1, 0))
        self.graph.RemoveEdge(0, 1)
        self.assertFalse(self.graph.IsEdge(0, 1))
        self.assertFalse(self.graph.IsEdge(1, 0))
        for i in range(self.graph.max_vertex):
            for j in range(self.graph.max_vertex):
                self.assertEqual(self.graph.m_adjacency[i][j], 0)

    def test_add_edge(self):
        self.graph.AddVertex(3)
        self.assertFalse(self.graph.IsEdge(0, 2))
        self.assertFalse(self.graph.IsEdge(2, 0))
        self.graph.AddEdge(0, 2)
        self.assertTrue(self.graph.IsEdge(0, 2))
        self.assertTrue(self.graph.IsEdge(2, 0))
        self.graph.AddEdge(1, 2)
        self.assertTrue(self.graph.IsEdge(1, 2))
        self.assertTrue(self.graph.IsEdge(2, 1))
        for i in range(self.graph.max_vertex):
            for j in range(self.graph.max_vertex):
                if i != j:
                    self.assertEqual(self.graph.m_adjacency[i][j], 1)
                else:
                    self.assertEqual(self.graph.m_adjacency[i][j], 0)

    def test_depth_first_search(self):
        self.graph.AddVertex(3)
        self.graph.AddEdge(1, 2)
        self.assertListEqual(
            self.graph.DepthFirstSearch(0, 2), self.graph.vertex
        )
        self.assertListEqual(
            self.graph.DepthFirstSearch(1, 2), self.graph.vertex[1:]
        )
        self.assertListEqual(
            self.graph.DepthFirstSearch(0, 1), self.graph.vertex[:2]
        )

    def test_breadth_first_search(self):
        self.graph.AddVertex(3)
        self.graph.AddEdge(1, 2)
        self.assertListEqual(
            self.graph.BreadthFirstSearch(0, 2), self.graph.vertex
        )
        self.assertListEqual(
            self.graph.BreadthFirstSearch(1, 2), self.graph.vertex[1:]
        )
        self.assertListEqual(
            self.graph.BreadthFirstSearch(0, 1), self.graph.vertex[:2]
        )

    def test_weak_vertices(self):
        self.graph.AddVertex(3)
        self.graph.AddEdge(0, 2)
        self.assertTrue(self.graph.WeakVertices())
        self.assertIsInstance(self.graph.WeakVertices(), list)
        self.assertIsInstance(self.graph.WeakVertices()[0], Vertex)
        self.assertEqual(
            len(self.graph.WeakVertices()), len(self.graph.vertex)
        )
        # добавляем связь до треугольника
        self.graph.AddEdge(1, 2)
        # уязвимых вершин не обнаружено
        self.assertFalse(self.graph.WeakVertices())


class TestDFSandBDF(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = SimpleGraph(11)
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        self.graph.AddVertex(6)
        self.graph.AddVertex(7)
        self.graph.AddVertex(8)
        self.graph.AddVertex(9)
        self.graph.AddVertex(10)
        self.graph.AddVertex(11)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(4, 5)
        self.graph.AddEdge(5, 6)
        self.graph.AddEdge(2, 6)
        self.graph.AddEdge(2, 7)
        self.graph.AddEdge(3, 8)
        self.graph.AddEdge(3, 9)
        self.graph.AddEdge(5, 9)
        self.graph.AddEdge(1, 3)

    def test_1(self):
        path_BFS = self.graph.BreadthFirstSearch(5, 7)
        self.assertIsInstance(path_BFS, list)
        self.assertEqual(len(path_BFS), 4)
        path_DFS = self.graph.DepthFirstSearch(5, 7)
        self.assertIsInstance(path_DFS, list)
        self.assertEqual(len(path_DFS), 5)
        # проверяем, что алгоритм BFS нашел более короткий путь
        self.assertGreater(len(path_DFS), len(path_BFS))

    def test_2(self):
        path_BFS = self.graph.BreadthFirstSearch(8, 6)
        path_DFS = self.graph.DepthFirstSearch(8, 6)
        self.assertIsInstance(path_BFS, list)
        self.assertEqual(len(path_BFS), 5)
        self.assertIsInstance(path_DFS, list)
        self.assertEqual(len(path_DFS), 6)
        # проверяем, что алгоритм BFS нашел более короткий путь
        self.assertGreater(len(path_DFS), len(path_BFS))


if __name__ == '__main__':
    unittest.main()
