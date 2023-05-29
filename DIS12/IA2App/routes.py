from flask import request, redirect, url_for, flash, session, render_template #Grabbing things I need in order to use flask well, and pull things to and from html and users
from DIS12.IA2App import app #Just to import things such as Secret Key and make it work
from DIS12.IA2App.forms import LoginForm, RegisterForm, SearchForm, FaveForm, FriendForm, EventForm, DjForm, RTypeForm, SearchDjForm, HistoryForm # All the diffeernt forms I used in order to do that effectively
from DIS12.IA2App.apifunctions import search_albums, search_track, search_artist, search_track_id, save_albums_to_db, dictionary_into_db #Grab all of the functions to call from the AudioDB Api
import sqlite3, json #Grab Sqlite so we can interact with the  database
from werkzeug.security import generate_password_hash, check_password_hash #Encrypting to make sure users passwords are safe!
from datetime import date, datetime #Dates in order to do Date of birthds

def db_connect(): #Connecting to the database, just makes it a little cleaner.
    connection = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA2App\ndjdatabase.db ')
    return connection

@app.route("/home", methods=['GET', 'POST']) #The Index Page, currently nothing.
def index():
    # session['type'] = None #Used to just be testing for the website functions, before I created the songs page for full.
    # form = SearchForm()
    # fave = FaveForm()
    # do = ['None']
    # if form.validate_on_submit():
    #     data = search_albums(form.album.data)
    #     if fave.validate_on_submit():
    #         do = fave.favourite.data
    # else:
    #     data = ['None']

    # return "<h1>Hello Everyone!!</h>"
    return render_template("index.html", login=False, index=True) #Returning render template, and sending activity.
@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST']) #Routes to get to the login page, which is the index, and login
def login(): #Open the login page
    form = LoginForm() #Get the Form from the routes page, using WTForms!
    if form.validate_on_submit(): #If the user inputs and everything goes through safely
        if form.dj.data == 0: #If they are not a DJ
            email = form.email.data
            password = form.password.data   #Grab all the data I need
            conn = db_connect()
            users = conn.execute("SELECT password, user_id, first_name FROM users WHERE email = ?", (email,)).fetchone() #SQL Query to get the password, user_id and name from users
            conn.commit()
            conn.close()
            try: #Try incase of error
                if check_password_hash(users[0],password): #Checking password with Security encryption
                    flash("You have successfully logged in! Good work.","success") #User feedback to show they did well
                    session['user'] = users[1]
                    session['username'] = users[2] #Get some session variables to allow further functions.
                    return redirect("/index")
                else:
                    flash(f"Sorry, there was an error.", "danger") #More user feedback for safety
            except:
                flash(f"Sorry, there was an error.", "danger") #More user feedback for safety again
        else: #This is for Djs this time
            email = form.email.data
            password = form.password.data #Get the data
            conn = db_connect()
            users = conn.execute("SELECT password, dj_id, name FROM djs WHERE email = ?", (email,)).fetchone() #Get the DJ password, Id and name for lter
            conn.commit()
            conn.close()
            try: #In case of error
                if check_password_hash(users[0],password): #check their passwords with the security functions
                    flash("You have successfully logged in! Good work.","success")  #User feedback!
                    session['dj'] = users[1]
                    session['djname'] = users[2] #Put some session variables for later
                    return redirect("/index")
                else:
                    flash(f"Sorry, there was an error.", "danger") #More user feedback in case of error
            except Exception as e:
                flash(f"Sorry, there was an error.{e}", "danger") #User feedback in cae of error, with e for testing purposes

    return render_template("login.html", form=form, login=True) #return template and have login =True for active nav
