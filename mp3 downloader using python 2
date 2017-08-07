import re, urllib , os , sys #import all library used
 user_input = raw_input
 import urllib2
 urlopen = urllib2.urlopen
 encode = urllib.urllenode
 retrieve = urllib.urlretrieve
 cleanup = urllib.urlcleanup()
 def screen_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#function to retrieve video title from given link
def video_title(url):
    try:
        webpage = urlopen(url).read()
        title = str(webpage).split('<title>')[1].split('</title>')[0]
    except:
        title = 'youtube song'
    return title 
#the intro to script
def intro():
    print('''created by shubham singh
    FB:- Meshubham001
    Email:- meshubhama01@gmail.com''')

#what user want to do
def prompt():                                              #promp to asking mode
    print ('''\t\t\t select a mode
    [1] download from a list
    [2] download from direct entry
    press any other key to exit''')

    choice = user_input('>>> ')
    return str(choice)
    # download from a list of songs or links
def list_download():
    fileName = user_input('fileName(with extension): ')  # get the file name to be opened

    # find the file and set fhand as handler
    try:
        fhand = open(fileName, 'r')
    except IOError:
        print('File does not exist')
        exit(1)
 # Iterating over the lines in file
    for song in fhand:
        single_download(song)

    fhand.close()

#to download song directly with name or link
def single_download(song=None):
    if not(song):
          song = user_input('Enter the song name or youtube link: ')  # get the song name from user
  
     if "youtube.com/" not in song:
                                                                           # try to get the search result and exit upon error
     try:
         query_string = encode({"search_query" : song})
         html_content = urlopen("http://www.youtube.com/results?" + query_string)
		 search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read())
     except:
	     print('Network Error')
         return None
         try:
             query_string = encode({"search_query" : song})
             html_content = urlopen("http://www.youtube.com/results?" + query_string)
			 search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read())
	 	  except:
             print('Network Error')
            return None 
         # generate a download link that can be used to get the audio file using youtube2mp3 API
         downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]
	else:      # For a link
         downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video='+song
         song=video_title(song)
    
    else:      # For a link
         downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video='+song
         song=video_title(song)
  
     # generate a download link that can be used to get the audio file using youtube2mp3 API
    downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]
      try:
          print('Downloading %s' % song)
          # code a progress bar for visuals? this way is more portable than wget
         retrieve(downloadLinkOnly, filename='%s.mp3' % song)
         cleanup  # clear the cache created by urlretrieve
      except:
         print('Error downloading %s' % song)
         return None		 
 def exit(code):
     print('\nExiting....')
     print('\nHave a good day.')
     sys.exit(code)
  # main guts of the program
 def main():
     try:
         screen_clear()
         intro()
         choice = prompt()
 
         try:
             if choice == '1':
                 list_download()
             elif choice == '2':
                 single_download()
         except NameError:
             exit(1)
     except KeyboardInterrupt:
         exit(1)
     exit(1)
 
 if __name__ == '__main__':
     main()  # run the main program
     exit(0)  # exit the program
