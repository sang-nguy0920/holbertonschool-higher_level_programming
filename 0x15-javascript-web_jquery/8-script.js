$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, value) {
    $('#list_movies').append(value.title);
  });
});
