# Parser ad data visualizer for Arecoreder 

##Installing

In order to run program you need python 3 with isntalled matplotlib 
```shell
pip install matplotlib
```
and csv
```shell
pip install csv
```

## Usage

To use this software you need to put a file with measurments into folder with Parser.py and then execute said .py file with:

```shell
python Parser.py
```
**Keep in mind that this program will open first file with name `MEAS*.csv` That is present in folder, for opening multiple files keep them in separate folders**

After few seconds, depending on .csv file size window should pop up. 

## Data format

After opening window, 4 subplots should appear:
* First one visualizes accelerations on all 3 axis in `24g` range
* Second plots pressure in form of RAW data and Kalman filtered
* Third shows altitude obtained from pressure and second order acceleration integral
* Las one is velocity from pressure and acceleration integral

## Sources:
* [Arecorder thread](https://www.forum.rakiety.org.pl/viewtopic.php?t=3039)
* [Instructions manual (PL)](https://drive.google.com/file/d/1ujWXMafTv1fnUb7v_bf8Bu2hM3gAQGBD/view)
* [Instructions manual (EN)](https://drive.google.com/file/d/1kpMVD8JVcOfqZkLpwjSBWpt2eQ2miaQd/view)
* [Configuration tool](https://drive.google.com/file/d/1b-haXZP8a1FCob4YfWzAAo6OGfvEhVCZ/view)

## All above software is made using funding from [Odkrywcy Diamentów](https://odkrywcydiamentow.com.pl/)
![alt text](https://odkrywcydiamentow.com.pl/wp-content/uploads/2017/09/cropped-Odkrywcy_logo-1.png)
