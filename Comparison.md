# ST implementations: summary

| Implementation                        | Worst-case cost (after N inserts) | | | Average case (after N random inserts) | | | Ordered iteration? | Key interface |
| ------------------------------------- |:---------------------------------:|:---:|:---:|:---------------------------------------:|:---:|:---:|:-----------------:|:-------------:|
|                                       | search | insert | delete | search hit | insert | delete |                   |                 |
| Sequential search (unordered list)    | N      | N      | N      | N/2        | N      | N/2    | no                | `equals()`      |
| Binary search (ordered array)         | lg N   | N      | N      | lg N       | N/2    | N/2    | yes               | `compareTo()`   |
| BST                                   | N      | N      | N      | 1.39 lg N  | 1.39 lg N | ?    | yes               | `compareTo()`   |
| 2-3 tree                              | c lg N | c lg N | c lg N | c lg N     | c lg N | c lg N | yes               | `compareTo()`   |
| Red-black BST                         | 2 lg N | 2 lg N | 2 lg N | 1.00 lg N* | 1.00 lg N* | 1.00 lg N* | yes               | `compareTo()`   |

\* exact value of coefficient unknown but extremely close to 1


# Sorting summary

| Algorithm   | Inplace? | Stable? | Worst       | Average     | Best       | Remarks                      |
|-------------|:--------:|:-------:|:-----------:|:-----------:|:----------:|------------------------------|
| Selection   | ✔️       |         | N / 2       | N / 2       | N / 2      | N exchanges                  |
| Insertion   | ✔️       | ✔️      | N / 2       | N / 4       | N          | Use for small N or partially ordered |
| Shell       | ✔️       |         | ?           | ?           | N          | Tight code, subquadratic     |
| Merge       |          | ✔️      | N lg N      | N lg N      | N lg N     | N log N guarantee, stable    |
| Quick       | ✔️       |         | N / 2       | 2 N ln N    | N lg N     | Fastest in practice          |
| 3-way Quick | ✔️       |         | N / 2       | 2 N ln N    | N          | Improves quicksort in presence of duplicate keys |
| ???         | ✔️       | ✔️      | N lg N      | N lg N      | N lg N     | Holy sorting grail           |
