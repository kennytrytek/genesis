from os.path import dirname, join, realpath

from google.appengine.ext.webapp import template


def render(filepathgroup, **kwargs):
    path = join(dirname(realpath(filepathgroup[0])), filepathgroup[1])
    return template.render(path, kwargs)
