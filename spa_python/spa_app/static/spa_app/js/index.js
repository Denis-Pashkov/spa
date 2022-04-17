$(document).ready(function ($) {
    $(document).on('submit', '#form', function (e) {
        e.preventDefault();
        var serializedData = $(this).serialize();
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/',
            data: serializedData,
            success: function (json) {
                function reset_table() {
                    let body = document.getElementById('body');
                    let table = document.getElementById('table');

                    while (table.firstChild) {
                        table.removeChild(table.firstChild);
                    }

                    lst = ['DATE', 'NAME', 'AMOUNT', 'DISTANCE']

                    for (let index = 0; index < lst.length; index++) {
                        td_title = document.createElement('td');
                        td_title.setAttribute('class', 'title_table');
                        td_title.innerHTML = lst[index];
                        table.append(td_title);
                    }
                    body.append(table);
                }
                reset_table()
                // document.getElementById("form").reset();
                console.log(json)
                var instance = JSON.parse(json["success"]);
                let fields = ''
                for (let index = 0; index < instance.length; index++) {
                    fields = instance[index]["fields"];

                    if (fields["date"].indexOf('T') != -1) {
                        fields["date"] = fields["date"].slice(0, 10) + ' ' + fields["date"].slice(11, 19);
                    };

                    $("#table").append(

                        `<tr>
                        <td>${fields["date"]||""}</td>
                        <td>${fields["name"]||""}</td>
                        <td>${fields["amount"]||""}</td>
                        <td>${fields["distance"]||""}</td>
                        </tr>`

                    )
                }
            },
            error: function (response) {
                alert(response.responseJSON.errors);
            }
        });
    });
});