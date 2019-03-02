# Copyright (C) 2018
# This notice is to be included in all relevant source files.
# "Brandon Goldbeck" <bpg@pdx.edu>
# “Anthony Namba” <anamba@pdx.edu>
# “Brandon Le” <lebran@pdx.edu>
# “Ann Peake” <peakean@pdx.edu>
# “Sohan Tamang” <sohan@pdx.edu>
# “An Huynh” <an35@pdx.edu>
# “Theron Anderson” <atheron@pdx.edu>
# This software is licensed under the MIT License.
# See LICENSE file for the full text.
from src.model_conversion.edge import Edge


class Triangle:
    """A triangle is a set of 3 edges.
    """
    def __init__(self, e1, e2, e3):
        """Build a triangle from three edges.

        :param e1: The first edge.
        :param e2: The second edge.
        :param e3: The third edge.
        """
        self.triangles = [e1, e2, e3]

    def is_closed_loop(self):
        """Determine if a triangle has all its edges connected.

        :return: True, if all it's edges are connected.
        """
        start_edge = self.triangles[0]

        first_check = Edge.has_shared_vertex(start_edge, self.triangles[1])
        second_check = Edge.has_shared_vertex(start_edge, self.triangles[2])
        third_check = Edge.has_shared_vertex(self.triangles[1], self.triangles[2])

        return first_check and second_check and third_check

    @staticmethod
    def are_neighbors(t1, t2):
        """Determine if two triangles have a shared edge.

        :param t1: The first triangle.
        :param t2: The second triangle.
        :return: True, if the triangles had a shared edge.
        """
        result = False
        # x being an edge in the first triangle.
        for x in t1:
            # y being an edge in the second triangle.
            for y in t2:
                if Edge.same_edge(x, y):
                    # We just need one shared edge to be true.
                    result = True
        return result






