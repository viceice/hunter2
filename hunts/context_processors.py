from django.db.models import Q

from hunts import models
from hunts.models import AnnoucmentType


def announcements(request):

    # Get all announcements, including puzzle specific announcements if present
    has_puzzle = hasattr(request, 'puzzle') and request.puzzle is not None

    css_class = {
        AnnoucmentType.INFO: 'alert-info',
        AnnoucmentType.SUCCESSS: 'alet-success',
        AnnoucmentType.WARNING: 'alert-warning',
        AnnoucmentType.ERROR: 'alert-danger',
    }

    if has_puzzle:
        current_announcements = models.Annoucement.objects.filter(
            (Q(event__isnull=True) | Q(event=request.event)) &
            (Q(puzzle__isnull=True) | Q(puzzle=request.puzzle)))
    else:
        current_announcements = models.Annoucement.objects.filter(
            (Q(event__isnull=True) | Q(event=request.event)) &
            (Q(puzzle__isnull=True)))

    # TODO: This is relatively closely linked to the CSS so perhaps should be further moved to the view / template
    for announcement in current_announcements:
        announcement.css_type = css_class[announcement.type]

    return {
        'announcements': current_announcements
    }