function delete_wish(id) {http://localhost:5000/userhome
  if(confirm("Are you sure you want to delete the wish"))
  {
    location.href = '/deletewish/'+id;
  }}

