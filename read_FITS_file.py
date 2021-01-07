def load_fits(fit):
  arq = fits.open(fit)
  return arq.info()



if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image0.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 
