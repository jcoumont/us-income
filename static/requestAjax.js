analyse.on('click', 
  function(e){
    const url = '/analyse';
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
          response = xhr.response;
          response = JSON.parse(response)
    }
  });

  tuning.on('click', function(e){
    const url = '/tuning';
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      response = xhr.response;
      response = JSON.parse(response)
}
  });