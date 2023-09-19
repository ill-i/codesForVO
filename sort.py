import os
import shutil

files = os.listdir()

for f in files:
  if ".hdr" in f:
    with open(f) as h:
      for line in h.readlines():
        if "WCSAXES" not in line:
          print("no wcs",f)
          shutil.move(os.getcwd()+"/"+f.replace(".hdr",""), "/var/gavo/inputs/astroplates/maksutov_50_telescope/wcs_failed/"+f.replace(".hdr",""))
          shutil.move(os.getcwd()+"/"+f, "/var/gavo/inputs/astroplates/maksutov_50_telescope/wcs_failed/"+f)
        else:
          print("wcs",f)
          shutil.move(os.getcwd()+"/"+f.replace(".hdr",""), "/var/gavo/inputs/astroplates/maksutov_50_telescope/header_done/"+f.replace(".hdr",""))
          shutil.move(os.getcwd()+"/"+f, "/var/gavo/inputs/astroplates/maksutov_50_telescope/header_done/"+f)