@app.route("/register", methods=['GET', 'POST']) #REgister!
def register():#Begin Register Function
    # Rform = RTypeForm()
    # type = "role"
    # if session.get('type'):
    #     if session['type'] == "register":
    #         type = "register"
    #         form = RegisterForm()
    #     if session['type'] == "dj":
    #         type = "dj"
    #         form = DjForm()
    # if session['type'] == "register":
    #     if form.validate_on_submit():
    type = "none" #A type to help with dj or user register
    form = RTypeForm() #Setting the forms here to make check for the Type
    form2 = RTypeForm()
    if form.validate_on_submit(): #If its submitted the first time
        if form.dj.data: #if the user selected dj
            form2 = DjForm() #The form is DJform
            type = "dj" #Set the type to DJ
        if form.register.data: #if they selected user
            form2 = RegisterForm() #the form is instead the regsiter form
            type = "register" #Register
    if form2.validate_on_submit(): #If the second form goes through
        try:
            form2 = DjForm() # check if they picked DJ the first time
            if form2.age.data: #if so, go to the next
                raise Exception("Go to DJ form")

            form2 = RegisterForm()
            email = form2.email.data
            password = form2.password.data
            password = generate_password_hash(password,"sha256") #Collect data from form, and encrypt the password
            first_name = form2.first_name.data
            last_name = form2.last_name.data
            dob = form2.dob.data
            try: #Try to put it into the database
                conn = db_connect()
                conn.execute("INSERT INTO users (first_name, last_name, email, password, dob) VALUES (?,?,?,?,?)", #In put the data into the database
                    (first_name, last_name, email, password, dob)
                        )
                conn.commit()
                conn.close()
                flash(f"{first_name[0:len(first_name)]}, the registration was successful", "success")
            except sqlite3.IntegrityError as e: #If this doesnt work, due to an intgrity error (which will be the email being the same)
                flash(f"Sorry, this email is already in use!{e}", 'warning')
            # session['type'] = None
            return redirect("/index")
        except Exception as e: #If they used the DJ form instead
            form2 = DjForm()
            name = form2.name.data
            email = form2.email.data
            genre = form2.genre.data
            age = form2.age.data        #Collect all the data from the form
            description = form2.description.data
            price = form2.price.data
            password = form2.password.data
            password = generate_password_hash(password,"sha256") #Encrypt the password
            try:
                conn = db_connect()
                conn.execute("INSERT INTO djs (name, email, genre, age, description, price, password) VALUES (?,?,?,?,?,?,?)", #Insert all of th eimportant data into the DJ table and get that working
                             (name, email, genre, age, description, price, password))
                conn.commit()
                conn.close()
                flash(f"{name}, the registration was successful", "success") #send some good user feedback
            except Exception as e:
                flash(f"{e}", 'warning') #send bad user feedback
                # session['type'] = None
            return redirect("/login")

            # return("<h1>DJJJJJJ</h1>")
    # if form.validate_on_submit():
    #     return f"<h1>{form.dj.data}</h1>"
    #     if form.dj.data:
    #         form = DjForm()
    #         type = "dj"
    #         session['type'] = "dj"
    #         return f"<h1>{type}</h1>"
    #     else:
    #         form = RegisterForm()
    #         type = "register"
    #         session['type'] = "register"
    return render_template("register.html", login=False, register=True, form=form, type=type, form2=form2) #Rendering all of the differnt forms and variables
@app.route("/friends", methods=['GET', 'POST'])
def friends(friendslist = None): #Friends! Friendslist = None
    form = FriendForm() #Friend Form
    if session.get('user'): # If the user is detected
        conn = db_connect()
        friendslist = conn.execute("SELECT * FROM users AS u INNER JOIN friend AS f ON u.user_id = f.user_id_2 WHERE f.user_id_1 = ?", (session['user'],)).fetchall() #Get all the friends that user has
        conn.commit()
        conn.close()
        if form.validate_on_submit(): #If they want to add a new friend
            try: #attempt to
                friendId = form.friendId.data #collect data
                conn = db_connect()
                conn.execute("INSERT INTO friend (user_id_1, user_id_2) VALUES (?,?)", #Insert the values inoto friends table
                    (session['user'], friendId)
                        )
                conn.commit()
                conn.close()
                flash("You are now friends!", "success") #make them friends
            except sqlite3.IntegrityError:
                flash("Sorry, you are already friends!", "danger")#Incase they are already friends

    return render_template("friends.html", friends=True, form=form, friendslist=friendslist) #Export the friends list and form
