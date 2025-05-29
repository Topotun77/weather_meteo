// Массив городов получаем с помощью AJAX-запроса к базе данных городов)

fetch('/api/stat_api_app/get-cities/')
    .then(response => {
        if (!response.ok) throw new Error(`HTTP ошибка! Статус: ${response.status}`);
        return response.json();
    })
    .then(data => {
        console.log(data); // data теперь содержит массив городов
        processCities(data);
    })
    .catch(error => {
        console.error('Ошибка:', error.message);
    });

// Функция для последующей обработки полученного массива городов
function processCities(cities) {
    document.getElementById("id_city").addEventListener("input", function() {
        let inputValue = this.value.trim();
        if (!inputValue) {
            // Если поле пустое, скрываем подсказки
            document.getElementById("citySuggestions").innerHTML = "";
            return;
        }
        // Фильтруем города по совпадению начала названия
        let filteredCities = cities.filter(city => city.toLowerCase().startsWith(inputValue.toLowerCase()));

        // Если нашли хотя бы один город, показываем подсказки
        if (filteredCities.length > 0) {
            let suggestionsList = document.getElementById("citySuggestions");

            // Формируем элементы списка с подсказками
            suggestionsList.innerHTML = '';
            filteredCities.forEach(function(city) {
                let suggestionItem = document.createElement("li");
                suggestionItem.className = "city-suggestion";
                suggestionItem.textContent = city;

                // По клику вставляем выбранное значение в поле ввода
                suggestionItem.addEventListener("click", () => {
                    document.getElementById("id_city").value = city;
                    suggestionsList.innerHTML = ''; // Скрыть подсказки после выбора
                });

                suggestionsList.appendChild(suggestionItem);
            });
        } else {
            document.getElementById("citySuggestions").innerHTML = ""; // Нет совпадений
        }
    });
};
