from django.shortcuts import render
import markdown2
from . import util
import random
from django.urls import reverse
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
# ToDo: Edit page
# ToDo: Warning if Article already exists
# ToDo: Enhanced search with regex

def index(request):
    entries = util.list_entries()
    entries.sort(key = str.lower)
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def wiki(request, pageName):
    return render(request, "encyclopedia/wikipage.html", {
        "pageName": f"{pageName}",
        "wikiEntry": markdown2.markdown(util.get_entry(f"{pageName}"), extras=["tables"])
    })

def search(request):
    query = request.GET.get('q', None)
    entries = util.list_entries()
    try:
        index_no = entries.index(query)
        return render(request, "encyclopedia/wikipage.html", {
            "pageName": f"{pageName}",
            "wikiEntry": markdown2.markdown(util.get_entry(f"{entries[index_no]}"))
            })
    except ValueError:
        pos_results = list()
        for i in entries:
            if i.find(query) != -1:
                pos_results.append(i)
            else:
                pass
        return render(request, "encyclopedia/search_results.html", {
            "search_results": pos_results
            })

def randomPage(request):
    entries = util.list_entries()
    pageName = entries[random.randrange(0, len(entries) - 1)]
    return HttpResponseRedirect(reverse("wiki", args=(pageName,)))

def createPage(request):
    if request.method == "POST":
        pageName = request.POST.get('nTitle', )
        if util.entry_exists(pageName):
            return render(request, "encyclopedia/edit_page.html", {
            "pageName": pageName,
            "pageContent": util.get_entry(f"{pageName}")
            })
        else:
            util.save_entry(pageName, request.POST.get('nPage', ))
            return HttpResponseRedirect(reverse("wiki", args=(pageName,)))
        return render(request, "encyclopedia/wikipage.html", {
            "pageName": f"{pageName}",
            "wikiEntry": markdown2.markdown(util.get_entry(f"{pageName}"), extras=["tables"])
        })
    else:
        return render(request, "encyclopedia/create_new.html")

def editPage(request):
    pageName = request.POST.get('nPageName', )
    if request.method == "POST" and request.POST.get('nForm', ) == "edit":
        return render(request, "encyclopedia/edit_page.html", {
            "pageName": pageName,
            "pageContent": util.get_entry(f"{pageName}")
            })
    elif request.method == "POST" and request.POST.get('nForm', ) == "save":
        util.save_entry(pageName, request.POST.get('nPage', ))
        return HttpResponseRedirect(reverse("wiki", args=(pageName,)))
    else:
        return HttpResponseRedirect(reverse("index"))
        



