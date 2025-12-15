const BACKEND_URL = "http://127.0.0.1:8000";

function showSection(id){
    document.querySelectorAll(".page").forEach(page=>{
        page.style.display = "none";
    });
    document.getElementById(id).style.display = "block";
}

async function getWeather(){
    const city = document.getElementById("city").value.trim();
    const apiKey = localStorage.getItem("api_key");
    if(!apiKey){ alert("You must login!"); return; }
    if(!city){ alert("Enter city"); return; }

    try {
        const res = await fetch(`${BACKEND_URL}/api/weather`, {
            method:"POST",
            headers:{
                "Content-Type":"application/json",
                "api-key":apiKey
            },
            body: JSON.stringify({ city })
        });
        const data = await res.json();
        const card = document.getElementById("currentWeather");
        if(res.ok){
            card.innerHTML=`
                <h2>${data.city}</h2>
                <p><strong>Temp:</strong> ${data.temperature}°C</p>
                <p><strong>Condition:</strong> ${data.condition}</p>
            `;
        } else {
            card.innerHTML=`<p style="color:red;">Error: ${data.detail}</p>`;
        }
    } catch(e){ alert("Backend connect error");}
}

async function scrapeWeather(){
    const city = document.getElementById("city").value.trim();
    if(!city){ alert("Enter city"); return; }
    try {
        const res = await fetch(`${BACKEND_URL}/api/scrape/${city}`);
        const data = await res.json();
        document.getElementById("currentWeather").innerText = data.result;
    } catch(e){ alert("Error scraping"); }
}

function logout(){
    localStorage.removeItem("api_key");
    window.location.reload();
}

async function showHistory(){
    const city = document.getElementById("graphCity").value.trim();
    if(!city){ alert("Enter city"); return; }
    document.getElementById("historyImg").src = `${BACKEND_URL}/api/weather_graph/${encodeURIComponent(city)}`;
}
