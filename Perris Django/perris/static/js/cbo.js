$(document).ready(function()
{
    $("#cboRegion").change(function()
    {
        var codigo = $("#cboRegion").val();

       if(codigo =="")
            {
                $("#cboCiudad").prop("disabled",true);
                $("#cboCiudad").val("");
                return ;
            }

        $.get("region.php",{id:codigo}, function(respuesta)
        {
            $("#cboCiudad").html(respuesta)
            $("#cboCiudad").prop("disabled",false);

        });

    });
});