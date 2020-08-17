# -*- coding: utf-8 -*-

"""
    Upload folder to Google Drive
"""

# Enable Python3 compatibility
from __future__ import (unicode_literals, absolute_import, print_function, division)

# Import Google libraries
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import GoogleDriveFileList
import googleapiclient.errors

# Import general libraries
from argparse import ArgumentParser
from os import chdir, listdir, stat
from sys import exit
import ast

class GDrive:
  def __init__(self):
    print("inicia enlase Google Drive")

  def authenticate(self):
    """ 
		Authenticate to Google API
	  """
    gauth = GoogleAuth()
    return GoogleDrive(gauth)

  def crearFolder(self):
    #Create folder
    id_canbalashamdo = "1tzu7XbsTL-6UYxZPtYpCl5IEeOTO4DHB"
    drive = self.authenticate()
    folder_metadata = {'title' : 'otraPrub', 'mimeType' : 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    #Get folder info and print to screen
    foldertitle = folder['title']
    folderid = folder['id']
    print('title: %s, id: %s' % (foldertitle, folderid))
    return folderid

  def listaArchivos(self):
    drive = self.authenticate()
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
      print('title: %s, id: %s' % (file1['title'], file1['id']))
    return file_list

  def cargarFiles(self):
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    path_to_upload_file = ""
    drive = GoogleDrive(gauth)
    file_upload = drive.CreateFile({'title': 'test_file.txt', 'mimeType' : 'text/plain'})
    file_upload.SetContentFile(path_to_upload_file)
    file_upload.Upload()
    return True

    