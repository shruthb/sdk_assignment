import re
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sdk
PORT_NUMBER = 8080

#This class will handles any incoming request from the browser 
class myHandler(BaseHTTPRequestHandler):
        
        #Handler for the GET requests
        def do_GET(self):
                self.send_response(200)
                #self.headers used nto extract the headers
                           
                m=re.search("User-Agent:\s([a-z A-Z 0-9 / \. ' ' \- ; \, ( ) :]*[0-9 \.]*)",str(self.headers))
                print "The following is the user agent\n"
                print m.group(1),'\n \n'
                
                usragent=m.group(1)
                
                self.send_header('Content-type','text/html')
                self.end_headers()
                # checks for touch support
                if sdk.isTouch(usragent)==None :
                    self.wfile.write("touch support not known")
                else:
                    st="supported" if sdk.isTouch(usragent) else "not supported"
                    st1="Touch: "+st
                    self.wfile.write(st1)
                self.wfile.write('\n')

                #Gives RAM
                ram=sdk.getRAM(usragent)
                if ram==None:
                    ram="not known"
                self.wfile.write("RAM in GB: "+str(ram))
                self.wfile.write('\n')

                #Gives display width
                disp=sdk.getDisplayWidth(usragent)
                if disp==None:
                        disp="not known"
                self.wfile.write("Display width in pixels: "+str(disp))
                self.wfile.write('\n')

                #Gives OS
                os=sdk.getOS(usragent)
                if os==None:
                    os="not known"
                self.wfile.write("OS of device: "+os)
                self.wfile.write('\n')

                #Gives height of device
                ht=sdk.getHeight(usragent, st="mm")
                if ht==None:
                        ht="not known"
                self.wfile.write("height of device in mm: "+str(ht))
                self.wfile.write('\n')
                
                #Checks for bluetooth 
                if sdk.isBluetooth(usragent)==None:
                    self.wfile.write("Bluetooth support not known")
                else:
                    st="supported" if sdk.isBluetooth(usragent) else "not supported"
                    st1="Bluetooth: "+st
                    self.wfile.write(st1)
                self.wfile.write('\n')

                #Gives internal memory
                mem=sdk.getInternalMemory(usragent) 
                if mem==None:
                    mem="not known"
                self.wfile.write("Internal Memory in GB: "+str(mem))
                self.wfile.write('\n')

                #Gives no of sims in device
                st3=sdk.getSimNum(usragent)
                if st3==None:
                    st3="not known"
                self.wfile.write("Number of sims: "+str(st3))
                self.wfile.write('\n')
                
            

try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print 'Started httpserver on port ' , PORT_NUMBER
        
        #Wait forever for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()

