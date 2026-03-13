function scan(){

let text=document.body.innerText;

fetch("http://127.0.0.1:8000/check_message?message="+encodeURIComponent(text))
.then(res=>res.json())
.then(data=>{

if(data.risk==="High Risk Message"){

alert("⚠ Binance P2P Guardian: Scam message detected");

}

});

}

setInterval(scan,5000);