@app.route("/songs", methods=['GET', 'POST'])
def songs(data=None, artist=None): #Song searching
    fave = FaveForm()
    form = SearchForm()
    favourites = []#Set all the variabels and the forms
    faves = []
    songlist = []
    artistlist=[]
    debuglist = []
    # if session['user']:
    #     conn = db_connect()
    #     song_list = conn.execute("SELECT song_id FROM songs_fave WHERE user_id = ?",
    #                              (25714,)).fetchall()
    #     conn.close()
    #     for song in song_list:
    #         faves.append((search_track(song)))
    if form.validate_on_submit():# if the user searches
        if form.category.data == "Album" or form.category.data == "Track": #If they want tracks or albums
            try:
                conn = db_connect()
                data = conn.execute("SELECT strAlbum, intYearReleased, strAlbumThumb, idAlbum FROM albums WHERE strArtist LIKE ?", (form.album.data,)).fetchall() #Try to get data form the DB, but if that doesnt work
                conn.commit()
                conn.close()
                if data == []:
                    raise Exception("No Data in database") #say theres no data
            except:
                data = search_albums(form.album.data) #Search through the album database instead
                if data != None: #Here just to get the data out of the search function
                    for dictionary in data:
                        try:
                            dictionary_into_db(dictionary, 'albums') #Put the dictionaries into the SQL database
                        except:
                            continue #In case of errors, or its already in there, continue incase there is new albums or smth
                    conn = db_connect()
                    data = conn.execute("SELECT strAlbum, intYearReleased, strAlbumThumb, idAlbum FROM albums WHERE strArtist LIKE ?", (form.album.data,)).fetchall() #Get the data back out of the database.
                    conn.commit()
                    conn.close() #This is done again to make sure that the data given to the html is the same as above
                # save_albums_to_db(data['strArtist'], data['idAlbum'], ")
            if form.category.data == "Track": #If they wanted tracsk
                try:
                    conn = db_connect()
                    songlist = conn.execute("SELECT t.strTrack, t.strAlbum, t.idTrack, t.intDuration, a.idAlbum, a.intYearReleased FROM songs as t INNER JOIN albums AS a ON t.idAlbum = a.idAlbum WHERE a.strArtist LIKE ?", (form.album.data,)).fetchall() #Get all the Track information from the artist in the database
                    conn.commit()
                    conn.close()
                    if songlist == []:
                        raise Exception("No Data in database") #If theres no data, raise error
                except Exception as e: #If error
                    for song in data:
                        if song != None:
                            faves.append(search_track(song[3])) #Get the data from the API
                    for tracks in faves:
                        if tracks != None: #Processing the Data
                            for track in tracks:
                                try:
                                    dictionary_into_db(track, 'songs') #Put the data into the SQL Database
                                    information = [track['strTrack'], track['strAlbum'], track['idTrack'], track['intDuration']]
                                    songlist.append(information)
                                except:
                                    continue #Continue incase some songs are already in the database/errors occur
                data = None
        else: #
            try: #Try
                conn = db_connect()
                artists = conn.execute("SELECT strArtist, strArtistThumb, strArtistBanner, strArtistLogo, strBiographyEN, idArtist FROM artists WHERE strArtist LIKE ?", (form.album.data,)).fetchall() #Grab all the artist details if they exist
                conn.commit()
                conn.close()
                if artists == []: #If there were no artists
                    raise Exception("No Data in database") #Raise error and go to except instead
            except: #Except if no data is found in database
                artists = search_artist(form.album.data, 'name') #Search with the API instead
                for artist in artists['artists']: #Processing the data
                    try:
                        dictionary_into_db(artist, 'artists') #Put it into the database
                    except:
                        continue #Continue in case of errors
                conn = db_connect()
                artists = conn.execute("SELECT strArtist, strArtistThumb, strArtistBanner, strArtistLogo, strBiographyEN, idArtist FROM artists WHERE strArtist LIKE ?", (form.album.data,)).fetchall() #Select The data from the database to keep the data same values.
                conn.commit()
                conn.close()

                data = None #Remove data and songlist so albums and tracks dont show up
                songlist = []

            for artist in artists: #put all the artists into a list
                artistlist.append(artist)

            # artist

    elif session.get('user'):
        if session.get('friend'): #If you are looking through the friend function
            id = session['friend']
            session['friend'] = None #Reset the function
        else:
            id = session['user'] #Just user id for the id
        conn = db_connect()
        favourites = conn.execute("SELECT strTrack, strAlbum, idTrack, strArtist FROM songs AS s INNER JOIN songs_fave AS f ON s.idTrack = f.song_id WHERE f.user_id = ?", (id,)).fetchall() #If your are looking for friends, use their id instead,ohterwise user id favourites
        conn.commit()
        conn.close()
        data = None#Reset data

    return render_template("songs.html", login=False, songs=True, form=form, fave=fave, data=data, favourites=favourites, songlist=songlist, artistlist=artistlist) #return everything, faves if no search,
