function tokenizePrompt() {
    const prompt = document.getElementById("prompt").value;

    fetch("/tokenize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: prompt }),
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = "Data: " + data;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function classifyPrompt() {
    const prompt = document.getElementById("prompt").value;

    fetch("/classify", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: prompt }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        const resultDiv = document.getElementById("result");
        const mostSimilarSentence = data["Most similar sentence"];
        const intent = data["Intent"];
        const cosineSimilarity = data["Cosine Similarity"];
        
        // Display the formatted data in the resultDiv
        resultDiv.innerHTML = "Most similar sentence: " + mostSimilarSentence + "<br>" +
                              "Intent: " + intent + "<br>" +
                              "Cosine Similarity: " + cosineSimilarity;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function extractPrompt() {
    const prompt = document.getElementById("prompt").value;

    fetch("/extract", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: prompt }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        const resultDiv = document.getElementById("result");
        const keywords = data["Keywords"];
        
        // Display the formatted data in the resultDiv
        resultDiv.innerHTML = "Keywords: " + keywords;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}