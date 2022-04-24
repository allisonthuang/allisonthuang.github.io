**[Link to create task](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)**

## Allison's Create Task Plan
Program short description/Data Collection Type: A user inputs the number of the magnitude of earthquake that you felt, then it pulls up from a database and generates the other locations that people who have inputted have felt that earthquake. 

Procedure that contributes to the purpose (w/output on graph): Then, you can click a button that says add into graph, and then add your data into a dotplot so you can see the distribution of earthquake magnitudes of people around you. The procedure that I'll include is probably how the data from the database is sorted and combined to fit into a graph. 

## Create Task Content

### [Runtime Video Link](https://youtu.be/8-k_yPk_hU0)

### [Final Committed Program Code](https://github.com/allisonthuang/allisonthuang.github.io/blob/main/earthquakegraph.html)

### Written Response to Create Task
3a i. The overall purpose of the program is for users to create/simulate a graph of what they felt at (x,y) coordinate points, and for users to receive advice based upon the data they entered.

3a ii. The program generates a square based on three parameters: x-coordinate, y-coordinate and earthquake magnitude. Depending on the magnitude, the program will also display a randomly generated advice message.

3a iii. The input of the program are integers for one x-coordinate, one y-coordinate, and one magnitude. X-coordinate and y-coordinate values can be greater than, equal to, or less than 0. Magnitude can range from 1 to 10. Based on these three parameters, the program will output a square and an advice message that corresponds to the magnitude of the earthquake.

3b i.
`<script>
    const good = [ "That's not the worst", "OK you'll be fine", "Stay safe!" ];
    const bad = [ "Evacuate your family immediately.", "GET OUT. NOW!", "Find shelter immediately!" ];
</script>`


3b ii.
`<script>
    function magnitude(mag){
        if ((parseInt(mag) == 1) || (parseInt(mag) == 2) || (parseInt(mag) == 3)) {
            const magni = Math.floor(Math.random() * good.length);
            console.log(magni, good[magni]);
            document.getElementById("arrPrint").innerHTML = good[magni];
        }
        else{
            const magni = Math.floor(Math.random() * bad.length);
            console.log(magni, bad[magni]);
            document.getElementById("badPrint").innerHTML = bad[magni];
        }
    }
</script>`


3b iii. “good” and “bad” are the arrays being used.

3b iv. The data in the array represents advice messages and phrases that are associated with lower (good) or higher (bad) earthquake magnitudes.

3b v. Without the array, different users would receive the same message every time they tried to use the generator. It wouldn’t make sense that each user received the same message. With the array, I can store multiple possible messages and randomize them. Without the array, there would only have to be one prescribed message to each magnitude.

3c i. 
`<script>
    function magnitude(mag){
        if ((parseInt(mag) == 1) || (parseInt(mag) == 2) || (parseInt(mag) == 3)) {
            const magni = Math.floor(Math.random() * good.length);
            console.log(magni, good[magni]);
            document.getElementById("arrPrint").innerHTML = good[magni];
        }
        else{
            const magni = Math.floor(Math.random() * bad.length);
            console.log(magni, bad[magni]);
            document.getElementById("badPrint").innerHTML = bad[magni];
        }
    }
</script>`

3c ii. 
`<button onclick="magnitude(document.getElementById('lvar').value)"> Create </button>`

3c iii. The procedure randomly selects an item from an array dependent on the parameter of magnitude.

3c iiii. First, the function is defined as “magnitude” with the parameter “mag.” From there, it is simpler logic. If the magnitude (mag) inputted by the user is one of the values 1, 2, or 3, then the operation Math.floor is returning the largest integer less than or equal to a random number from the “good” array. Then, the console.log statement is printing that result. The document.getElementByID assigns an ID to print the result, which is displayed elsewhere in the .html document. The else statement operates similarly, except with the “bad” array.

3d i. The first call is the onclick of the button, which displays the result of the procedure “magnitude” that has the parameter of lvar. The second call is also a button, which at the onclick of the button displays the result of the procedure “square” on the graph.

3d ii. The condition tested by the first call is whether the phrase is positive or negative. The condition tested by the second call is how large and where the square is placed on the grid.

3d iii. The result of the first call is a phrase that is dependent on the magnitude inputted, with a high magnitude, it generates a warning (negative) phrase. With a low magnitude, it generates a good/reassuring (positive) phrase. The result of the second call is a square that is generated based on the three parameters of x-coordinate, y-coordinate, and magnitude. The results of the call (the square) get placed on the grid.




