from navAirpoint import NavAirport
from navPoint import NavPoint
from navSegment import NavSegment

class AirSpace:
    def __init__(self):
        self.list_navpoints=[]
        self.list_navsegments=[]
        self.list_navairports=[]

def LoadNavPoints(file, airspace):
    F=open(file, "r")
    line=F.readline()
    while line!="":
        trozos=line.rstrip().split()
        navpoint=NavPoint(trozos[0], trozos[1], trozos[2], trozos[3])
        airspace.list_navpoints.append(navpoint)
        line=F.readline
    F.close()

def LoadNavSegments(file, airspace):
    F = open(file, "r")
    line = F.readline()
    while line != "":
        trozos = line.rstrip().split()
        navseg = NavSegment(trozos[0], trozos[1], trozos[2])
        airspace.list_navsegments.append(navseg)
        line=F.readline()
    F.close()

def LoadNavAirports(file,airspace):
    mateixAer=None
    noms=[]
    F=open(file, "r")
    for line in F:
        line=line.strip()
        if line.startswith("LE") and len(line)==4:
            if mateixAer:
                noms.append(mateixAer)
            mateixAer=NavAirport(line)
        if line.endswith(".D"):
            mateixAer.sid.append(line)
        elif line.endswith(".A"):
            mateixAer.star.append(line)
    if mateixAer:
        noms.append(mateixAer)
    return(noms)


