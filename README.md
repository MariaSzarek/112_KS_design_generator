# Sewage system with Turtle

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#running)

## General info
Sewage System Route Generator calculates the total length and depth 
of pipes for installation and generate pipeline routes with turtle. 
The generator is based on the A* algorithm.
Input data are kept in points.csv. Mandatory structure of the file:

![img.png](img.png)

>15, 10,  length and width of the building
>
>x, y
>
>8, 0, last point of sewage system, need to be (x, 0)
>
>10, 9, sample point
>
>1, 5, sample point
>
> ... , rest points


Program generates routes.csv with data:
* for each point connected to the sewage system routes (point by point)
* longest route
* length
* depth


## Technologies
* turtle
* csv

## Future developent
To return dimension of pipes depending on how many points are already 
connected to main pipe and change slope of pipes.

## Running
To run this project 
>python main.py 


