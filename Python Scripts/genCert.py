from subprocess import call

#Get client name
client = raw_input("Client Name?  ")
openSslCmd1  = "openssl req -newkey rsa:2048 -days 3600 -nodes -keyout " + client + "-key.pem -out " + client + "-req.pem"
call(openSslCmd1, shell=True)
#print("US")

openSslCmd2 = "openssl rsa -in " + client + "-key.pem -out " + client + "-key.pem"
call(openSslCmd2, shell=True)

openSslCmd3 = "openssl x509 -req -in " + client + "-req.pem -days 3600 -CA ca.pem -CAkey ca-key.pem -set_serial 01 -out " + client + "-cert.pem"
call(openSslCmd3, shell=True)

certFile = "openssl pkcs12 -export -in " + client + "-cert.pem -inkey " + client + "-key.pem -certfile ca.pem -out " + client + ".pfx"
call(certFile, shell=True)

#Make directory to store keys/certifcate in
dir = client + "cert"
mkDir = "mkdir " + dir
call(mkDir, shell=True)

#Move all generated files associated with client to newly created directory
moveFiles = "mv *" + client + "-* " + dir
moveCert = "mv " + client + ".pfx " + dir
call(moveFiles, shell=True)
call(moveCert, shell=True)



 

