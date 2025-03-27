#PYTHON UNIT 6

#question 1
class SongNode:
	# def __init__(self, song, next=None):
	# 	self.song = song
	# 	self.next = next
    
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next
    

# For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
    print()
		
# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))


#test
# print_linked_list(top_hits_2010s)

# Problem 2
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def get_artist_frequency(playlist):
    frequency = {}
    curr = playlist
    while curr:
        frequency[curr.artist] = frequency.get(curr.artist, 0) + 1

       # if curr.artist in frequency:
        #    frequency[curr.artist] += 1
        #else:
         #   frequency[curr.artist] = 1
        curr = curr.next
    return frequency

#test
playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

#print(get_artist_frequency(playlist))


#problem 3
# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))

#problem 4
def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head
    
    while fast and fast.next: #we do both bc if fast becomes none, theres no cycle, and since fast.next moves 2 steps, we needa make sure fast.next exists before jumping to .next.next. if fast.next is none, .n.n would raise error (i did some searching)
        slow = slow.next
        fast = fast.next.next #bc moving 2 steps
        
        if slow == fast:
            return True
    return False


song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))