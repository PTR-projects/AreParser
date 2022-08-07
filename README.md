# Parser ad data visualizer for Arecoreder 

## Usage

To use this software you need to put a file with measurments into folder with Parser.py and then execute said .py file with:

```shell
python Parser.py
```

After few seconds, depending on .csv file size window should pop up. 

## Data format

After opening window, 4 subplots should appear. 
* First one visualizes accelerations on all 3 axis in |24g| range
* Second plots pressure in form of RAW data and Kalman filtered
* Third shows altitude obtained from pressure and second order acceleration integral
* Las one is velocity from pressure and acceleration integral