# encoding=utf-8
import logging

from django.conf import settings
from django.db.models.fields.files import ImageFieldFile

__author__ = 'quxl'

log = logging.getLogger('root')

class  UploadTo(object):

    def __init__(self,upload_to="",filename_prefix=None,*args,**kwargs):
        if  filename_prefix:
            filename_prefix+="_"
        else:
            filename_prefix = ""
        self.args = args
        self.kwargs = kwargs
        self.upload_to = upload_to
        self.filename_prefix = filename_prefix

    def __call__(self, instance,file_name):
        return "%s/%s%s"%(self.upload_to,self.filename_prefix,self.generate_filename(instance,file_name))

    def generate_filename(self,instance,file_name):
        log.debug(type(instance.file))
        if isinstance(instance.file,ImageFieldFile):
            return file_name.replace('.','_%s_%s.'%(instance.file.width,instance.file.height))
        else:
            return file_name



