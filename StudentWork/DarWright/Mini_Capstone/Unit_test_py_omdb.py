from Mini_Capstone.py_omdb import Search

def test_init():
    search = Search()
    assert(search.imdb_id == '?i=')  # A valid IMDb ID (e.g. tt1285016)
    assert(search.title == '?t=')  # Movie title to search for.
    assert(search.s_type== '&type=movie')  # movie, series, episode	Type of result to return.
    assert(search.year == '&y=')  # Year of release.
    assert(search.response_type == '&r=json')
    assert(search.plot == '&plot=short')
    assert(search.tomatoes == '&tomatoes=true')
    assert(search.url == 'http://www.omdbapi.com/')
    assert(search.response_list == ['Title', 'Plot', 'Actors', 'Year'])
# test_init()

def test_movie():
    search = Search()
    search.movie('Mad+Max')
    assert(search.title == '?t=Mad+Max')
    assert(search.url == 'http://www.omdbapi.com/?t=Mad+Max&y=&plot=short&tomatoes=true')
# test_movie()

def test_imdbid():
    search = Search()
    search.imdbid('tt0079501')
    assert(search.imdb_id == '?i=tt0079501')
    assert (search.url == 'http://www.omdbapi.com/?i=tt0079501&tomatoes=true')
# test_imdbid()

def test_episode():
    search = Search()
    search.episode('Game+of+Thrones', '2', '1')
    assert(search.title == '?t=Game+of+Thrones&Season=2&Episode=1')
    assert(search.url == 'http://www.omdbapi.com/?t=Game+of+Thrones&Season=2&Episode=1&y=&plot=short&tomatoes=true')
test_episode()
# http://www.omdbapi.com/?t=Game+of+Thrones&Season=2&Episode=1&y=&plot=short&tomatoes=true

    
    
    
    
        
