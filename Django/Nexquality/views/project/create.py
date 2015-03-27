from Nexquality.views.mixins import LoginRequiredMixin
from Nexquality.models import Project
from django.views.generic import edit
from django.core.urlresolvers import reverse


class ProjectCreationView(LoginRequiredMixin, edit.CreateView):
    model = Project
    fields = ['name']
    template_name = 'project/update.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ProjectCreationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('Nexquality:project:update', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(ProjectCreationView, self).get_context_data(**kwargs)
        context['title'] = 'New project'
        return context
