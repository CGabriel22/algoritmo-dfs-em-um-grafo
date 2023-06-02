# Algoritmo Busca em Profundidade (depth-first search - DFS)

O algoritmo permite "caminhar" em um grafo, explorar todos os vértices e arestas, retornando dados úteis sobre o gráfico.

## Aplicações:

Resolução de problemas enumerativos. Organização de grupos. Localizar arquivos em sistemas operacionais.

## Notações:

- <b>vetor d</b>: marca o instante que o vértice foi descoberto;
- <b>vetor f</b>f: marca o instante que o fecho transitivo do vértice foi totalmente visitado
- <b>v[G]</b>: Vetor dos vértices de G [c, a, b, d, e, f, g, h]
- <b>mark</b>: Contador de tempo
- <b>cor[u]</b>: Cor do vértice u

## Cores:

- Branco: Vértice desconhecido
- Cinza: Vértice encontrado
- Preto: Vértice encontrado, com fecho positivo totalmente visitado

## Arquivo:

O arquivo exemplo define em sua primeira linha nesta ordem: qnt de vertices, arestas e se direcionado.

Nas demais linhas define o vértice e seu adjacente, ou seja, uma aresta.
