# Parser ad data visualizer for Arecoreder 

## Usage

To use this software you need to put a file with measurments into folder with Parser.py and then execute said .py file with:

```shell
python Parser.py
```

After few seconds, depending on .csv file size window should pop up. 

## Data format

After opening window, 4 subplots should appear:
* First one visualizes accelerations on all 3 axis in |24g| range
* Second plots pressure in form of RAW data and Kalman filtered
* Third shows altitude obtained from pressure and second order acceleration integral
* Las one is velocity from pressure and acceleration integral

## Sources:
* [Arecorder thread](https://www.forum.rakiety.org.pl/viewtopic.php?p=31879&hilit=arecorder#p31879)
* [Instructions manual (PL)](https://drive.google.com/file/d/1ujWXMafTv1fnUb7v_bf8Bu2hM3gAQGBD/view)
* [Instructions manual (EN)](https://drive.google.com/file/d/1kpMVD8JVcOfqZkLpwjSBWpt2eQ2miaQd/view)
* [Configuration tool](https://drive.google.com/file/d/1b-haXZP8a1FCob4YfWzAAo6OGfvEhVCZ/view)