const delcategory = function( reg, name ) {
    var msg = "¿Estas seguro que deseas eliminar la categoria " + name + "?";
    deleteRegistry( msg, reg );
}

const delsubcategory = function( reg, name ) {
    var msg = "¿Estas seguro que deseas eliminar la subcategoria " + name + "?";
    deleteRegistry( msg, reg );
}

const deleteRegistry = function( msg, reg ) {
    var confirmation = confirm( msg );
    if ( confirmation ) {
        document.getElementById( reg ).submit();
    }
    return confirmation;
}