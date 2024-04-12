# FIle has not been tested
# This file just verifys download, maybe show console output/input in installer...
download_score = 0
t_installer = 0
# For Input, ik there is other ways
yes_table = ['Y','y']
no_table = ['N','n']
# For Ease of changing all uses in file
github_url = r'https://github.com/QuickMash/DeCheaty'
# Verify the installer exists
if exists(path_to_file):
  print('Verified Installation files')
  download_score = download_score + 1
else:
  # This file is only required if using GUI installer
  t_installer = t_installer + 1
  print('Error! File installer files do not exist\n')
    redownload_p1 = input('Redownload files? (Y/n)')
  if redownload_p1 == yes_table:
    print('Download files')
  else:
    print('Go to', github_url , '\n or restart this file.')
if exists(path_to_file):
  print('Verified Source Files')
  download_score = download_score + 1
else:
  print('Source files do not exist!\nCritical Warning!')
  redownload_p2 = input('Redownload files? (Y/n)')
  if redownload_p2 == yes_table:
    print('Download files')
  else:
    print('Go to', github_url , '\n or restart this file, to reverify and do auto installation')
if download_score == 2:
  # Open the installer GUI
  open('path to installer')
else:
  print('Installer did not meet minimum installer requirements')
elif t_installer == 1:
  print('System will run terminal installer...')
  # Open the installer script(Python file)
  open('path to download')
