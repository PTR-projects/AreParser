#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv
import os

x = []
Xacc = []
Yacc = []
Zacc = []

P = []
Kp = []

AltP = []
Alt = []

Vaxis = []
Vp = []

X_1_g = 0
Hx_1_g = 0
X_0_g = 0
Hx_0_g = 0

Y_0_g = 0
Z_0_g = 0

cnt = 0
fileList = os.listdir()
csvList = []

for file in fileList:
    if file.startswith('MEAS'):
        csvList.append(file)

with open(csvList[0], 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        if cnt == 6:
            X_1_g = int(row[1])
        elif cnt == 7:
            Hx_1_g = int(row[1])
        elif cnt == 8:
            X_0_g = int(row[1])
        elif cnt == 9:
            Hx_0_g = int(row[1])
        elif cnt == 10:
            Y_0_g = int(row[1])
        elif cnt == 11:
            Z_0_g = int(row[1])
        elif cnt >= 25:
            if row[0] != 'Rocket angle at launch':
                x.append(float(row[0]))
                Xacc.append((int(row[1]) - X_0_g) / X_1_g)
                Yacc.append((int(row[2]) - Y_0_g) / X_1_g)
                Zacc.append((int(row[3]) - Z_0_g) / X_1_g)

                P.append(int(row[5]) / 100)
                Kp.append(int(row[6]) / 100)

                AltP.append(float(row[9]))
                Alt.append(float(row[10]))

                Vaxis.append(float(row[8]))
                Vp.append(float(row[12]))
            else:
                break
        cnt += 1

(figure, axis) = plt.subplots(2, 2)

axis[0, 0].plot(
    x,
    Xacc,
    color='r',
    linestyle='solid',
    marker='',
    label='X axis',
    )
axis[0, 0].plot(
    x,
    Yacc,
    color='g',
    linestyle='solid',
    marker='',
    label='Y axis',
    )
axis[0, 0].plot(
    x,
    Zacc,
    color='b',
    linestyle='solid',
    marker='',
    label='Z axis',
    )

axis[0, 0].legend()
axis[0, 0].set_title('Acceleration')
axis[0, 0].set_xlabel('seconds', fontsize=1)
axis[0, 0].set_ylabel('g')

axis[0, 1].plot(
    x,
    P,
    color='r',
    linestyle='solid',
    marker='',
    label='Pressure',
    )
axis[0, 1].plot(
    x,
    Kp,
    color='g',
    linestyle='solid',
    marker='',
    label='Kalman pressure',
    )

axis[0, 1].legend()
axis[0, 1].set_title('Pressure')
axis[0, 1].set_xlabel('seconds', fontsize=1)
axis[0, 1].set_ylabel('hPa')

axis[1, 0].plot(
    x,
    AltP,
    color='r',
    linestyle='solid',
    marker='',
    label='Altitude pressure',
    )
axis[1, 0].plot(
    x,
    Alt,
    color='g',
    linestyle='solid',
    marker='',
    label='Altitude',
    )

axis[1, 0].legend()
axis[1, 0].set_title('Altitude')
axis[1, 0].set_xlabel('seconds', fontsize=1)
axis[1, 0].set_ylabel('m')

axis[1, 1].plot(
    x,
    Vaxis,
    color='r',
    linestyle='solid',
    marker='',
    label='Velocity',
    )
axis[1, 1].plot(
    x,
    Vp,
    color='g',
    linestyle='solid',
    marker='',
    label='Velocity pressure',
    )

axis[1, 1].legend()
axis[1, 1].set_title('Velocity')
axis[1, 1].set_xlabel('seconds', fontsize=1, rotation=30)
axis[1, 1].set_ylabel('m/s')

# plt.xticks(rotation = 30)

plt.show()

def test_placeholder():
    pass
