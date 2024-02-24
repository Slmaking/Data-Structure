# Data-Structure and algorithm 

# Fundamental Algorithms and Data Structures

This repository is a comprehensive collection of Java and Python implementations of fundamental algorithms and data structures, inspired by the curriculum of Princeton University. It serves as an educational resource for understanding and applying key concepts in computer science, with an emphasis on applications and scientific performance analysis.

## Structure

The repository is organized into two main parts:

### Part I: Elementary Data Structures, Sorting, and Searching

Covers basic data structures and algorithms for sorting and searching, including:

- Union-Find
- Binary Search
- Stacks, Queues, Bags
- Various Sorting Algorithms
- Binary Heaps
- Binary Search Trees and Red-Black Trees
- Hash Tables
- Geometric Algorithms and kd-Trees

### Part II: Graph and String-Processing Algorithms

Focuses on advanced topics in graph theory and string processing, including:

- Graph Algorithms
- String-Processing Algorithms
- Compression and Encoding Algorithms
- Reductions and Intractability

# Data Structures and Algorithms

 <h2>Data Structures and Algorithms Summary</h2>
<table>
    <tr>
        <th>Topic</th>
        <th>Data Structures and Algorithms</th>
        <th>Part</th>
    </tr>
    <tr>
        <td>Data Types</td>
        <td>stack, queue, bag, union-find, priority queue</td>
        <td rowspan="3">Part 1</td>
    </tr>
    <tr>
        <td>Sorting</td>
        <td>quicksort, mergesort, heapsort</td>
    </tr>
    <tr>
        <td>Searching</td>
        <td>BST, red-black BST, hash table</td>
    </tr>
    <tr>
        <td>Graphs</td>
        <td>BFS, DFS, Prim, Kruskal, Dijkstra</td>
        <td rowspan="3">Part 2</td>
    </tr>
    <tr>
        <td>Strings</td>
        <td>radix sorts, tries, KMP, regexps, data compression</td>
    </tr>
    <tr>
        <td>Advanced</td>
        <td>B-tree, suffix array, maxflow</td>
    </tr>
</table>


## Sorting models comaparision

<table border="1">
    <tr>
        <th>Implementation</th>
        <th colspan="3" style="text-align:center">Worst-case cost (after N inserts)</th>
        <th colspan="3" style="text-align:center">Average case (after N random inserts)</th>
        <th>Ordered iteration?</th>
        <th>Key interface</th>
    </tr>
    <tr>
        <td></td>
        <td style="text-align:center">search</td>
        <td style="text-align:center">insert</td>
        <td style="text-align:center">delete</td>
        <td style="text-align:center">search hit</td>
        <td style="text-align:center">insert</td>
        <td style="text-align:center">delete</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Sequential search (unordered list)</td>
        <td>N</td>
        <td>N</td>
        <td>N</td>
        <td>N/2</td>
        <td>N</td>
        <td>N/2</td>
        <td>no</td>
        <td><code>equals()</code></td>
    </tr>
    <tr>
        <td>Binary search (ordered array)</td>
        <td>lg N</td>
        <td>N</td>
        <td>N</td>
        <td>lg N</td>
        <td>N/2</td>
        <td>N/2</td>
        <td>yes</td>
        <td><code>compareTo()</code></td>
    </tr>
    <tr>
        <td>BST</td>
        <td>N</td>
        <td>N</td>
        <td>N</td>
        <td>1.39 lg N</td>
        <td>1.39 lg N</td>
        <td>sqrt(N)</td>
        <td>yes</td>
        <td><code>compareTo()</code></td>
    </tr>
    <tr>
        <td>2-3 tree</td>
        <td>c lg N</td>
        <td>c lg N</td>
        <td>c lg N</td>
        <td>c lg N</td>
        <td>c lg N</td>
        <td>c lg N</td>
        <td>yes</td>
        <td><code>compareTo()</code></td>
    </tr>
    <tr>
        <td>Red-black BST</td>
        <td>2 lg N</td>
        <td>2 lg N</td>
        <td>2 lg N</td>
        <td>1.00 lg N*</td>
        <td>1.00 lg N*</td>
        <td>1.00 lg N*</td>
        <td>yes</td>
        <td><code>compareTo()</code></td>
    </tr>
</table>
<p>* exact value of coefficient unknown but extremely close to 1</p>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sorting Summary</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>


## Sorting Algorithm Summary


    <h2>Sorting Summary</h2>
    <table>
        <tr>
            <th>Algorithm</th>
            <th>Inplace?</th>
            <th>Stable?</th>
            <th>Worst</th>
            <th>Average</th>
            <th>Best</th>
            <th>Remarks</th>
        </tr>
        <tr>
            <td>Selection</td>
            <td>✔️</td>
            <td></td>
            <td>N / 2</td>
            <td>N / 2</td>
            <td>N / 2</td>
            <td>N exchanges</td>
        </tr>
        <tr>
            <td>Insertion</td>
            <td>✔️</td>
            <td>✔️</td>
            <td>N / 2</td>
            <td>N / 4</td>
            <td>N</td>
            <td>Use for small N or partially ordered</td>
        </tr>
        <tr>
            <td>Shell</td>
            <td>✔️</td>
            <td></td>
            <td>?</td>
            <td>?</td>
            <td>N</td>
            <td>Tight code, subquadratic</td>
        </tr>
        <tr>
            <td>Merge</td>
            <td></td>
            <td>✔️</td>
            <td>N lg N</td>
            <td>N lg N</td>
            <td>N lg N</td>
            <td>N log N guarantee, stable</td>
        </tr>
        <tr>
            <td>Quick</td>
            <td>✔️</td>
            <td></td>
            <td>N / 2</td>
            <td>2 N ln N</td>
            <td>N lg N</td>
            <td>Fastest in practice</td>
        </tr>
        <tr>
            <td>3-way Quick</td>
            <td>✔️</td>
            <td>✔️</td>
            <td>N / 2</td>
            <td>2 N ln N</td>
            <td>N</td>
            <td>Improves quicksort in presence of duplicate keys</td>
        </tr>
        <tr>
            <td>Ideal</td>
            <td>✔️</td>
            <td>✔️</td>
            <td>N lg N</td>
            <td>N lg N</td>
            <td>N lg N</td>
            <td>Holy sorting grail</td>
        </tr>
    </table>

</body>
</html>



## Usage

Each directory within this repository corresponds to a specific topic or algorithm and contains both Java and Python implementations. Detailed README files are provided in each directory to explain the concepts, applications, and performance analysis of the implementations.

## Contributing

Contributions to this repository are welcome.

![image](https://github.com/Slmaking/Data-Structure/assets/58626257/2a61e1d6-3a12-48c1-9244-cbd51a748e6f)


