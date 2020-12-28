# CSV to Graph

## Description

In this repository, there is an implementation of *CSV* to *Graph (V, E)* transform using `Python 3.8` . The repository was created to validate the results of the TSP algorithm using a naive approach, which is implemented here.

## Installation

* Open a Terminal
* Change to Project directory
* Execute `pip install -r requirements.txt`

## Setup 

* Create a directory `data` inside the Project directory
* Place all `graph.csv` files in `./data`
* Create a directory `output` inside the Project directory

## Notes

The filename of the input data must follow the format **graph[x]** where `x` is any natural number including 0. The input files must have 2 columns of integers and no headers. The input files must be of CSV file type.

## Results

After its execution, the program saves its results into `./output` directory. The results will be PNG files and the ammount of those files is equal to the number of input files. An example PNG file output by the program is attached below:

![Sample Graph Output](output/graph05.png)
