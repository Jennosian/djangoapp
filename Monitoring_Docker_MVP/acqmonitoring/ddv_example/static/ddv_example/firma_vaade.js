
$(document).ready(function()  {
    var dt_table =
    $('#tbl_firma').dataTable({
        language: dt_language,  // global variable defined in html
        order: [[ 0, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs: [
            {orderable: true,
             searchable: true,
             className: "left",
             targets: [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
            },
            {
                data: 'random_name ',
                targets: [0]
            },
            {
                data: 'random_amount ',
                targets: [1]
            },
            {
                data: 'date ',
                targets: [1]
            },
            {
                data: 'type',
                targets: [2]
            },
            {
                data: 'random_id_code',
                targets: [9]
            }
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: FIRMA_JSON_URL
    });
});


