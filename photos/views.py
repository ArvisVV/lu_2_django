from django.shortcuts import render
from django.http import HttpResponse

from photos import (
    forms,
    models,
)


def upload_photo(request):
    if request.method == 'POST':
        form = forms.PhotoUploadForm(
            data=request.POST,
            files=request.FILES,
        )

        if form.is_valid():
            form.save()

            return HttpResponse('File is uploaded')

    else:
        form = forms.PhotoUploadForm()

    return render(
        request=request,
        template_name='photos/upload.html',

        context={
            'form': form,
        }
    )


def view_photo(request, photo_id):
    photo = models.Photo.objects.get(id=photo_id)

    # sql = 'SELECT * FROM photos_photo WHERE photos_photo.id = %s'
    # photo = models.Photo.objects.raw(sql, [photo_id])

    return HttpResponse(f'Photo path: {photo.picture}')
