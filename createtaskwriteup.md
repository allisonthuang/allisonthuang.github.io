**[Link to create task](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)**

## Create Task Content

### [Runtime Video Link](https://drive.google.com/file/d/17YDttxZEh3itEvA15FTNoinsc3nxf7FD/view?usp=sharing)

### [Program Code](https://github.com/allisonthuang/allisonthuang.github.io/blob/main/earthquakegraph.html)

### Written Response to Create Task
3a i. The overall purpose of the program is for users to obtain more information about the earthquake they felt at their location. People can obtain more information about earthquakes from this program. It can help create/simulate a graph of what they felt at (x,y) coordinate points with magnitude (l), help users receive advice based upon inputted values, add their data to a list, and take the average of all the data.

3a ii. The program generates a square based on three parameters: x-coordinate, y-coordinate and earthquake magnitude. Depending on the magnitude, the program will also display a randomly generated advice message. The program will also give advice based upon the values that are inputted, compile and average magnitudes.

3a iii. The input of the program are integers for one x-coordinate, one y-coordinate, and one magnitude. X-coordinate and y-coordinate values can be greater than, equal to, or less than 0. Magnitude can range from 1 to 10. Based on these three parameters, the program will output a square and an advice message that corresponds to the magnitude of the earthquake. From the inputted magnitudes, they are compiled in a array. Then, the average is taken from that array of magnitudes.

3b i.
![image](https://user-images.githubusercontent.com/89219200/165346545-84a6eaf2-9302-4601-9ffc-b6476e024201.png)


3b ii.
![image](https://user-images.githubusercontent.com/89219200/165346578-2e738bd0-861a-4fc7-bf49-1ed44d6d3624.png)


3b iii. "magnitudes" is the array being used.

3b iv. The data in the array represents a list of the magnitude of the earthquakes that all users have felt and inputted into the program.

3b v. The identified procedure "magaverage" takes the array "magnitudes" from the "compare" procedure, and takes the average of all the current values in the array. Without the array of magnitudes formed from the "compare" procedure, the draw graph, feedback, and average functions would not be able to work in the program. All the other overall program functionalities are tangent upon the inputted magnitudes, and would not be able to function without it. Without the list, then the average of the multiple magnitudes can't be calculated, and data would all have to be inputted at once.

3c i. ![image](https://user-images.githubusercontent.com/89219200/165346694-a9ce5598-9055-426e-a07a-f53e4f670731.png)

3c ii. ![image](https://user-images.githubusercontent.com/89219200/165346754-7b5b5a78-d54a-4eec-b1eb-f17eff2d7a07.png)

3c iii. The procedure randomly selects an item from an array dependent on the parameter of magnitude.

3c iv. First, the function is defined as “magnitude” with the parameter “mag.” From there, it is simpler logic. If the magnitude (mag) inputted by the user is one of the values 1, 2, or 3, then the operation Math.floor is returning the largest integer less than or equal to a random number from the “good” array. Then, the console.log statement is printing that result. The document.getElementByID assigns an ID to print the result, which is displayed elsewhere in the .html document. The else statement operates similarly, except with the “bad” array.

3d i. 1st call: If a user inputs a value from 1-3 from the magnitude, and clicks the get advice button to call the "magnitude" procedure. The first call will generate a random element from the low magnitude advice array ("good" array).

2nd call: If a user inputs a value greater than 3 from the magnitude, and clicks the get advice button to call "magnitude" procedure. The second call will generate a random element from the high magnitude advice array ("bad" array).


3d ii. 1st call: The condition tested by the first call is whether the inputted magnitude is from 1-3 (a low magnitude). If the first condition is true, the program will display a randomly generated value from the "good" array.


2nd call: The condition tested by the second call is whether the inputted magnitude is greater than 3 (a high magnitude). If the first condition is false, then the program will default to the second call. If the second condition is true, the second call will have the program display a randomly generated value from the "bad" array.

3d iii. 1st call: The result of the first call is a randomly generated advice phrase. It is dependent on the magnitude inputted. With a magnitude from 1-3, it will generate random advice from the "good" array. If the condition is false, it will go to the second call.

2nd call: The result of the second call is a randomly generated advice phrase. It is dependent on the magnitude inputted. With a magnitude greater than 3, it will generate random advice from the "bad" array.
