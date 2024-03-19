import gzip
import networkx as nx


def create_node_to_article_mapping(file_path: str, delimiter=" ") -> dict:
    mapping = {}
    with gzip.open(file_path, "rt") as file:
        for line in file:
            parts = line.strip().split(delimiter)
            if len(parts) >= 2:
                node_number = parts[0]
                article_name = delimiter.join(parts[1:])
                mapping[node_number] = article_name
    return mapping


file_path = "wiki-topcats-page-names.txt.gz"

mapping_n2a = create_node_to_article_mapping(file_path)
mapping_a2n = {v: k for k, v in mapping_n2a.items()}


def id2name(node_number: str, mapping=mapping_n2a) -> str:
    return mapping.get(node_number)


def name2id(article_name: str, mapping=mapping_a2n) -> str:
    return mapping.get(article_name)


def out_conns(G: nx.Graph, node: str) -> list[str]:
    return [id2name(x) for x in G[node]]


def in_conns(G: nx.DiGraph, node: str) -> list[str]:
    # Ensure the node exists in the graph to avoid KeyError
    if node in G:
        # Use the predecessors method to get inbound connections
        return [id2name(x, mapping_n2a) for x in G.predecessors(node)]
    else:
        return []
