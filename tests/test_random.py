import sys

import networkx as nx
import pytest

from pycid.random.random_cid import random_cid, random_cids
from pycid.random.random_dag import random_dag


@pytest.mark.parametrize("n_all,n_decisions,n_utilities", [(4, 1, 1), (8, 2, 2), (12, 3, 3)])
def test_random_cid_create(n_all: int, n_decisions: int, n_utilities: int) -> None:
    random_cid(n_all, n_decisions, n_utilities).check_model()


def test_random_cids_create_one() -> None:
    for cid in random_cids(n_cids=1):
        cid.check_model()


def test_random_dag_create_one() -> None:
    dag = random_dag(number_of_nodes=5, edge_density=0.4, max_in_degree=4)
    assert nx.is_directed_acyclic_graph(dag)


if __name__ == "__main__":
    pytest.main(sys.argv)