@app.route('/<int:id>/favourite/')
def favourite_song(id): #Favourite song with the link, giving in
    if id is None:
        flash('No Song ID Found')
        return redirect(url_for('songs'))
    try:
        conn = db_connect()
        conn.execute("INSERT INTO songs_fave (user_id, song_id) VALUES (?,?)", #Insert the song id and the user id into the songs_fave table
                (session['user'], id)
                    )
        conn.commit()
        conn.close()

    except sqlite3.IntegrityError:
        flash("This song is already favourited!", "warning") #User feedback!
    return redirect(url_for('songs'))
@app.route('/<int:id>/unfavourite/') #Unfavourite Songs
def remove_favourite_song(id): #sent through ID
    if id is None:
        flash('No Song ID Found')
        return redirect(url_for('songs'))
    conn = db_connect()
    conn.execute("DELETE FROM songs_fave WHERE user_id = ? AND song_id = ?", #delete from the tables from songs_fave where the user_id and song_id is existence
            (session['user'], id)
                )
    conn.commit()
    conn.close()
    return redirect(url_for('songs'))
@app.route('/create', methods=["GET", "POST"]) #Create new events
def create_event():
    form = EventForm() #Event form to get event data
    if form.validate_on_submit(): #if the form submits (There are errors)
        location = form.location.data
        private = form.private.data
        details = form.details.data #collect all the event data
        dj = form.dj.data
        date = form.date.data
        end_time = f"{form.end_time.data}"
        start_time = f"{form.start_time.data}"
        conn = db_connect()
        conn.execute("INSERT INTO events (location, private, details, date, start_time, end_time, host) VALUES (?,?,?,?,?,?,?)", #Insert the values into the events table
                (location, private, details, date, start_time, end_time, session['user']) #Here are the data values
                    )
        conn.commit()
        conn.close()
        flash(f"Event Created Succesfully!", "success") #More user feedback
    return render_template("create.html", create_event=True, form=form, create=True) #User feedback by active nav bar
@app.route("/hosting", methods=["GET", 'POST']) #Which DJS you are hosting
def host():
    events = None
    eventlist = [] #Set some variables
    if session['user']: #If someone is logged in
        conn = db_connect()
        events = conn.execute("SELECT location, details, dj, date, start_time, end_time, private, event_id FROM events WHERE host = ? ", (session['user'],)).fetchall() # Select all the important details from the events tab where its hosted by logged in user
        conn.commit()
        conn.close()
        for event in events: #Processing the data
            if event[2] != None:
                event = list(event)
                conn = db_connect() #Get the Dj name for each event and put it into the event
                event[2] = (conn.execute("SELECT d.name FROM events AS e INNER JOIN djs as d ON d.dj_id=e.dj WHERE e.event_id = ?", (f"{event[7]}",)).fetchall())[0][0] #
                # return(F"{event[2][0]}")
                conn.commit()
                conn.close()
            eventlist.append(event) #Processing data so it can be listed out
        # return f"{events, session['user']}"
    return render_template("host.html", events=eventlist, host=True)
