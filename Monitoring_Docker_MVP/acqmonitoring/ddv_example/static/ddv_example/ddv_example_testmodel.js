
$(document).ready(function() {
    var dt_table = $('#tbl_koond').dataTable({

        language: dt_language,  // global variable defined in html
        aaSorting: [[ 5, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs: [
            {orderable: true,
             searchable: true,
             className: "left",
             targets: [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11]
            },
            {
                data: 'year',
                targets: [0]
            },
            {
                data: 'month',
                targets: [1]
            },
            {   data: 'random_id_code',
                targets:[2],
                render: function ( data, type, row, meta ) {
                    if(type === 'display'){
                        data = '<a href="http://127.0.0.1:8000/firma/' + encodeURIComponent(data) + '">' + data + '</a>';
                    }

                    return data;
            }
            },
            {
                data: 'type',
                targets: [3]
            },
            {
                data: 'random_name',
                targets: [4]
            },
            {
                data: 'random_amount',
                targets: [5]
            },
            {
                data: 'random_count',
                targets: [6],
                    render(data){
                        return Number(data).toFixed(0) }
            },
            {
                data: 'random_percent',
                targets: [7],
                    render(data){
                        return Number(data).toFixed(0) }

            },
            {
                data: 'rule_1',
                targets: [8],
                    render(data){
                        return Number(data).toFixed(0) }

            },
            {
                data: 'rule_2',
                targets: [9],
                    render(data){
                        return Number(data).toFixed(0) }
            },
            {
                data: 'rule_3',
                targets: [10],
                    render(data){
                        return Number(data).toFixed(0) }

            },
            {   data: 'rule_4',
                targets: [11],
                render(data){
                        return Number(data).toFixed(0) }

            }
        ],

        rowCallback: function (row, data, index) {
                if (Number(data.rule_1).toFixed(0) > 99.5) {
                    $("td:eq(8)", row).css('background-color','#ff9b71')
            }
                if (Number(data.rule_2).toFixed(0) > 99.5) {
                    $("td:eq(9)", row).css('background-color','#ff9b71')
            }
                if (Number(data.rule_3).toFixed(0) > 99.5) {
                    $("td:eq(10)", row).css('background-color','#ff9b71')
            }
                if (Number(data.rule_4).toFixed(0) > 99.5) {
                    $("td:eq(11)", row).css('background-color','#ff413c')
                    console.log(Number(data.rule_4))
            }
        },


        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: TESTMODEL_LIST_JSON_URL



    });

} );



