from astropy.io import fits
import os


files = [files_ for files_ in os.listdir() if "fit" in files_]

for f in files:
  print(f)
  file_name = f.replace(".hdr","").replace(".fit","")
  if "hdr" not in f:
    fit_file = fits.open(f,mode="update")
    # Define the keyword and its value
    keyword = 'FILENAME'
    value = file_name.replace("_"," ")
    # Add the new keyword to the header
    fit_file[0].header[keyword] = value

    # Save the changes to the FITS file
    fit_file.flush()

    # Close the FITS file
    fit_file.close()

  else:
    # Open the FITS header for editing
    header = fits.Header.fromtextfile(f)

    # Add a keyword with a value to the header
    header['FILENAME'] = file_name

    # Save the modified header back to the .hdr file
    header.totextfile(f, overwrite=True)    