@app.route("/<id>/artist", methods=['GET', 'POST']) #Getting the artist data with an ID from clicking on their image
def artist(id):
    conn = db_connect()
    artists = conn.execute("SELECT strArtist, strArtistThumb, strArtistBanner, strArtistLogo, strBiographyEN FROM artists WHERE idArtist LIKE ?", (f"{id}",)).fetchall() #Collect the artist data
    conn.commit()
    conn.close()
    return render_template("artist.html", artists=artists[0]) #Return the artist details for the artist
@app.route("/favourites", methods=['GET', 'POST'])
def favourites(): #Favourite page for songs. Now OBSOLETE
    songlist = []
    conn = db_connect()
    songs = conn.execute("SELECT song_id FROM songs_fave WHERE user_id = ? ", (session['user'],)).fetchall() #OBSOLETE
    conn.commit()
    conn.close()
    for id in songs:
        song = search_track_id(id[0]) #OBSOLETE
        songlist.append(song)

    return render_template("favourite.html", songlist=songlist)
@app.route("/joined", methods=['GET','POST']) #Events that you have joined
def joined():
    eventlist = None
    if session.get('user'): #If there is a session['user']
        conn = db_connect()
        eventlist = conn.execute("SELECT * FROM events AS e INNER JOIN eventuser AS u ON u.event_id = e.event_id WHERE u.user_id = ?", (session['user'],)).fetchall() #Fetch the events that you are part of events_user
        conn.commit()
        conn.close()
    return render_template("joined.html", eventlist=eventlist, joined=True) #Render the page with active
@app.route("/events", methods=['GET','POST']) #Events that are public essentially
def events():
    oldeventlist = None #set Variables
    if session.get('friend'): #If you are looking at friends
        conn = db_connect()
        eventlist = conn.execute("SELECT * FROM events as e INNER JOIN users AS u ON e.host = u.user_id INNER JOIN eventuser AS f ON e.event_id=f.event_id  WHERE private = 0 AND f.user_id= ?", (session['friend'],)).fetchall() #Find their public events that they are part of
        conn.commit()
        conn.close()
        session['friend'] = None #reset this sesssion
    elif session.get('djname'): #If you are a dj looking for which events you are part of
        conn = db_connect()
        eventlist = conn.execute("SELECT * FROM events as e INNER JOIN users AS u ON e.host=u.user_id INNER JOIN  djs AS d ON e.dj = d.dj_id WHERE e.dj = ? AND date >= ?", (session['dj'],date.today())).fetchall() #Select all the events that the DJ is part  where the date after today
        conn.commit()
        conn.close()
        # session[''] = None
        conn = db_connect()
        oldeventlist = conn.execute("SELECT * FROM events as e INNER JOIN users AS u ON e.host=u.user_id INNER JOIN  djs AS d ON e.dj = d.dj_id  WHERE e.dj = ? AND date < ?", (session['dj'],date.today())).fetchall() #Also select all the previous events DJ was part of (Event before today)
        conn.commit()
        conn.close()
        # session['friend'] = None
    else: #if they arent a friend or DJ
        conn = db_connect()
        eventlist = conn.execute("SELECT * FROM events as e INNER JOIN users AS u ON e.host = u.user_id WHERE private = 0 GROUP BY e.event_id").fetchall() #Select just the basic information of events that arent private
        conn.commit()
        conn.close()
    return render_template("events.html", eventlist=eventlist, event=True, oldeventlist=oldeventlist) #Send all this info through
