-- select with left join all that not matching
-- https://stackoverflow.com/questions/4076098/how-to-select-rows-with-no-matching-entry-in-another-table
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id=tv_shows.id WHERE tv_show_genres.show_id IS NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
