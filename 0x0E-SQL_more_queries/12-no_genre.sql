-- list all shows in which genre is NULL
SELECT show.title, genre.genre_id
  FROM tv_shows AS show
  LEFT JOIN tv_show_genres AS genre
  ON show.id = genre.show_id
  WHERE genre.genre_id IS NULL
  ORDER BY s.title, g.genre.id;
