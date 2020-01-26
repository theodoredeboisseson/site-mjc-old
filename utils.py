from django.utils.text import slugify


def clean_filename(filename):
    slug = slugify(filename)
    ext = filename.split(".")[-1]
    clean_fn = slug[0:len(slug)-len(ext)] + "." + ext
    return clean_fn


def upload_path_handler(instance, filename):
    return "files/{folder}/{file}".format(folder=instance.folder ,file=clean_filename(filename))