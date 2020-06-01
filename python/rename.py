import argparse
import os
import re

parser = argparse.ArgumentParser(description='Rename files by regex')
parser.add_argument('regex', type=str,
                    help='patern for renaming files or directories', )
parser.add_argument('replacer', type=str, help='string what replaced a patern', )
parser.add_argument('path', nargs='?', type=str, default='.',
                    help='path to directory for scaning', )
args = parser.parse_args()

regex = re.compile(args.regex, re.IGNORECASE)

files_by_regex = []
failed_files = []

for root, dirs, files in os.walk(args.path):
  for file in files:
    if regex.search(file):      
      replace = regex.sub(args.replacer, file)
      files_by_regex.append([root, file, replace])
      print(replace)

answer = input('\nDo you want to accept this? [y|N] ')

if answer and answer.lower()[0] == 'y':
  for root, file, replace in files_by_regex:
    try:
      os.rename(os.path.join(root, file), os.path.join(root, replace))
    except Exception as e:     
      failed_files.append([root, file])

  print(f'\n{len(files_by_regex) - len(failed_files)} files was renamed')

  if failed_files:
    print('\nfailed files:')
  for root, file in failed_files:
    print(os.path.join(root, file))