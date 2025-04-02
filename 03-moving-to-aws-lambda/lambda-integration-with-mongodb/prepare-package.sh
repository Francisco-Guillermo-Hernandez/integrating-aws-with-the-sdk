#!/bin/bash


zipFileName="lambda-function.zip"
libsDirName="package"

preparePackage() {
   cd $libsDirName || return
   if zip -v &> /dev/null; then
      zip -r $zipFileName .
      mv $zipFileName ..
      cd ..
      zip $zipFileName lambda_function.py database.py
      echo "The zip file is ready to upload."
   else
      echo "Please install zip util."
   fi
}

installDependencies() {
  if [ -d "$libsDirName" ]; then
    echo "Zipping the files ..."
    preparePackage
  else
    echo "Installing packages"
    pip install -r requirements.txt --target ./package
    preparePackage
  fi
}

installDependencies