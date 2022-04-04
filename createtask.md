{% include navigation.html %}

## Create Task from Tri 2
### [Plan and Writeup](https://github.com/christinlee367/n225_FireEradicatorsTheSequel/wiki/Allison's-Create-Task-Plan)
#### [Runtime Video](https://youtu.be/8-k_yPk_hU0), [Final Committed Program Code](https://github.com/christinlee367/n225_FireEradicatorsTheSequel/blob/main/templates/earthquakegraph.html) & [Written Response to Create Task](https://github.com/christinlee367/n225_FireEradicatorsTheSequel/wiki/Allison's-Create-Task-Plan#written-response-to-create-task)
- Program short description/Data Collection Type: A user inputs the number of the magnitude of earthquake that you felt, then it pulls up from a database and generates the other locations that people who have inputted have felt that earthquake.
- Procedure that contributes to the purpose (w/output on graph): Then, you can click a button that says add into graph, and then add your data into a dotplot so you can see the distribution of earthquake magnitudes of people around you. The procedure that I'll include is probably how the data from the database is sorted and combined to fit into a graph.

### Code Snippets
##### List usage
``` python
<script>
    const good = [ "That's not the worst", "OK you'll be fine", "Stay safe!" ];
    const bad = [ "Evacuate your family immediately.", "GET OUT. NOW!", "Find shelter immediately!" ];
</script>
```

##### Conditional Statement & Call
``` python
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
</script>
```

### Runtime
