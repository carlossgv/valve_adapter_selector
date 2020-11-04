let brand_select = document.getElementById("brand");
let serie_select = document.getElementById("serie");
let size_select = document.getElementById("size");
let act_type_select = document.getElementById("act_type")
let act_size_select = document.getElementById("act_size")

brand_select.onchange = function () {
    brand = brand_select.value;

    fetch('/serie/' + brand).then(function (response) {

        response.json().then(function (data) {
            let optionHTML = '';

            for (let serie of data.series) {
                optionHTML += '<option value="' + serie + '">' + serie + '</option>';
            }

            serie_select.innerHTML = optionHTML;

        });
    });
}
serie_select.onchange = function () {
    brand = brand_select.value;
    serie = serie_select.value;

    fetch('/size/' + serie + '/' + brand).then(function (response) {

        response.json().then(function (data) {
            let optionHTML = '';

            for (let size of data.sizes) {
                optionHTML += '<option value="' + size + '">' + size + '</option>';
            }

            size_select.innerHTML = optionHTML;

        });
    });
}

act_type_select.onchange = function () {
    act_type = act_type_select.value;

    fetch('/act_size/' + act_type).then(function (response) {

        response.json().then(function (data) {
            let optionHTML = '';

            for (let act_size of data.act_sizes) {
                optionHTML += '<option value="' + act_size + '">' + act_size + '</option>';
            }

            act_size_select.innerHTML = optionHTML;

        });
    });

}