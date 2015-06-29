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
test_init()

def test_movie():
    search = Search()
    search.movie('Mad+Max')
    assert(search.title == '?t=Mad+Max')
    print search.url
    # http://www.omdbapi.com/?t=Mad+Max&y=&plot=short&tomatoes=true
    # Why does this not match?!
    assert(search.url == 'http://www.omdbapi.com/?t=Mad+Max&plot=short&tomatoes=true')
test_movie()

def test_imdbid():
    search = Search()
    search.imdbid('tt0079501')
    assert(search.imdb_id == '?i=tt0079501')
    assert (search.url == 'http://www.omdbapi.com/?i=tt2178782&tomatoes=true')
# test_imdbid()


    
    
    
    
        
