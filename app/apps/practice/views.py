from django.shortcuts import get_object_or_404, render

from apps.base.models import Section

from .models import Activity

KIND_URLS = {
    Activity.Kind.RECIPE: 'practice:recipes',
    Activity.Kind.MASTERCLASS: 'practice:masterclasses',
    Activity.Kind.TASK: 'practice:tasks',
}


def _section():
    return Section.objects.get(key='practice')


def index(request):
    activities = Activity.objects.published()
    groups = [
        {'kind': kind, 'label': label, 'url_name': KIND_URLS[kind], 'items': activities.filter(kind=kind)[:3]}
        for kind, label in Activity.Kind.choices
    ]
    return render(request, 'practice/index.html', {'section': _section(), 'groups': groups})


def activity_list(request, kind):
    return render(request, 'practice/activity_list.html', {
        'section': _section(),
        'kind': kind,
        'kind_label': Activity.Kind(kind).label,
        'activities': Activity.objects.published().filter(kind=kind),
        'kinds': [(k, label, KIND_URLS[k]) for k, label in Activity.Kind.choices],
    })


def activity_detail(request, kind, slug):
    activity = get_object_or_404(Activity.objects.published(), kind=kind, slug=slug)
    return render(request, 'practice/activity_detail.html', {
        'section': _section(),
        'activity': activity,
        'kind_label': Activity.Kind(kind).label,
        'list_url': KIND_URLS[kind],
        'supplies': activity.supplies.all(),
        'steps': activity.steps.all(),
        'more': Activity.objects.published().filter(kind=kind).exclude(pk=activity.pk)[:3],
    })
