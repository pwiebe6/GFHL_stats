function sortTable(columnIndex) {
    const html_button = event.target.parentNode;
    const html_th = html_button.parentNode;
    const html_head = html_th.parentNode;
    const html_table = html_head.parentNode;
    const parentId = html_table.id;
    var table = document.getElementById(parentId);
    var rows = table.rows;
    var switching = true;

    while (switching) {
        switching = false;

        for (var i = 1; i < rows.length - 1; i++) {
            var shouldSwitch = false;
            var x = rows[i].getElementsByTagName("TD")[columnIndex];
            var y = rows[i + 1].getElementsByTagName("TD")[columnIndex];

            if (!isNaN(x.innerHTML)){
                if (Number(x.innerHTML) > Number(y.innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            }
            else{
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}