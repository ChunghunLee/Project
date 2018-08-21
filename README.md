# Project ?
It was the project that developed the 'Drone-Car license plate recognition' that I made when I progressed the senier project.

<<< 1st Step >>> 
By manually adjusting the drones, we have implemented the application to upload the pictures of the vehicles to the server in real time.
After the drones took a picture while flying, it send the photos to the server with the Android app.
(This app was also implemented simply for the purpose of transmission for server communication.)

<<< 2nd Step >>>
Once the photos are uploaded to the server, you connect to the server with a desktop or laptop and download the photos.
(This part will be implemented so that it will be automatically downloaded later.)

<<< 3rd Step >>>
Match the received picture file with the path created in the python file.
it use the Canny edge detection which detect the 'edge' in plate.