@app.route("/eventsongs/", methods=['GET','POST']) #Songs for the even ts
def eventsongs(events=None):
    songlist = []
    if session.get('event'): #if there has been an event
        events = session['event'] #Set the event id to the session variable
        conn = db_connect()
        songlist = conn.execute("SELECT t.strTrack, t.strAlbum, t.strArtist, e.location, e.date, count(*) FROM songs AS t INNER JOIN songs_list AS s ON t.idTrack = s.song_id INNER JOIN events AS e ON s.event_id = e.event_id WHERE s.event_id = ? GROUP BY t.idTrack", (events[0])).fetchall() #Grab all the songs and their names nad info from the SQL database where the eventid is what was brought through
        conn.commit()
        conn.close()
    return render_template("eventsongs.html", events=events, joined=True, songlist=songlist) #Return event active nav and the songlist
@app.route('/<id>/eventdata/') #Grab an ID from the page that sent this
def open_event(id): #The point of this is to get an event id and then go to songs so you can add them to the even t
    if id is None:
        flash('No Event Found') #User info incase the user tries to go here
        return redirect(url_for('events')) #Go back to events page
    else:
        session['event'] = id #Set the id to session['event'}
    return redirect(url_for('songs')) #Redirect to songs
@app.route('/<id>/addtoevent/') #Add to event with the id given
def addtoevent(id): #Point of this function is to add a song to the event
    if id is None:
        flash('No Song ID Found') #User info incase the user tries to go here
        return redirect(url_for('eventsongs')) #If there is no id, return user info
    try:
        conn = db_connect()
        conn.execute("INSERT INTO songs_list (event_id, song_id, user_id) VALUES (?,?,?)", #If it works, put these songs into the songs_list for the dj
                (session['event'], id, session['user'])
                     )
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError: #in case they have already voted
        flash('You have already voted for this song!', 'danger') #Give some user feedback and redirect back to eventsongs
    return redirect(url_for('eventsongs'))
@app.route('/<id>/eventqueue/') #go the event songs with specific event
def select_event(id): #Select Events with the id and go back to eventsongs
    if id is None:
        flash('No Event Found')
        return redirect(url_for('events'))
    else:
        session['event'] = id
        return redirect(url_for('eventsongs'))
@app.route('/bookdj', methods=['GET','POST'])
def djs(): #Get DJ INformation
    form = SearchDjForm()
    conn = db_connect()# set Variables
    djs = conn.execute("SELECT * FROM djs").fetchall() #normally just select all DJs
    conn.commit()
    conn.close()
    if form.validate_on_submit():#If they do a search though
        if form.genre.data and form.name.data:
            conn = db_connect()
            djs = conn.execute("SELECT * FROM djs WHERE genre LIKE ? AND name LIKE ?", (form.genre.data, form.name.data)).fetchall() #If they search for both, check both
            conn.commit()
            conn.close()
        elif form.genre.data:
            conn = db_connect()
            djs = conn.execute("SELECT * FROM djs WHERE genre LIKE ? ", (form.genre.data, )).fetchall() #If they only search for genre, seach genre
            conn.commit()
            conn.close()
        elif form.name.data:
            conn = db_connect()
            djs = conn.execute("SELECT * FROM djs WHERE name LIKE ?", (form.name.data, )).fetchall() #if they only search for name do name
            conn.commit()
            conn.close()
    elif session.get('user'):
        conn = db_connect()
        djsf = conn.execute("SELECT * FROM djs AS d INNER JOIN djuser as u ON u.dj_id = d.dj_id WHERE u.user_id = ?", (session['user'],)).fetchall() #If they search for both, check both
        conn.commit()
        conn.close()

    return render_template('bookdj.html', djs=djs, form=form, dj=True, djsf=djsf)
@app.route("/logout")
def logout(): #If click logout
    session.clear() #clear all the session variables
    return redirect(url_for('login'))  #go back to login
