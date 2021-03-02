-- select with left join all tv show with genre and tv show with not
-- https://explainextended.com/2009/09/15/not-in-vs-not-exists-vs-left-join-is-null-sql-server/
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id=tv_shows.id ORDER BY tv_shows.title, tv_show_genres.genre_id;
