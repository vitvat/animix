document.addEventListener('DOMContentLoaded', function () {
    const fatherField = document.getElementById('id_father');
    const motherField = document.getElementById('id_mother');

    if (fatherField && motherField) {
        // Сначала делаем поле матери неактивным, если отец не выбран
        if (!fatherField.value) {
            motherField.disabled = true;
        }

        // Активируем поле матери и устанавливаем текущее значение, если отец уже выбран при редактировании записи
        if (fatherField.value && motherField.getAttribute('data-current-value')) {
            fetch(`/anymix/filter_mother_choices/?father_id=${fatherField.value}`)
                .then(response => response.json())
                .then(data => {
                    const options = data.mother_choices;
                    motherField.innerHTML = '';  // Очистить текущее содержимое
                    options.forEach(option => {
                        const opt = document.createElement('option');
                        opt.value = option.id;
                        opt.textContent = option.name;
                        motherField.appendChild(opt);
                    });
                    motherField.value = motherField.getAttribute('data-current-value');
                    motherField.disabled = false;  // Сделать поле матери активным
                });
        }

        fatherField.addEventListener('change', function () {
            if (fatherField.value) {
                fetch(`/anymix/filter_mother_choices/?father_id=${fatherField.value}`)
                    .then(response => response.json())
                    .then(data => {
                        const options = data.mother_choices;
                        motherField.innerHTML = '';  // Очистить текущее содержимое
                        options.forEach(option => {
                            const opt = document.createElement('option');
                            opt.value = option.id;
                            opt.textContent = option.name;
                            motherField.appendChild(opt);
                        });
                        motherField.disabled = false;  // Сделать поле матери активным
                    });
            } else {
                motherField.innerHTML = '';
                motherField.disabled = true;  // Оставить поле матери неактивным, если отец не выбран
            }
        });
    }
});