@app.route('/<id>/booking/') #Grab an id with the booking url
def booking(id): #Book dj for an event
    if id is None:
        flash('No Event Found') #Give user feedback
        return redirect(url_for('host'))  #chuck back to host
    else:
        session['event'] = id #Grab the event id for later
        return redirect(url_for('djs')) #Redirect to djs page
@app.route('/<id>/sendbooking/') #grab the event id
def sendbooking(id): #Grab the dj id, and use session['event'] t put into table
    if id is None:
        flash('No DJ Found')# user feedback
        return redirect(url_for('djs'))  #Return back djs
    else:
        conn = db_connect()
        conn.execute("UPDATE events SET dj=? WHERE event_id = ? ", (id, session['event']) ) #Update the events and set the dj to the correct new dj
        conn.commit()
        conn.close()
        flash("Dj Booked!") #return some user feedback
        return redirect(url_for('host'))
@app.route('/<lang>/<artist>/changelangdesc/') #ended up not being added
def changelangdesc(lang,artist):
    session['lang'] = lang
    return redirect(url_for('artist', id=artist))
@app.route('/<id>/checkfriendevents/')
def checkfriendevents(id): #send a friend id into the events page to look at their information instead
    if id is None:
        flash('No Friend Found') #user feedback
        return redirect(url_for('friends'))
    else:
        session['friend'] = id #friend id setup
        return redirect(url_for('events')) #sent to friends
@app.route('/<id>/checkfriendsongs/')
def checkfriendsongs(id): #same as before but for songs favourited
    if id is None:
        flash('No Friend Found')
        return redirect(url_for('friends'))
    else:
        session['friend'] = id
        return redirect(url_for('songs'))
@app.route('/<id>/joinevent')
def joinevent(id): #Join the event that you click
    if session.get('user'):
        try:
            conn = db_connect()
            conn.execute("INSERT INTO eventuser (event_id, user_id) VALUES (?,?)", #insert the info into the eventuser table
                    (id, session['user'])
                         )
            conn.commit()
            conn.close()
            return redirect(url_for('joined'))
        except:
            flash("You are already part of this event!", "danger") #if that doesnt work, they are likely already part of the evnt
            return redirect(url_for('joined'))
    else:
        flash("sorry there was an error", "warning") #otheriwse, run and error
        return redirect(url_for('events'))
@app.route("/djcloseevent")
def djscloseevent(): #Just closesthis so you dont accidentallly book for the wrong person
    session['event'] = None
    return redirect(url_for('djs'))
@app.route("/<id>/favouritedj") #Favourite DJS
def favourite_dj(id):
    if session.get('user'):
        try:
            conn = db_connect()
            conn.execute("INSERT INTO djuser (dj_id, user_id) VALUES (?,?)", #put data into favourite djs table
                    (id, session['user'])
                         )
            conn.commit()
            conn.close()
            return redirect(url_for('djs'))
        except:
            flash("You have already favourited this DJ!", "danger") #Return user feedback
            return redirect(url_for('djs'))
    else:
        flash("sorry there was an error", "warning") #return user feedback
        return redirect(url_for('djs'))
@app.route('/<int:id>/unfavouritedj/') #unfavourite djs
def remove_favourite_dj(id):#same as before, but delete instead of insert
    if id is None:
        flash('NoD DJ ID Found')
        return redirect(url_for('djs'))
    conn = db_connect()
    conn.execute("DELETE FROM djuser WHERE user_id = ? AND dj_id = ?",
            (session['user'], id)
                )
    conn.commit()
    conn.close()
    return redirect(url_for('djs'))
