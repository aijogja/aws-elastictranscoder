from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.conf import settings
from dj_elastictranscoder.transcoder import Transcoder
from video.models import Video

# Create your views here.


def home(request):

    video = Video.objects.first()

    inputfile = {
        'Key': 'check_sound.mp4',
    }

    outputfile = [{
        'Key': 'check_sound1235.mp4',
        'PresetId': '1351620000001-000020'
    }]

    pipeline_id = '1447246892935-kvvx1g'

    transcoder = Transcoder(pipeline_id)
    # import ipdb; ipdb.set_trace()
    transcoder.encode(inputfile, outputfile)

    # your can also create a EncodeJob for object automatically
    # transcoder.create_job_for_object(obj)

    # Transcoder can also work standalone without Django
    # just pass region and required aws key/secret to Transcoder, when
    # initiate

    # transcoder = Transcoder(pipeline_id, settings.AWS_REGION, settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    return HttpResponse('cek')
