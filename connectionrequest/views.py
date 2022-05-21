from django.shortcuts import render
from .forms import ConnectionRequestForm
from django.shortcuts import render, redirect, reverse, get_object_or_404


def send_connection_request(request):
    """ A view to return the connection request page """

    form = ConnectionRequestForm()

    if request.method == "POST":
        form = ConnectionRequestForm(request.POST)
        if form.is_valid():
            new_connection_request = form.save()
            print("NEW CONNECTION REQUEST CREATED")
            print(new_connection_request.request_id)
            # messages.success(
            #     request,
            #     f"Instructor Profile for \
            #                 {instructor.friendly_name} created",
            # )
        else:
            # messages.error(
            #     request,
            #     "Unable to Instructor Profile. Please check \
            #     that the form is valid",
            # )
            print("CONNECTION REQUEST FAILED")

        return redirect(reverse("send_connection_request"))

    context = {
        'form': form,
    }

    return render(request, 'connectionrequest/send-request.html', context)
