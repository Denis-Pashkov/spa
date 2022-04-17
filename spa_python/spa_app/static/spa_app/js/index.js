function add_active() {
    // 
    // Функция для выделения подпункта меню для текущей страницы.
    // 
    let url_path = document.location.href;
    url_path = url_path.split('/');
    let list_items = ['ourteam', 'photo', 'reviews', 'video', 'aragats', 'ararat', 'elbrus', 'kazbek', 'kilimanjaro', 'lenin_peak', 'manaslu', 'monblan', 'peak_separate', 'arcticles', 'clothes_and_equuipment', 'phisical_training', 'question_answer', 'treaties', 'arround_annapurna', 'lician_path']
    let current_item = url_path[url_path.length - 1];

    function check_in_list(current_item, list_items) {
        for (let i = 0; i < list_items.length; i++) {
            if (current_item == list_items[i]) {
                return (true);
            }
        }
    }

    function setItemAttribute(current_item, list_items) {
        if (check_in_list(current_item, list_items)) {
            item = document.getElementById(current_item);
            item.classList.add('active');
        }
    }
    setItemAttribute(current_item, list_items);
}

add_active();


function align_right() {

    const mediaQuery = window.matchMedia('(max-width: 767px)')

    if (mediaQuery.matches) {
        // alert('Media Query Matched!')
        let bw = document.getElementById('bw');
        bw.classList.remove('justify-content-center');
        bw.classList.add('justify-content-start');
    }
    // let bw = document.getElementById('bw');
    // bw
    // .d-flex.justify-content-center.my-brand{

}

align_right();

function hidden_body(burger) {
    a = burger.classList[1];
    let body = document.getElementById('body');
    // let body = document.getElementsByTagName('body');

    if (a != 'collapsed') {
        body.style.overflow = 'hidden';
    } else {
        body.style.overflow = 'visible';
    }
}

// hidden_body();

// <!DOCTYPE html>
// <html>
//     <head>
//         <title>Single Page</title>
//         <script>

//             //  This function communicates with django (backend)

//             function showSection(section) {   
//                 fetch(`/sections/${section}`)
//                 .then(response => response.text())
//                 .then(text => {
//                     console.log(text);
//                     document.querySelector('#content').innerHTML = text;
//                 });

//             }


//             document.addEventListener("DOMContentLoaded", function() {
//                 document.querySelectorAll('button').forEach(button => {
//                     button.onclick = function() {
//                         showSection(this.dataset.section)
//                     }
//                 })
//             });


//         </script>
//     </head>
//     <body>
//         <h1>Hello</h1>
//         <button data-section="1">Section 1</button>
//         <button data-section="2">Section 2</button>
//         <button data-section="3">Section 3</button>

//         <!-- Contents loaded from server is inserted here by javascript -->
//         <div id="content">

//         </div>

//     </body>
// </html>

function ajax_1() {
    variable1 = new XMLHttpRequest();

    xhttp.onload = function () {
        // What to do when the response is ready
        table = document.getElementById("table");
        document.getElementById("body").removeChild(table);
    }
    xhttp.open("GET", "ajax_info.txt");
    xhttp.send();
}

function update_table() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            table = document.getElementById("table");
            document.getElementById("body").removeChild(table);
        }
    };
    xhttp.open("GET", "ajax_info.txt", true);
    xhttp.send();
}

$(document).ready(function ($) { //когда страница прогрузилась
    $(document).on('submit', '#form', function (e) {
        e.preventDefault();
        var serializedData = $(this).serialize();
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/',
            // data: {
            //     title: 1,
            //     description: 2,
            //     csrfmiddlewaretoken: 2,
            //     action: 3
            // },
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
                        // console.log(lst[index]);
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
                // var fields = instance[0]["fields"];
                // prepend
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



// function loadDoc() {
//     const xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//       if (this.readyState == 4 && this.status == 200) {
//         document.getElementById("demo").innerHTML =
//         this.responseText;
//       }
//     };
//     xhttp.open("GET", "ajax_info.txt");
//     xhttp.send();
//   }