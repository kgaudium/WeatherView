function getPageName() {
            const url = window.location.href;
            return url.substring(url.lastIndexOf('/') + 1);
        }

async function getUserIP() {
    try {
        const response = await fetch('https://api.ipify.org?format=json');
        const data = await response.json();
        console.log('IP address:', data.ip);
        return data.ip;
    } catch (error) {
        console.error('Could not fetch IP address:', error);
        return null;
    }
}

async function doRequest(url, data){
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

async function getWeatherByIP() {
    const data = {
        ip: await getUserIP()
    };

    return await doRequest('/get-weather-by-ip', data)

    // try {
    //     const response = await fetch(, {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         },
    //         body: JSON.stringify(data)
    //     });
    //
    //     return await response.json();
    // } catch (error) {
    //     console.error('Error:', error);
    //     throw error;
    // }
}

async function getWeatherByName(name){
    const data = {
        name: name
    };

    return await doRequest('/get-weather-by-name', data)
}

async function performSearch(elem) {
    if (event.key !== 'Enter') {
        return;
    }

    let searchValue = elem.value;
    const weather_data = await getWeatherByName(searchValue);
    console.log(`Weather data for search query ${searchValue}:`);
    console.log(weather_data)
    await setWeather(weather_data);
}

async function getIconUrl(filename){
    const data = {
        filename: filename
    };

    try {
        const response = await fetch('/get-icon-filename', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

async function setWeather(weather_data) {
    document.getElementById("name").textContent = weather_data["name"];
    document.getElementById("real-temp").textContent = weather_data["temp"];
    document.getElementById("feels-like-temp").textContent = weather_data["feels"];
    document.getElementById("icon").src = await getIconUrl(weather_data["icon_name"]);
    document.getElementById("description").textContent = weather_data["desc"];
    document.getElementById("date").textContent = weather_data["date"];
    document.getElementById("wind-speed").textContent = weather_data["wind_speed"];
    document.getElementById("wind-scale8").textContent = weather_data["wind_scale8"];
    document.getElementById("wind-arrow").style.rotate = weather_data["wind_degrees"] + "deg";
    document.getElementById("pressure").textContent = weather_data["pressure"];
    document.getElementById("humidity").textContent = weather_data["humidity"];
    // document.getElementById("gm-intensity").textContent = weather_data["gm"];
    document.getElementById("water").textContent = weather_data["water"];

}

async function setWeatherOnLoad() {
    let pageNmae = getPageName();
    if (pageNmae === "index" || pageNmae === ""){
        const weather_data = await getWeatherByIP();
        console.log(weather_data)
        await setWeather(weather_data)
    }

}


window.onload = function () {
    setWeatherOnLoad()
}