@app.route('/<id>/seenextevent')
def seenextevent(id): #Similar to djs see next events but is a fetchone instead
    if id is None:
        flash('NoD DJ ID Found')
        return redirect(url_for('djs'))
    conn = db_connect()
    next = conn.execute("SELECT e.*, u.*FROM djs AS d INNER JOIN events AS e ON e.dj = d.dj_id INNER JOIN users AS u ON e.host = u.user_id WHERE e.private = 0 AND e.date > ? AND dj_id = ? ORDER BY e.date ASC ",
            (date.today(), id)).fetchone()

    conn.commit()
    conn.close()
    return render_template("events.html", eventlist=None, next=next, event=True) #Use the already made events page
@app.route('/<id>/invitetoevent') #Allow to invite poeple to events
def invitetoevent(id): #on your friends list you can click and post their id here
    if session.get('event'):
        try:
            conn = db_connect()
            conn.execute("INSERT INTO eventuser (event_id, user_id) VALUES (?,?)", #Put them in the event_user table
                    (session['event'], id)
                         )
            conn.commit()
            conn.close()
            session['event'] = None
            return redirect(url_for('host'))
        except:
            flash("They are already invited!", "danger") #otherwise they are already invited (feedback)
            return redirect(url_for('host'))
            session['event'] = None
    else:
        flash("sorry there was an error", "warning") #or there is an error (feedback)
        return redirect(url_for('host'))
        session['event'] = None
    session['event'] = None #Reset sessions just in case, i was having porblems earlier.
@app.route('/<id>/openfriends/') #Brings open the page where you can add friends to event
def open_friend(id):
    if id is None:
        flash('No Event Found')
        return redirect(url_for('host'))
    else:
        session['event'] = id #session the event id and send them to friends where you can invite.
    return redirect(url_for('friends'))
@app.route('/history', methods=['GET', 'POST']) #Get the event history for a DJ
def history():
    history1 = None #setting variables
    history2 = None
    information = []
    form=HistoryForm()
    if form.validate_on_submit(): #if the form goes through on their search
        location = form.location.data
        conn = db_connect()
        history1 = conn.execute("SELECT e.event_id, s.user_id, u.dob, t.strTrack, count(t.strTrack) FROM events AS e INNER JOIN songs_list AS s ON e.event_id = s.event_id INNER JOIN users AS u ON s.user_id = u.user_id INNER JOIN songs AS t ON s.song_id = t.idTrack WHERE e.location LIKE ? AND e.date <= ? GROUP BY u.dob", #grab the event corresponding to the location, with dobs
                (location, '2024-12-02')).fetchall()
        conn.commit()
        conn.close()
        conn = db_connect()
        history2 = conn.execute("SELECT e.event_id, s.user_id, u.dob, t.strTrack, count(t.strTrack) FROM events AS e INNER JOIN songs_list AS s ON e.event_id = s.event_id INNER JOIN users AS u ON s.user_id = u.user_id INNER JOIN songs AS t ON s.song_id = t.idTrack WHERE e.location LIKE ? AND e.date <= ? GROUP BY t.strTrack", #grab the event corresponding to the location, with the songs and votes
                (location, '2024-12-02')).fetchall()
        conn.commit()
        conn.close()
        information = []
        ages = []
        votes = []
        for i, event in enumerate(history2): #get together the information in order to use it effectively
            try:
                dob = history1[i]
                today = date.today()
                dob = datetime.strptime(dob[2], '%Y-%m-%d').date()
                ages.append(today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))) #get their age from dob
            except:
                votes.append(0)
            votes.append(history2[i])
            information.append([ages,votes]) #find the votes for song
            votes=[]
            ages=[]
            # information.append(votes)
    return render_template('history.html', form=form, history1=history1, history2=history2, information=information) #put them back through
@app.route('/<int:id>/declineevent/')# allowing the dj to decline an event
def declineevent(id): #Dj clicks button, declines event
    if id is None:
        flash('No Event ID Found')
        return redirect(url_for('events'))
    conn = db_connect()
    conn.execute("UPDATE events SET dj= NULL WHERE event_id = ? ", (id,) ) #Update into the events where the dj is supposed to be
    conn.commit()
    conn.close()
    return redirect(url_for('events'))
