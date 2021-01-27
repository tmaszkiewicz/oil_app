# oil_app

Oil dispenser reporting part. The sources need to be run under the django (possibly in docker virual env) and cooperate with the raspberry PI in the Oil dispenser. 

Also py script "czytnik_kart.py" is added to repository. It should be started on the rasp. 

Rasp is connected to optoisolated relay that releases oildrop. the scrpt is triggered through  an RFID reader (kind of keyboard).

