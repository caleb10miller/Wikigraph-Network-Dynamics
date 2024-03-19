# Wikigraph-Network-Dynamics
This study examines the Wiki-Topcats network, revealing Wikipedia's hyperlink structure and centrality. It identifies key information nodes and Western bias in knowledge representation, offering insights into global information distribution and connectivity biases within the Wikipedia network.

## Overview
This project delves into the Wiki-Topcats network, exploring the dynamics of Wikipedia's hyperlink structure to understand the architecture of human knowledge. Our analysis seeks to identify key patterns of information interconnectivity, centrality of topics, and the clustering of knowledge communities.

## Team Members
- Caleb Miller
- Luke Chesley

## Objectives
- Investigate centrality measures and structural makeup of the Wiki-Topcats network.
- Uncover patterns revealing interconnected information, pivotal topics, and knowledge clustering.
- Analyze global connectivity bias, focusing on Western dominance within Wikipedia's English version.

## Methodology
- **Data Collection**: Utilized the "Wikipedia Top Categories" dataset from the Stanford Large Network Dataset Collection.
- **Network Construction**: Employed Python's networkx library to model the Wikipedia hyperlink graph.
- **Centrality Analysis**: Computed various centrality metrics to understand the influence and prestige of articles within the network.

## Key Findings
- Identified articles with high centrality metrics, highlighting the influence of topics related to countries and significant historical events.
- Revealed a pronounced Western bias in the network's structure, with an overrepresentation of Western countries.

## Future Work
- Extend the analysis to other language versions of Wikipedia to explore cultural and linguistic influences on knowledge organization.
- Further investigate the causes of the observed Western bias and its implications on global knowledge representation.

## Usage
For a detailed exploration of the network and to run the centrality measures:

- Ensure Python and relevant libraries (networkx, pandas) are installed.
- Download wiki-topcats-categories.txt.gz, wiki-topcats-page-names.txt.gz, and wiki-topcats.txt.gz from https://snap.stanford.edu/data/wiki-topcats.html
- Run the provided Jupyter notebooks (centrality_measures.ipynb, country_analysis.ipynb) for interactive analysis.
- Use g_funcs.py and centrality_measures.py for graph functions and calculations.

## Resources
- Project Proposal
- Exploring Network Dynamics and Centrality Within The Wiki-Topcats Network (Paper)
- Project Presentation

## Acknowledgements
Thanks to the Stanford Large Network Dataset Collection for providing the dataset and to all contributors to the Wikipedia hyperlink graph analysis.

For further inquiries or contributions, please contact the team members.
