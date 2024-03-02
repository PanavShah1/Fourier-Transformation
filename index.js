var elt = document.getElementById('calculator');
var calculator = Desmos.GraphingCalculator(elt);

// calculator.setExpression({id: 'circle', latex: 'x^2+y^2 < 1'})
calculator.setExpression({id: 'm1', latex: 'y='})

var state = calculator.getState().expressions.list[0].latex
console.log(state)

var function_ = calculator.getState().expressions.list[0].latex

function userChange(){
    state = calculator.getState()
    console.log(state)
    // calculator.setExpression({id: 'm1', latex: 'y=\\sin(x)'})
    function_ = calculator.getState().expressions.list[0].latex

    if (function_ != "y="){
        document.getElementById("pointer").hidden = true
    }
    else{
        document.getElementById("pointer").hidden = false
    }

    
}
// calculator.addEventListner("click", userChange)
elt.addEventListener("click", userChange)
document.addEventListener("keyup", userChange)


function format(equation){
    equation = equation.replaceAll("\\cos", "cos")
    equation = equation.replaceAll("\\sin", "sin")
    equation = equation.replaceAll("\\pi", "π")
    equation = equation.replaceAll("+ -", "- ")
    equation = equation.replaceAll("*", "")

    return equation
}

function go(){
    function_ = calculator.getState().expressions.list[0].latex
    console.log("function : "+function_)
    myPromise = api_call(function_)

    myPromise.then(
        function(value){
            graph = value.graph
            console.log(value.graph)
            calculator.setExpression({id: 'm2', latex: (graph)})
            document.getElementById("fourier-function").value = format(graph)
        },
        function(error){
            console.log(error)
        }
    )
}
// range_min = 1
// range_max = 5
// no_data_points = 10
document.getElementById("range-min").value = 1
document.getElementById("range-max").value = 10
document.getElementById("no-data-points").value = 10
var range_min_ = 1
var range_max_ = 10
no_data_points_ = 10
function input_data(){
    range_min_ = document.getElementById("range-min").value
    range_max_ = document.getElementById("range-max").value
    no_data_points_ = document.getElementById("no-data-points").value
    console.log(range_min_, range_max_, no_data_points_)
}
document.addEventListener("input", input_data)







async function api_call(function_) {
    const apiUrl = `http://127.0.0.1:8000/operate/`;
    const requestData = {graph: function_, range_min: parseFloat(range_min_), range_max: parseFloat(range_max_), no_data_points: parseFloat(no_data_points_)}
    console.log(requestData)

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await response.json();
        console.log("Response from API:", data);
        return data;
    } catch (error) {
        console.error("Error:", error);
        throw error; // Re-throw the error to handle it outside of the function if needed
    }
}


