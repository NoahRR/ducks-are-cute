// ON DOM LOAD
window.addEventListener('DOMContentLoaded',function(){
    
    // hide blob if on ipad
    const iPad = !!(navigator.userAgent.match(/(iPad)/)
    || (navigator.platform === "MacIntel" && typeof navigator.standalone !== "undefined"))

    if (iPad == true) {
        document.querySelector('#desktop-blob-main').style.display = 'none';
    }

},false);

// Counter Buttons
const counterEl = document.getElementById("counter");
const btn = document.getElementById("increment-btn");
const mobile_counterEl = document.getElementById("mobile-counter");
const mobile_btn = document.getElementById("mobile-increment-btn");
btn.addEventListener("click", async () => {
try {
    const resp = await fetch("/increment", {
        method: "POST",
        headers: { "Accept": "application/json" }
    });

    if (!resp.ok) {
        throw new Error(`Request failed: ${resp.status}`);
    }

    const data = await resp.json();
    counterEl.textContent = data.value;
    mobile_counterEl.textContent = data.value;

} catch (err) {
    console.error(err);}
});
mobile_btn.addEventListener("click", async () => {
try {
    const resp = await fetch("/increment", {
        method: "POST",
        headers: { "Accept": "application/json" }
    });

    if (!resp.ok) {
        throw new Error(`Request failed: ${resp.status}`);
    }

    const data = await resp.json();
    mobile_counterEl.textContent = data.value;
    counterEl.textContent = data.value;

} catch (err) {
    console.error(err);}
});