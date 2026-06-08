import networkx as nx
import matplotlib.pyplot as plt

def prim(G):
    masinf=float('inf')
    A={v:(None,masinf) for v in G.nodes}
    v0=list(A.keys())[0]
    del(A[v0])

    aristas_buenas=[]

    for v in G.neighbors(v0):
       A[v]=(v0,G[v][v0]['weight'])

    while A:
        # Encontrar la mejor arista de T a A y agregarla al árbol.
        # Debe de ser de entre las mejores para cada vértice.
        mejor_peso=masinf
        for v in A.keys():
            if A[v][1]<mejor_peso:
                mejor=v
                mejor_peso=A[v][1]
        aristas_buenas.append((mejor,A[mejor][0],A[mejor][1]))
        del(A[mejor])

        # Actualizar las mejores para cada vértice, si es necesario.
        for v in G.neighbors(mejor):
            if v in A.keys():
                if A[v][1]>G[v][mejor]['weight']:
                    A[v]=(mejor,G[v][mejor]['weight'])
    return aristas_buenas


    //H=nx.Graph()
H.add_weighted_edges_from(prim(G))

KKL=nx.kamada_kawai_layout(G)

fig, ax= plt.subplots(1,2)
fig.set_size_inches(12,6)

ax[0].set_title('Gráfica original')
nx.draw_kamada_kawai(G,ax=ax[0],with_labels=True, node_color='#bbbb22',node_size=500)
nx.draw_networkx_edge_labels(G,KKL,ax=ax[0],edge_labels=labels)

labels2 = nx.get_edge_attributes(H,'weight')
ax[1].set_title('Árbol de peso mínimo')
nx.draw(H,pos=KKL,ax=ax[1],with_labels=True, node_color='#bbbb22',node_size=500)
nx.draw_networkx_edge_labels(H,KKL,ax=ax[1],edge_labels=labels2)

plt.plot()//