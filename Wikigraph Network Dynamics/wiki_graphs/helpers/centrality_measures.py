import networkx as nx
import pandas as pd


def centrality_measures(graph: nx.Graph) -> pd.DataFrame:
    # remove isolated nodes
    graph.remove_nodes_from(list(nx.isolates(graph)))

    degree_centrality = nx.degree_centrality(graph)
    print('done with degree_centrality')
    betweenness_centrality = nx.betweenness_centrality(graph)
    print('done with betweenness_centrality')
    eigenvector_centrality = nx.eigenvector_centrality(graph, max_iter=500)
    print('done with eigenvector_centrality')
    closeness_centrality = nx.closeness_centrality(graph)
    print('done with closeness_centrality')
    pagerank = nx.pagerank(graph)
    print('done with pagerank')

    centrality_df = pd.DataFrame(
        {
            "Degree Centrality": degree_centrality,
            "Betweenness Centrality": betweenness_centrality,
            "Closeness Centrality": closeness_centrality,
            "Eigenvector Centrality": eigenvector_centrality,
            "PageRank": pagerank,
        }
    )

    return centrality_df
