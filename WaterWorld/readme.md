	Year is 3030, water is a scare resource. Civilaizations live around glaciers in clusters, with a federal body (identified as F)
	in center melting glaciers and controlling the water distribution. Each cluster has need for water for a day and a water storage
	capacity. Cluster are connected to each other with a pipe identified by _. Pipes are flow controlled and water flows in forward
	direction only.	Every time water starts flowing through pipe, the clusters drain their tanks for use in other activities, as
	they can use the water flowing to fill the tanks, and federal body sends water till the capacity is full. Tanks are empty at
	begining of day, water tanks fill in an instant. Clusters don't share their water with other clusters, but allow federal water
	to flow through the pipe. Federal body releases water at start of day, cluster uses water at end of day. In a pipe link like 
	F-C1-C2-C3-C4, when federal water body targets C3, only C3 and nodes before it (here C1,C2,C3) can fill the tank, 
	C4 can fill it only when it's targeted.

Calculate the minimum water needed to help the civilizations survive for n days.

Input is multiline. First line is the number of days to survive. Second line the number of clusters followed by their definitions. Next is the number of links in the system, followed by the link definition.

Custer defintion
C1 100 300
here

C1 - cluster name
100 - daily water need
300 - storage capacity
Link definition
F_C1
here

F - is the federal source of pipe
C - is the sink/destination of pipe (cluster tank)
Input
2
3 
C1 100 300
C2 150 300
C3 100 100
3
F_C1
F_C2
C2_C3
Output
1100
Input
2
3 
C1 100 300
C2 150 300
C3 100 100
3
F_C1
F_C2
F_C3
Output
800
Input
3
4 
C1 100 300
C2 100 300
C3 100 200
C4 100 400
4
F_C1
F_C2
C2_C3
C3_C4
Output
1700
