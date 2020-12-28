
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from natsort import natsorted


def export_tsp_route():
    debug_graph_df = pd.read_csv(file_data_path + debug_data[i], names=cols)
    G_deb_graph = nx.Graph()
    for r_deb_g in debug_graph_df.iterrows():
        G_deb_graph.add_node(r_deb_g[0], pos=(r_deb_g[1].X, r_deb_g[1].Y))
        if r_deb_g[0] != 0:
            G_deb_graph.add_edge(r_deb_g[0] - 1, r_deb_g[0], weight=1)
    G_deb_graph.add_edge(debug_graph_df.shape[0] - 1, 0)
    pos = nx.get_node_attributes(G_deb_graph, 'pos')
    G_deg_g_weights = nx.get_edge_attributes(G_deb_graph, 'weight').values()
    nx.draw(G_deb_graph,
            pos,
            width=list(G_deg_g_weights),
            with_labels=True,
            node_color='lightgreen')
    plt.savefig(export_dir + exported_filename + str(padding).zfill(padding_len) + ".png", dpi=image_quality)
    plt.clf()


if __name__ == "__main__":
    # user must create input dir and replace this filename with the user defined input dir filename
    file_data_path = "./data/"
    # user must replace this string with the desired filename to appoint to output files
    exported_filename = "graph"
    # user must create output dir and replace this filename with the user defined output dir filename
    export_dir = "./output/"
    mode = "TSP"
    image_quality = 300
    cols = ["X", "Y"]
    items = [f for f in os.listdir(os.getcwd() + file_data_path)
             if os.path.isfile(os.path.join(os.getcwd() + file_data_path, f))]
    padding_len = len(str(len(items))) + 1
    debug_data = natsorted(list(filter(lambda k: "graph" in k, items)))
    acs_tsp = natsorted(list(filter(lambda k: "acs_tsp" in k, items)))
    debug_data = debug_data + acs_tsp
    if len(debug_data) + len(acs_tsp) == 0:
        exit(-1)
    padding = 0
    for i in range(len(
        [name for name in os.listdir(file_data_path) if os.path.isfile(os.path.join(file_data_path, name))]
    )):
        export_tsp_route()
        padding = padding + 1
