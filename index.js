var elt = document.getElementById('calculator');
var calculator = Desmos.GraphingCalculator(elt);

// calculator.setExpression({id: 'circle', latex: 'x^2+y^2 < 1'})
calculator.setExpression({id: 'm1', latex: 'y=x*x'})

var state = calculator.getState().expressions.list[0].latex
console.log(state)

function userChange(){
    state = calculator.getState()
    console.log(state)
    // calculator.setExpression({id: 'm1', latex: 'y=\\sin(x)'})
    function_ = calculator.getState().expressions.list[0].latex
    console.log("function : "+function_)
    myPromise = api_call(function_)

    myPromise.then(
        function(value){
            console.log(value.graph)
            calculator.setExpression({id: 'm2', latex: (value.graph)})
        },
        function(error){
            console.log(error)
        }
    )
}
// calculator.addEventListner("click", userChange)
elt.addEventListener("click", userChange)


async function api_call(function_) {
    const apiUrl = `http://127.0.0.1:8000/operate/`;
    const requestData = {graph: function_}

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


