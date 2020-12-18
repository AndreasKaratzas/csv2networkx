
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# TODO: After project completion execute: pip freeze > requirements.txt
def main():
    df_before = pd.read_csv("./before.csv", names=["X", "Y"])
    G = nx.Graph()
    for i in df_before.iterrows():
        G.add_node(i[0], pos=(i[1].X, i[1].Y))
        if i[0] != 0:
            G.add_edge(i[0] - 1, i[0])
    G.add_edge(df_before.shape[0] - 1, 0)
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos)
    plt.show()
    plt.savefig("before" + ".png", dpi=300, bbox_inches='tight')
    df_after = pd.read_csv("./after.csv", names=["X", "Y"])
    G = nx.Graph()
    for i in df_after.iterrows():
        G.add_node(i[0], pos=(i[1].X, i[1].Y))
        if i[0] != 0:
            G.add_edge(i[0] - 1, i[0])
    G.add_edge(df_after.shape[0] - 1, 0)
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos)
    plt.show()
    plt.savefig("after" + ".png", dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    main()
